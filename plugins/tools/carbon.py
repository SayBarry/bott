from pyrogram import filters
from aiohttp import ClientSession
from pyrogram import Client as bot
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from io import BytesIO

#from PIL import Image
from pyrogram.types import Message

aiohttpsession = ClientSession()

async def make_carbon(code):
    url = "https://carbonara.vercel.app/api/cook"
    async with aiohttpsession.post(url, json={"code": code}) as resp:
        image = BytesIO(await resp.read())
    image.name = "carbon.png"
    return image


@bot.on_message(filters.command("code"))
async def carbon_func(_, message):
    if not message.reply_to_message:
        return await message.reply_text(
            "solo se usa en un text."
        )
    if not message.reply_to_message.text:
        return await message.reply_text(
            "solo se usa en un text."
        )
    user_id = message.from_user.id
    m = await message.reply_text("<b>⎚ `Pasando a Img...`</b>")
    carbon = await make_carbon(message.reply_to_message.text)
    await m.edit("`Pasando a Img...`..")
    await message.reply_photo(
        photo=carbon,
        caption="""<b>⎚ Create <b><a href="tg://resolve?domain=Daniels_1906">Light!</a></b></b>""",
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton("C R E A D O R", url="https://t.me/Daniels_1906")]]),                   
    )
    await m.delete()
    carbon.close()