

from miko import *

__MODULE__ = "Afk"
__HELP__ = """
Bantuan Untuk Afk

• Perintah: <code>{0}afk</code> [reason]
• Penjelasan: Untuk mengaktifkan mode afk.
"""


@PY.miko("afk")
async def _(client, message):
    await set_afk(client, message)
    
    
@miko.on_message(
    is_afk
    & (filters.mentioned | filters.private)
    & ~filters.me
    & ~filters.bot
    & filters.incoming
)
async def _(client, message):
    await afk_er(client, message)
    
    
@miko.on_message(filters.outgoing & filters.me & is_afk)
async def _(client, message):
    await no_afke(client, message)
