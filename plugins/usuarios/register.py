from pyrogram import Client, filters
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

@Client.on_message(filters.command(["register"], ["/", "."]))
async def register(_, m: Message):
    with open(file='plugins/usuarios/users.txt',mode='r+',encoding='utf-8') as archivo:
        x = archivo.readlines()
        if str(m.from_user.id) + '\n' in x:
            return await m.reply(f'<b>⎚ Usuario ya estas registrado.</code></b>')
        else:
            archivo.write('{}\n'.format(m.from_user.id))
            return await m.reply(f'<b>⎚Registro Correct <code>{m.from_user.id} ✅</code></b>')