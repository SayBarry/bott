import time


from pyrogram import Client, filters
from pyrogram.types import Message
from pulpos.plantillas import _start 
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

@Client.on_message(filters.command("tiempo", ["/", "."]))
async def start(client, message):
    message_counts = {}

    # Umbral máximo de mensajes permitidos para cada usuario
    MAX_MESSAGES = 3

    # Función para manejar el comando /start
    def start(update, context):
        context.bot.send_message(chat_id=update.effective_chat.id, text="Hola! Soy un bot anti-spam. Envíame un mensaje y asegúrate de no ser un spammer.")

    # Función para manejar los mensajes que no son comandos
    def echo(update, context):
        # Obtiene el ID del usuario que envió el mensaje
        user_id = update.message.from_user.id
        
        # Verifica si el usuario ha enviado demasiados mensajes recientemente
        if user_id in message_counts and message_counts[user_id] >= MAX_MESSAGES:
            # Si el usuario ha enviado demasiados mensajes, envía un mensaje de error
            update.message.reply_text("Lo siento, parece que estás enviando mensajes spam.")
        else:
            # Si el usuario no ha enviado demasiados mensajes, aumenta el contador y procesa el mensaje
            if user_id not in message_counts:
                message_counts[user_id] = 1
            else:
                message_counts[user_id] += 1
            
            message_text = update.message.text
            update.message.reply_text("¡Gracias por tu mensaje!")

    # Función para reiniciar el contador de mensajes
    def reset_counter(update, context):
        # Reinicia el contador de mensajes para todos los usuarios
        message_counts.clear()
        update.message.reply_text("El contador de mensajes ha sido reiniciado.")

    # Crea un objeto Updater con el token del bot

    # Crea un objeto Dispatcher para el Updater
 