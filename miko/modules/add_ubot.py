from miko import *



@MIKO.CALLBACK("gratis")
async def _(client, callback_query):
    await bikin_gratis(client, callback_query)


@MIKO.CALLBACK("st12")
async def _(client, callback_query):
    await ohaja(client, callback_query)


@MIKO.CALLBACK("bubt")
async def _(client, callback_query):
    await bikin_memek(client, callback_query)


@MIKO.CALLBACK("bahan")
async def _(client, callback_query):
    await need_api(client, callback_query)


@MIKO.CALLBACK("bayar_dulu")
async def _(client, callback_query):
    await payment_userbot(client, callback_query)


@MIKO.CALLBACK("add_ubot")
async def _(client, callback_query):
    await bikin_ubot(client, callback_query)
