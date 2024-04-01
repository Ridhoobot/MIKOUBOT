from miko import *

__MODULE__ = "control"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴄᴏɴᴛʀᴏʟ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>setprefix</code> [sɪᴍʙᴏʟ ᴘʀᴇғɪx]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇɴɢᴜʙᴀʜ ᴘʀᴇғɪx/ʜᴀɴᴅʟᴇʀ ᴄᴏᴍᴍᴀɴᴅ

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>setemoji</code> [ǫᴜᴇʀʏ] [ᴠᴀʟᴇᴜ]
  <b>• ǫᴜᴇʀʏ: </b>
       <b>•> <code>pong</code> </b>
       <b>•> <code>userbot</code> </b>
       <b>•> <code>mention</code> </b>
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ: ᴜɴᴛᴜᴋ ᴍᴇʀᴜʙᴀʜ ᴛᴀᴍᴘɪʟᴀɴ ᴘᴀᴅᴀ ᴘɪɴɢ</b>

"""



@MIKO.UBOT("setprefix", sudo=True)
@MIKO.TOP_CMD
async def _(client, message):
    await setprefix(client, message)

@MIKO.UBOT("setemoji", sudo=True)
@MIKO.TOP_CMD
async def _(client, message):
    await change_emot(client, message)

