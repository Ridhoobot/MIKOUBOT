from miko import *

__MODULE__ = "sangmata"
__HELP__ = f"""
<b>『 ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ sᴀɴɢᴍᴀᴛᴀ 』</b>

  <b>• ᴘᴇʀɪɴᴛᴀʜ:</b> <code>sg</code> [ᴜsᴇʀ_ɪᴅ/ʀᴇᴘʟʏ ᴜsᴇʀ]
  <b>• ᴘᴇɴᴊᴇʟᴀsᴀɴ:</b> ᴜɴᴛᴜᴋ ᴍᴇᴍᴇʀɪᴋsᴀ ʜɪsᴛᴏʀɪ ɴᴀᴍᴀ/ᴜsᴇʀɴᴀᴍᴇ
"""


@MIKO.UBOT("sg", sudo=True)
@MIKO.TOP_CMD
async def _(client, message):
    await sg_cmd(client, message)
