
from miko import *

__MODULE__ = "Reminders"
__HELP__ = """
Modul ini memungkinkan pengguna untuk mengatur pengingat.

• Perintah: `{0}remind`
• Penjelasan: Mengatur pengingat untuk waktu tertentu di masa depan.

Penggunaan: `{0}remind <waktu> <pesan>`
Contoh:
`{0}remind 1j30m waktu sholat`

`{0}remind 1h30m ke pasar`

Catatan: Argumen waktu mendukung berbagai format seperti jam (j), menit (m), dan hari (h).

• Perintah: `{0}listremind`
• Penjelasan: Menampilkan daftar pengingat yang tersimpan.

Penggunaan: `{0}listremind`
Untuk mengatur pengingat, gunakan perintah `{0}remind` diikuti oleh waktu dan pesan yang diinginkan. Argumen waktu harus disediakan dalam format yang disebutkan di atas. Pengingat akan dikirim pada waktu yang ditentukan dengan pesan yang diberikan.

Untuk melihat daftar pengingat yang tersimpan, gunakan perintah `{0}listremind`.
"""


@MIKO.UBOT("remind", sudo=True)
async def _(client, message):
    await reminder(client, message)


@MIKO.UBOT("listremind", sudo=True)
async def _(client, message):
    await listrem(client, message)
