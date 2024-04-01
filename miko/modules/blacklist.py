from miko import *

__MODULE__ = "blacklist"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ʙʟᴀᴄᴋʟɪsᴛ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>addbl</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍᴀsᴜᴋᴋᴀɴ ɢʀᴏᴜᴘ ᴋᴇ ᴅᴀꜰᴛᴀʀ ʜɪᴛᴀᴍ sᴜᴘᴀʏᴀ ɢᴄᴀsᴛ ᴋᴀʟɪᴀɴ ᴛɪᴅᴀᴋ ᴍᴀsᴜᴋ ᴋᴇ ɢʀᴏᴜᴘ [ʟᴀᴋᴜᴋᴀɴ ᴅɪ ɢʀᴏᴜᴘ, sᴇʟᴀɪɴ ᴅɪ ɢʀᴏᴜᴘ ʙᴏᴛ ᴛɪᴅᴀᴋ ᴀᴋᴀɴ ʀᴇsᴘᴏɴ]

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>unbl</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢʜᴀᴘᴜs ɢʀᴏᴜᴘ ᴅᴀʀɪ ᴅᴀꜰᴛᴀʀ ʜɪᴛᴀᴍ ᴀɢᴀʀ ɢᴄᴀsᴛ ʙɪsᴀ ᴍᴀsᴜᴋ ᴋᴇ ɢʀᴏᴜᴘ  [ʟᴀᴋᴜᴋᴀɴ ᴅɪ ɢʀᴏᴜᴘ, sᴇʟᴀɪɴ ᴅɪ ɢʀᴏᴜᴘ ʙᴏᴛ ᴛɪᴅᴀᴋ ᴀᴋᴀɴ ʀᴇsᴘᴏɴ]
  
  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>rallbl</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢʜᴀᴘᴜs sᴇᴍᴜᴀ ʙʟᴀᴄᴋʟɪsᴛ
  
  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>listbl</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍᴇʀɪᴋsᴀ ᴅᴀꜰᴛᴀʀ ʙʟᴀᴄᴋʟɪsᴛ ɢʀᴏᴜᴘ
"""


@MIKO.UBOT("addbl", sudo=True)
@MIKO.GROUP
@MIKO.TOP_CMD
async def _(client, message):
    await add_blaclist(client, message)


@MIKO.UBOT("unbl", sudo=True)
@MIKO.GROUP
@MIKO.TOP_CMD
async def _(client, message):
    await del_blacklist(client, message)


@MIKO.UBOT("rallbl", sudo=True)
@MIKO.TOP_CMD
async def _(client, message):
    await rem_all_blacklist(client, message)


@MIKO.UBOT("listbl", sudo=True)
@MIKO.TOP_CMD
async def _(client, message):
    await get_blacklist(client, message)
