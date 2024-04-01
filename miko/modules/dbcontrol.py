from miko import *


@MIKO.BOT("prem")
@MIKO.UBOT("prem")
async def _(client, message):
    await prem_user(client, message)


@MIKO.BOT("unprem")
@MIKO.UBOT("unprem")
@MIKO.OWNER
async def _(client, message):
    await unprem_user(client, message)


@MIKO.BOT("getprem")
@MIKO.UBOT("getprem")
@MIKO.OWNER
async def _(cliebt, message):
    await get_prem_user(client, message)


@MIKO.BOT("seles")
@MIKO.OWNER
@bot.on_message(filters.command(["seles"], "/") & filters.user(DEVS))
async def _(client, message):
    await seles_user(client, message)


@MIKO.BOT("unseles")
@MIKO.OWNER
async def _(client, message):
    await unseles_user(client, message)


@MIKO.BOT("getseles")
@MIKO.OWNER
async def _(client, message):
    await get_seles_user(client, message)


@MIKO.BOT("topcmd")
@MIKO.OWNER
@bot.on_message(filters.command(["topcmd"], "/") & filters.user(DEVS))
async def _(client, message):
    await get_top_module(client, message)


@MIKO.BOT("time")
@MIKO.UBOT("time")
@MIKO.OWNER
@bot.on_message(filters.command(["setexp"], "/") & filters.user(DEVS))
async def _(client, message):
    await expired_add(client, message)


@MIKO.BOT("cek")
@MIKO.UBOT("cek")
@MIKO.OWNER
@bot.on_message(filters.command(["cek"], "/") & filters.user(DEVS))
async def _(client, message):
    await expired_cek(client, message)


@MIKO.BOT("untime")
@MIKO.UBOT("kill")
@MIKO.OWNER
async def _(client, message):
    await un_expired(client, message)


@MIKO.CALLBACK("restart")
async def _(client, callback_query):
    await cb_restart(client, callback_query)

