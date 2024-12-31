from pyrogram import Client, filters, enums
from pyrogram.types import *
from configss._def_main_ import *
from rank import get_user_rank

USERS_FILE = 'plugins/usuarios/users.txt'  # Archivo para guardar usuarios registrados
PREMIUM_FILE_PATH = "plugins/usuarios/creditos.txt"

def es_usuario_registrado(usuario_id):
    """Comprueba si un usuario está registrado en users.txt."""
    with open(USERS_FILE, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            if str(usuario_id) == linea.strip():
                return True
    return False

@Client.on_message(filters.command("me", ["/", "."]))
async def verificar_credito(client, message):
    user_id = message.from_user.id

    if not es_usuario_registrado(user_id):
        return await message.reply_text("No estás registrado, por favor, regístrate.")

    # Usuario registrado, continuar con la lógica del comando
    with open(PREMIUM_FILE_PATH, "r", encoding='utf-8') as premium_file:
        premium_users = premium_file.readlines()
        found = False
        creditos = 0
        for line in premium_users:
            if f"{user_id}|" in line:
                creditos = int(line.split("|")[1])
                found = True
                break

        rank = get_user_rank(user_id)

        if found:
            await message.reply(f"""<b>Kisuri Chk / User Data. 🔎
━━━━━━━━━━━━━━━
<a href='https://t.me/KirisuChkRef'>[⌘] </a> User Info:
Usuario: {message.from_user.first_name} </code> 
Id: {user_id}</code> 
━━━━━━━━━━━━━━━
<a href='https://t.me/KirisuChkRef'>[⌘] </a> Plan Data:
Plan: {rank} </code> 
Créditos: {creditos}
━━━━━━━━━━━━━━ 
dev by @Daniels_1906
""")
        else:
            await message.reply(f"""<b>Kisuri Chk / User Data. 🔎
━━━━━━━━━━━━━━━
<a href='https://t.me/KirisuChkRef'>[⌘] </a> User Info:
Usuario: {message.from_user.first_name} </code> 
Id: {user_id}</code> 
━━━━━━━━━━━━━━━
<a href='https://t.me/KirisuChkRef'>[⌘] </a> Plan Data:
Plan:  No plan contrated </code> 
Créditos: 0
━━━━━━━━━━━━━━ 
dev by @Daniels_1906
""")