from pyrogram import Client, filters, enums
from pyrogram.types import *
from configss._def_main_ import *
from rank import *
import random

PREMIUM_FILE_PATH = "plugins/usuarios/creditos.txt"

@Client.on_message(filters.command(["creditos"], ["/", "."]))
async def add_credit(client, message):
    with open(file='plugins/usuarios/admins.txt', mode='r+', encoding='utf-8') as archivo:
        x = archivo.readlines()
        if str(message.from_user.id) + '\n' in x:
            try:
                user_id = int(message.text.split()[1])
                creditos = int(message.text.split()[2])
                if 0 <= creditos <= 999999999:
                    with open(PREMIUM_FILE_PATH, 'r+', encoding='utf-8') as f:
                        lines = f.readlines()
                        found = False
                        for i, line in enumerate(lines):
                            if f"{user_id}|" in line:
                                old_creditos = int(line.split("|")[1])
                                lines[i] = f"{user_id}|{old_creditos + creditos}\n"
                                found = True
                                break
                        if not found:
                            lines.append(f"{user_id}|{creditos}\n")
                        f.seek(0)
                        f.writelines(lines)
                    await message.reply_text(f"Se han añadido {creditos} créditos al usuario con ID {user_id}.")
                else:
                    await message.reply_text("<b>Error: Los créditos deben estar entre 0 y 9999999.</b>")
            except (IndexError, ValueError):
                await message.reply_text("<b>Uso incorrecto: /creditos ID usuario creditos </b>")
        else:
            await message.reply_text("<b>Este comando es solo para admins.</b>")