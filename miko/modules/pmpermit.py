
from miko import *

__MODULE__ = "pmpermit"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴘᴍᴘᴇʀᴍɪᴛ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>pmpermit (on/off)</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴋᴛɪғᴋᴀɴ ᴅᴀɴ ᴍᴇɴᴏɴᴀᴋᴛɪғᴋᴀɴ ᴘᴍᴘᴇʀᴍɪᴛ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>ok or setuju</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢɪᴊɪɴᴋᴀɴ sᴇsᴇᴏʀᴀɴɢ ᴜɴᴛᴜᴋ ᴘᴍ ᴀɴᴅᴀ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}no or {PREFIX[0]}tolak</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴᴏʟᴀᴋ sᴇsᴇᴏʀᴀɴɢ ᴜɴᴛᴜᴋ ᴘᴍ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>{PREFIX[0]}setpm (ǫᴜᴇʀʏ) (ᴠᴀʟᴜᴇ)</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴀᴛᴜʀ ᴠᴀʀɪᴀʙᴇʟ ᴛᴇxᴛ_ᴘᴍᴘᴇʀᴍɪᴛ ᴅᴀɴ ʟɪᴍɪᴛ_ᴘᴍ

   <b>•> ǫᴜᴇʀʏ:</b>
       •> <code>PIC</code>
       •> <code>TEXT</code>
       •> <code>LIMIT</code>

       cara aktifin button pmpermit : setpm text kata-kata ~> buttonkata:link
"""


@MIKO.PMPERMIT()
async def _(client, message):
    await pm_anu(client, message)


@MIKO.UBOT("setpm", sudo=True)
@MIKO.TOP_CMD
async def _(client, message):
    await pm_set(client, message)


@MIKO.UBOT("pmpermit", sudo=True)
@MIKO.TOP_CMD
async def _(client, message):
    await pm_on_off(client, message)


@MIKO.INLINE("pm_pr")
async def _(client, message):
    await pm_sh(client, message)


@MIKO.UBOT("ok|setuju")
@MIKO.TOP_CMD
@MIKO.PRIVATE
async def _(client, message):
    await pm_ok(client, message)


@MIKO.UBOT("no|tolak")
@MIKO.TOP_CMD
@MIKO.PRIVATE
async def _(client, message):
    await pm_no(client, message)





