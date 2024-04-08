# Copas Teriak Copas MONYET
# Gay Teriak Gay Anjeng
# @Rizzvbss | @Kenapanan
# Kok Bacot
# © @KynanSupport
# FULL MONGO NIH JING FIX MULTI CLIENT


from asyncio import sleep
from contextlib import suppress
from random import randint
from typing import Optional

from pyrogram import Client, enums, filters
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.raw.types import InputGroupCall, InputPeerChannel, InputPeerChat
from pyrogram.types import Message

from miko import *
from pytgcalls import GroupCallFactory 

MODULE = "vctools"
HELP = f"""
✘ Bantuan Untuk Voice Chat

๏ Perintah: <code>startvc</code>
◉ Penjelasan: Untuk memulai voice chat grup.

๏ Perintah: <code>stopvc</code>
◉ Penjelasan: Untuk mengakhiri voice chat grup.
           
๏ Perintah: <code>naik</code>
◉ Penjelasan: Untuk bergabung voice chat grup.

๏ Perintah: <code>turun</code>
◉ Penjelasan: Untuk meninggalkan voice chat grup.
"""


async def get_group_call(
    client: Client, message: Message, err_msg: str = ""
) -> Optional[InputGroupCall]:
    chat_peer = await client.resolve_peer(message.chat.id)
    if isinstance(chat_peer, (InputPeerChannel, InputPeerChat)):
        if isinstance(chat_peer, InputPeerChannel):
            full_chat = (await client.send(GetFullChannel(channel=chat_peer))).full_chat
        elif isinstance(chat_peer, InputPeerChat):
            full_chat = (
                await client.send(GetFullChat(chat_id=chat_peer.chat_id))
            ).full_chat
        if full_chat is not None:
            return full_chat.call
    await eor(message, f"No group call Found {err_msg}")
    return False

list_data = []


def remove_list(user_id):
    list_data[:] = [item for item in list_data if item.get("id") != user_id]


def add_list(user_id, text):
    data = {"id": user_id, "nama": text}
    list_data.append(data)


def get_list():
    if not list_data:
        return "<b>ᴛɪᴅᴀᴋ ᴀᴅᴀ ᴜsᴇʀ ᴅɪ ᴅᴀʟᴀᴍ ᴏʙʀᴏʟᴀɴ sᴜᴀʀᴀ ᴍᴀɴᴀᴘᴜɴ</b>"

    msg = "\n".join(item["nama"] for item in list_data)
    return msg


@MIKO.UBOT("naik", sudo=True)
@MIKO.TOP_CMD
async def _(client, message):
    chat_id = message.command[1] if len(message.command) > 1 else message.chat.id
    text = f"• <b>[{client.me.first_name} {client.me.last_name or ''}](tg://user?id={client.me.id})</b> | <code>{chat_id}</code>"
    try:
        await client.group_call.start(chat_id, join_as=client.me.id)
    except Exception as e:
        return await message.reply(f"ERROR: {e}")
    await message.reply("<b>izin parkir puh</b>")
    await asyncio.sleep(5)
    await client.group_call.set_is_mute(True)
    add_list(client.me.id, text)


@MIKO.UBOT("turun", sudo=True)
@MIKO.TOP_CMD
async def _(client, message):
    try:
        await client.group_call.stop()
    except Exception as e:
        return await message.reply(f"ERROR: {e}")
    remove_list(client.me.id)
    return await message.reply("<b>izin turun puh</b>")


@MIKO.UBOT("listos")
@MIKO.OWNER
async def _(client, message):
    await message.reply(get_list())

@MIKO.UBOT("startvc")
async def start_vctools(client, message):
    flags = " ".join(message.command[1:])
    ky = await message.reply("<code>Processing....</code>")
    vctitle = get_arg(message)
    if flags == enums.ChatType.CHANNEL:
        chat_id = message.chat.title
    else:
        chat_id = message.chat.id
    args = (
        f"<b>• Obrolan Suara Aktif</b>\n<b>• Chat : </b><code>{message.chat.title}</code>"
    )
    try:
        if not vctitle:
            await client.invoke(
                CreateGroupCall(
                    peer=(await client.resolve_peer(chat_id)),
                    random_id=randint(10000, 999999999),
                )
            )
        else:
            args += f"\n • <b>Title : </b> <code>{vctitle}</code>"
            await client.invoke(
                CreateGroupCall(
                    peer=(await client.resolve_peer(chat_id)),
                    random_id=randint(10000, 999999999),
                    title=vctitle,
                )
            )
        await ky.edit(args)
    except Exception as e:
        await ky.edit(f"<b>INFO:</b> `{e}`")


@MIKO.UBOT("stopvc")
async def stop_vctools(client, message):
    ky = await message.reply("<code>Processing....</code>")
    message.chat.id
    if not (
        group_call := (await get_group_call(client, message, err_msg=", Kesalahan..."))
    ):
        return
    await client.invoke(DiscardGroupCall(call=group_call))
    await ky.edit(
        f"<b>• Obrolan Suara Diakhiri</b>\n<b>• Chat : </b><code>{message.chat.title}</code>"
)
