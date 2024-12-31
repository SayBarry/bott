import os
import requests
import random
import time
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

# File paths
USER_DATA_FILE = "plugins/usuarios/users.txt"
ADMINS_FILE = "plugins/usuarios/admins.txt"
CREDITOS_FILE = "plugins/usuarios/creditos.txt" 

@Client.on_message(filters.command("quitar_creditos", ["/", "."]) & filters.user(ADMINS_FILE)) 
async def quitar_creditos_command(client: Client, message: Message):
    args = message.text.split(None, 1)
    if len(args) < 2:
        return await message.reply("<b>⎚ Formato incorrecto. Usar <code>/quitar_creditos [ID de usuario]</code>.</b>")

    user_id = args[1].strip()

    # Read existing credits data
    try:
        with open(CREDITOS_FILE, "r") as f:
            creditos_data = f.readlines()
    except FileNotFoundError:
        creditos_data = []

    # Find the user's credits
    user_found = False
    for line in creditos_data:
        parts = line.strip().split("|")
        if parts[0] == user_id:
            user_found = True
            current_creditos = int(parts[1])
            break

    if not user_found:
        return await message.reply(f"<b>El usuario con ID {user_id} no tiene créditos registrados.</b>")

    # Ask for the amount to remove
    await message.reply(f"<b>⎚ Ingresa la cantidad de créditos a quitar al usuario con ID {user_id} (tiene {current_creditos}).</b>")

    @client.on_message(filters.text & filters.reply_to_message(message.message_id), user_id=message.from_user.id)
    async def handle_amount(client, message):
        try:
            amount = int(message.text)
        except ValueError:
            return await message.reply("<b>Por favor, ingresa un número válido.</b>")

        if amount <= 0:
            return await message.reply("<b>La cantidad de créditos a quitar debe ser mayor que 0.</b>")

        if amount > current_creditos:
            return await message.reply(f"<b>⎚ No puedes quitar más créditos de los que tiene el usuario ({current_creditos}).</b>")

        # Update the user's credits
        new_creditos = current_creditos - amount
        creditos_data = [
            line for line in creditos_data if line.strip().split("|")[0] != user_id
        ]
        creditos_data.append(f"{user_id}|{new_creditos}\n")

        # Write updated credits data
        with open(CREDITOS_FILE, "w") as f:
            f.writelines(creditos_data)

        await message.reply(f"<b>⎚ Se han quitado {amount} créditos al usuario con ID {user_id}. Ahora tiene {new_creditos} créditos.</b>")