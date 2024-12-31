from pyrogram import Client, filters
from pyrogram.types import Message
from datetime import datetime, timedelta
from random import randint

# ... (resto del código)

@Client.on_message(filters.command(["canjear"], ["/", "."]))
async def canjear_key(client: Client, message: Message):
    if len(message.command) < 2:
        await message.reply_text("<b>Usa el comando <code>/canjear key</code></b>")
        return

    key_ingresada = message.command[1]
    user_id = str(message.from_user.id)
    user_name = message.from_user.first_name or ""  # Obtener el nombre del usuario

    with open(file='plugins/usuarios/keys.txt', mode='r', encoding='utf-8') as keys_archivo:
        llaves = keys_archivo.readlines()
    
    encontrada = False
    for i, linea in enumerate(llaves):
        key_info = linea.strip().split("|")
        if key_info[0] == key_ingresada:
            encontrada = True
            if key_info[1] == "Disponible":  # Verificar si la key está disponible
                fecha_vencimiento = key_info[2]
                rank = key_info[3]

                # Verificar si la key está vencida
                fecha_vencimiento_dt = datetime.strptime(fecha_vencimiento, "%Y-%m-%d")
                if fecha_vencimiento_dt < datetime.now():
                    await message.reply_text("Lo siento, esta Key ha expirado.")
                    return

                # Otorgar acceso premium (reemplaza con tu lógica)
                # ... 

                # Actualizar la key en el archivo (marcar como usada y con el ID y nombre del usuario)
                llaves[i] = f"{key_ingresada}|{user_id}|{fecha_vencimiento}|{rank}|{user_name}\n"
                with open(file='plugins/usuarios/keys.txt', mode='w', encoding='utf-8') as keys_archivo:
                    keys_archivo.writelines(llaves)

                # Registrar la key canjeada en 'plugins/usuarios/canjeadas.txt'
                with open(file='plugins/usuarios/premium.txt', mode='a', encoding='utf-8') as canjeadas_archivo:
                    canjeadas_archivo.write(f"Key: {key_ingresada} - ID Usuario: {user_id} - Nombre: {user_name}\n")

                await message.reply_text(f"¡Felicidades! Has canjeado la key correctamente Tu rango ahora es: {rank}")
                return 
            else:
                await message.reply_text("Esta Key ya ha sido canjeada por otro usuario.")
                return

    if not encontrada:
        await message.reply_text("Key inválida.")