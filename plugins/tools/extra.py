import os
import requests
import random
import time
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup

USER_DATA_FILE = "plugins/usuarios/users.txt" 

@Client.on_message(filters.command("ext", ["/", "."]) & filters.user(USER_DATA_FILE)) 
async def extra_command(client: Client, message: Message):
    inicio = time.time()
    ID = message.from_user.id
    FIRST = message.from_user.first_name

    if message.reply_to_message:
        user_id = message.reply_to_message.from_user.id
        username = message.reply_to_message.from_user.username
    else:
        user_id = message.from_user.id
        username = message.from_user.username

    # Extract the card number from the message (assuming it's in the format "/extra [card number]")
    args = message.text.split(None, 1)
    if len(args) < 2:
        return await message.reply("<b>⎚ Usar <code>/extra [card number]</code> con al menos 6 dígitos.</b>")

    card_number = args[1].strip()

    # Check if the card number has at least 6 digits
    if len(card_number) < 6:
        return await message.reply("<b>⎚ Usar <code>/extra [card number]</code> con al menos 6 dígitos.</b>")

    # Extract the BIN from the card number
    BIN = card_number[:6]

    # Generate random values for CCF, CCP, and CVV
    ccf = str(random.randint(111111, 999999)).zfill(2)
    ccp = str(random.randint(111111, 999999)).zfill(2)

    mes = str(random.randint(1, 12)).zfill(2)
    
    cvv = str(random.randint(111, 999)).zfill(2)

    # Generate the formatted response string
    response_text = f"{BIN}{card_number[6:]}|{mes}|{ccf}|{cvv}"
    
    await message.reply(response_text, disable_web_page_preview=True)

    fin = time.time()
    tiempo = round(fin - inicio, 2)
    await message.reply(f"<b>Tiempo de respuesta: {tiempo} segundos</b>")

# ... rest of your code ...