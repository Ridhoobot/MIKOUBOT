from miko import *



@PY.CALLBACK("gratis")
async def _(client, callback_query):
    await bikin_gratis(client, callback_query)


@PY.CALLBACK("st12")
async def _(client, callback_query):
    await ohaja(client, callback_query)


@PY.CALLBACK("bubt")
async def _(client, callback_query):
    await bikin_memek(client, callback_query)


@PY.CALLBACK("bahan")
async def _(client, callback_query):
    await need_api(client, callback_query)


@PY.CALLBACK("bayar_dulu")
async def _(client, callback_query):
    await payment_userbot(client, callback_query)


@PY.CALLBACK("add_ubot")
async def _(client, callback_query):
    await bikin_ubot(client, callback_query)
