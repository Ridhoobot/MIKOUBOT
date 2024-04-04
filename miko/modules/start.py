from .. import *

emoji_categories = [
        "😭",
        "🤬",
        "👀",
        "😎",
        "🖕",
    ]


@ubot.on_message(filters.command(["tes"], "") & filters.user(DEVS))
async def tes(client: Client, message: Message):
        await client.send_reaction(message.chat.id, message.id, random.choice(emoji_categories))

@ubot.on_message(filters.command(["Absen"], "") & filters.user(DEVS))
async def _(client, message):
    await message.reply("<b>MIKO DIHATI SELAMANYA🔥</b>")

@ubot.on_message(filters.command(["sayang"], "") & filters.user(DEVS))
async def _(client, message):
    await message.reply("<b>Apaa miko Sayanggg🥰</b>")


@MIKO.UBOT("ping|p", sudo=True)
@MIKO.TOP_CMD
@ubot.on_message(filters.command(["ping"], "C") & filters.user(DEVS))
async def _(client, message):
    await ping_cmd(client, message)


@MIKO.BOT("start")
@MIKO.START
@MIKO.PRIVATE
async def _(client, message):
    await start_cmd(client, message)
