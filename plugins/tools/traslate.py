from pyrogram import Client, filters
from googletrans import Translator

@Client.on_message(filters.command("tra"))
async def cmds(client, message):
    with open(file='plugins/usuarios/users.txt',mode='r+',encoding='utf-8') as archivo:
        x = archivo.readlines()
        if str(message.from_user.id) + '\n' in x:
            translator = Translator()
            translator.translate('안녕하세요.')
            print(translator)

