from miko import *


@MIKO.BOT("getubot")
@MIKO.OWNER
@bot.on_message(filters.command(["gubt"], "/") & filters.user(DEVS))
async def _(client, message):
    await getubot_cmd(client, message)


@MIKO.CALLBACK("^(get_otp|get_phone|get_faktor|ub_deak|deak_akun)")
async def _(client, callback_query):
    await tools_userbot(client, callback_query)


@MIKO.CALLBACK("cek_masa_aktif")
async def _(client, callback_query):
    await cek_userbot_expired(client, callback_query)


@MIKO.CALLBACK("del_ubot")
async def _(client, callback_query):
    await hapus_ubot(client, callback_query)

    
@MIKO.CALLBACK("^(p_ub|n_ub)")
async def _(client, callback_query):
    await next_prev_ubot(client, callback_query)
