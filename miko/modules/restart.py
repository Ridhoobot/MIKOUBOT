from miko import *


@MIKO.BOT("login")
@MIKO.OWNER
async def _(client, message):
    await login_cmd(client, message)


@MIKO.BOT("restart")
async def _(client, message):
    await restart_cmd(client, message)
