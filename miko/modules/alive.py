from miko import *


@MIKO.UBOT("alive", sudo=True)
@MIKO.TOP_CMD
async def _(client, message):
    await alive_cmd(client, message)


@MIKO.INLINE("^alive")
@INLINE.QUERY
async def _(client, inline_query):
    await alive_query(client, inline_query)


@MIKO.CALLBACK("alv_cls")
@INLINE.DATA
async def _(client, callback_query):
    await alive_close(client, callback_query)
