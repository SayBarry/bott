from rank import get_user_rank
from pyrogram import Client, filters
import asyncio
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

_start = """<b><a href="tg://resolve?domain=PlutonRexBot">𝗣𝗹𝘂𝘁𝗼𝗻 🐦‍🔥</a>          <code>{hora}</code>

Fecha De Hoy: <code>{tiempo}</code> 
Estado   <code> {estado}</code>
ID   <code> {user_id} [{rank}]</code> 
Version Del Bot   1.1
━━━━━━━━━━━━━
</b>
"""

_cmd = """<a href='https://t.me/Mwellawaitt'>Bienvenidos a PlutonRexBot </a>
━━━━━━━━━━━━━
⎚ GaterWays                   0
⎚ status                          ON ✅
━━━━━━━━━
⎚Tools                             5
⎚ status                          ON ✅
━━━━━━━━━
━━━━━━━━━━━━━
Dev By: @Mwellawaitt"""

@Client.on_message(filters.command(["cmds"], ["/", "."]))
async def cmds(client, message):
    with open(file='plugins/usuarios/users.txt', mode='r+', encoding='utf-8') as archivo:
        x = archivo.readlines()
        if str(message.from_user.id) + '\n' in x:
            # Botones Inline
            botones = InlineKeyboardMarkup([
                [InlineKeyboardButton("Gates", callback_data="gates")],
                [InlineKeyboardButton("Tools", callback_data="tools")]
                # Agrega más botones aquí si lo necesitas
            ])
            
            await client.send_animation(
                chat_id=message.chat.id,
                animation="https://i.gifer.com/3OnPC.gif", 
                caption=_cmd,
                reply_markup=botones  # Agrega los botones aquí
            )
        else:
            return await message.reply(f'<b>No estas Registrado, Registrese <code>/register</code></b>')


_Call_Gateways = """<b> <b><a href="tg://resolve?domain=">Gates | Gateway 🌑</a></b>

⎚ Chill | Stripe Charge <code>[FREE]</code>
⎚ Usar <code>/str card</code> On [ ✅ ]
━━━━━━━━━
⎚ Pluton | Stripe Auth <code>[FREE]</code>
⎚ Usar <code>/xi card</code> On [ ✅ ]
━━━━━━━━━
⎚ Mass - <code>PREMIUM</code>
⎚ Usar <code>/mass cards</code>
━━━━━━━━━
⎚ Alga | Stripe Auth <code>[PREMIUM]</code>
⎚ Usar <code>/cr card</code> On [ ✅ ]
━━━━━━━━━
</b>"""

_Call_Tools = """<b><b> <b><a href="tg://resolve?domain=">Herramientas | Tools 🌑</a></b>

⎚ Bin - <code>FREE</code>
⎚ Usar <code>/bin 456789</code>
━━━━━━━━━
⎚ Gen Ccs - <code>FREE</code>
⎚ Usar <code>/gen 456789|rnd|rdn|rdn</code> 
━━━━━━━━━
⎚ Gen Mass Ccs <code>FREE</code>
⎚ Usar <code>/genmass 456789|rnd|rnd|rnd</code>
━━━━━━━━━
⎚ Ip - <code>FREE</code>
⎚ Usar <code>/ip 1.1.1.1</code>
━━━━━━━━━
⎚ Rand - <code>FREE</code>
⎚ Usar <code>/rand </code> 
━━━━━━━━━
⎚ Rand Pais - <code>PREMIUM</code>
⎚ Usar <code>/rdn ar</code>
━━━━━━━━━
⎚ Zip code Postal - <code>FREE</code>
⎚ Usar <code>/zip 10020</code>
━━━━━━━━━
</b>"""

_Call_Gateways_buttons = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    "Atras ",
                    callback_data="home"
                ),
                InlineKeyboardButton(
                    "Cerrar",
                    callback_data="exit"
                ),
        ]
        ]
    )
