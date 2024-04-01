from miko import *

__MODULE__ = "invite"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ɪɴᴠɪᴛᴇ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>invite</code> [ᴜsᴇʀɴᴀᴍᴇ] 
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴜɴᴅᴀɴɢ ᴀɴɢɢᴏᴛᴀ ᴋᴇ ɢʀᴜᴘ ᴀɴᴅᴀ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>inviteall</code> [ᴜsᴇʀɴᴀᴍᴇ_ɢʀᴏᴜᴘ - ᴄᴏʟʟᴅᴏᴡɴ=ᴅᴇᴛɪᴋ ᴘᴇʀ ɪɴᴠɪᴛᴇ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴜɴᴅᴀɴɢ ᴀɴɢɢᴏᴛᴀ ᴅᴀʀɪ ᴏʙʀᴏʟᴀɴ ɢʀᴜᴘ ʟᴀɪɴ ᴋᴇ ᴏʙʀᴏʟᴀɴ ɢʀᴜᴘ ᴀɴᴅᴀ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>cancel</code>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍʙᴀᴛᴀʟᴋᴀɴ ᴘᴇʀɪɴᴛᴀʜ ɪɴᴠɪᴛᴇᴀʟʟ
  """


@MIKO.UBOT("invite", sudo=True)
@MIKO.GROUP
@MIKO.TOP_CMD
async def _(client, message):
    await invite_cmd(client, message)


@MIKO.UBOT("inviteall", sudo=True)
@MIKO.GROUP
@MIKO.TOP_CMD
async def _(client, message):
    await inviteall_cmd(client, message)


@MIKO.UBOT("cancel", sudo=True)
@MIKO.GROUP
@MIKO.TOP_CMD
async def _(client, message):
    await cancel_cmd(client, message)
