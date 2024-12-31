import requests

from asyncio import sleep
from pyrogram import Client, filters
#from configs import Config                         # aqui dice que de configs importe lan classe config
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)


@Client.on_message(filters.command(["sk"], ["/", "."]))
async def sk(_, m: Message):

    skkey = m.text[len('/sk '):]
    if not skkey:
        return await m.reply(
            f"""
            <b>Ingresar correctamente el valor</b>: <code>/sk sk_live_51Gnxxxxxxxxxxxxxxxxxxxxxxxxxxhrh8</code>

            """)

    edit1 = await m.reply_text("<b>♳ Checkando SK...</b>")
    await sleep(1.5)

    cc = "4543218722787334"
    cvc = "780"
    mes = "07"
    ano = "2026"

    headers = {
        "Content-Type": "application/x-www-form-urlencoded"
    }

    data = {
        "card[number]": cc,
        "card[cvc]": cvc,
        "card[exp_month]": mes,
        "card[exp_year]": ano
    }

    pos = requests.post(f"https://api.stripe.com/v1/tokens",
                        data=data, headers=headers, auth=(skkey, ""))
    if 'Invalid API Key provided' in pos.text:
        await m.reply(f"""

<b>DEAD ❌

{skkey}

        """)
    elif 'api_key_expired' in pos.text:
        await edit1.edit(f"""


<b>DEAD ❌

{skkey}
""")
    elif 'testmode_charges_only' in pos.text:
        await edit1.edit(f"""

<b>DEAD ❌

{skkey}

""")
    elif 'test_mode_live_card' in pos.text:
        await edit1.edit(f"""

<b>DEAD ❌

{skkey}

""")
    else:
        await edit1.edit(f"""
<b>LIVE ✅</b>

<code><b>{skkey}</b></code>

<b>Reason: Sk Live!</b>
""")