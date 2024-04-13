from miko import *

__MODULE__ = "Copy"
__HELP__ = """
 Bantuan Untuk Copy

• Perintah : <code>{0}copy</code> [link]
• Penjelasan : Untuk mengambil pesan melalui link telegram.
  """


@MIKO.BOT("copy")
async def _(client, message):
    await copy_bot_msg(client, message)


@MIKO.UBOT("copy", sudo=True)
async def _(client, message):
    await copy_ubot_msg(client, message)


@MIKO.UBOT("ccopy")
async def _(client, message):
    await cancel_nyolong(client, message)


@MIKO.INLINE("^get_msg")
@INLINE.QUERY
async def _(client, inline_query):
    await copy_inline_msg(client, inline_query)


@MIKO.CALLBACK("^copymsg")
@INLINE.DATA
async def _(client, callback_query):
    await copy_callback_msg(client, callback_query)
