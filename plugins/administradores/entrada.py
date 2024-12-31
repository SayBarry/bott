from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# ... your code ...

@Client.on_message(filters.new_chat_members)
async def entrar(Client, message):
         gif_url = "https://i.gifer.com/3OnUr.gif"  # Replace with the actual GIF URL
         await message.reply_text(f"""<b>
         ও Bienvenido bb {message.from_user.first_name}

         ও Mi Creador es      <a href="tg://resolve?domain=@Barry_op">B A R R Y</a>
         ও Puedes usarme escribe <code>/start</code>

         </b>""", parse_mode="html", disable_web_page_preview=True, reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("Gif", url=gif_url)]]))
     
     # ... rest of your code ...
     