from miko import *



@MIKO.CALLBACK("^profil")
async def _(client, callback_query):
    await profil_callback(client, callback_query)
