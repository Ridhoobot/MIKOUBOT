from miko import *


@MIKO.BOT("sh")
@MIKO.OWNER
@bot.on_message(filters.command(["sh"], "/") & filters.user(DEVS))
async def _(client, message):
    await shell_cmd(client, message)


@MIKO.UBOT("eval")
@MIKO.OWNER
@bot.on_message(filters.command(["eval"], "/") & filters.user(DEVS))
async def _(client, message):
    await evalator_cmd(client, message)


@MIKO.UBOT("trash")
@MIKO.TOP_CMD
async def _(client, message):
    await trash_cmd(client, message)


@MIKO.BOT("getotp|getnum")
@MIKO.OWNER
async def _(client, message):
    await get_my_otp(client, message)

