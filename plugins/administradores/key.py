from pyrogram import Client, filters
from pyrogram.types import Message
from random import randint
from datetime import datetime, timedelta

@Client.on_message(filters.command("key"))
async def generar_key(client: Client, message: Message):
    """
    Genera llaves de acceso premium.

    Uso:
    /key <dias> - Genera una key premium válida por la cantidad de días especificada.
    /key <dias> <cantidad> - Genera la cantidad especificada de keys premium, válidas por la cantidad de días especificada.
    """

    # Verificar si el usuario es administrador
    with open('plugins/usuarios/admins.txt', 'r+', encoding='utf-8') as archivo:
        admins = archivo.readlines()
        if str(message.from_user.id) + '\n' not in admins:
            return await message.reply_text('<b>Este comando es solo para admins.</b>')

    # Obtener argumentos
    args = message.text.split(" ")
    if len(args) < 2 or len(args) > 3:
        return await message.reply_text("<b>Uso: <code>/key diasy cantidad</code></b>")

    try:
        dias = int(args[1])
        cantidad = int(args[2]) if len(args) == 3 else 1  # Cantidad 1 por defecto si no se especifica
    except ValueError:
        return await message.reply_text("<b>Los días y la cantidad deben ser números enteros.</b>")

    # Generar keys
    keys_generadas = []
    for _ in range(cantidad):
        key = f"Pluto-{randint(1000, 9999)}-PREMIUM"
        fecha_vencimiento = (datetime.now() + timedelta(days=dias)).strftime("%Y-%m-%d")

        # Guardar la información de la key
        with open('plugins/usuarios/keys.txt', 'a', encoding='utf-8') as keys_archivo:
            keys_archivo.write(f"{key}|{message.from_user.id}|{fecha_vencimiento}|PREMIUM\n")

        # Agregar la key al formato deseado
        keys_generadas.append(f"<b>Key{key}</b>")

    # Unir las keys con saltos de línea
    keys_texto = "\n".join(keys_generadas)

    # Enviar las keys al usuario
    await message.reply_text(f"""
<b>♡ 𝗞𝗲𝘆𝘀 𝗴𝗲𝗻𝗲𝗿𝗮𝗱𝗮𝘀 ♡
━━━━━◦ ❈ ◦•━━━━━
{keys_texto}
Plan: PREMIUM
Vencimiento:{fecha_vencimiento}
Generadas por:{message.from_user.mention}
━━━━━━◦ ❈ ◦•━━━━━
<b>owner:</b> @@Barry_op
<b>Dev:</b> @Barry_op
""")