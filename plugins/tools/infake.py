import requests
from asyncio import sleep
from pyrogram import Client, filters
#from configs import Config                         # aqui dice que de configs importe lan classe config
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)




@Client.on_message(filters.command(["rndF"], ["/", "."]))
async def rndF(_, m: Message):
    
    rndF = m.text[len("/rndF"):]
    if not rndF:
        await m.reply("Use de /nrdF Usa | /pais")
    
    spli = rndF.split()
    rndF = spli[0]

    rndF_api = requests.get(f'https://randomuser.me/api/?nat={rndF}').json()

#CAPTURAS
#data = rndF_api["data"]
    name = rndF_api["results"][0]["name"]
    gender = rndF_api["results"][0]["gender"]
    age = rndF_api["results"][0]["dob"]["age"]
    birthdate = rndF_api["results"][0]["dob"]["date"]
    street = rndF_api["results"][0]["location"]["street"]['number']
    street1 = rndF_api["results"][0]["location"]["street"]['name']
    city = rndF_api["results"][0]["location"]["city"]
    state = rndF_api["results"][0]["location"]["state"]
    postal = rndF_api["results"][0]["location"]["postcode"]
    email = rndF_api["results"][0]["email"]
    country =rndF_api["results"][0]["location"]["country"]


    edit1 = await m.reply_text("<b>Pene para boos.</b>")
    await sleep(2.5)
    
    await edit1.edit(f"""
<b>

Name : <code>{name["first"]} {name["last"]}</code>
Gender :<code> {gender}</code>
Age :<code> {age}</code>
Birthdate :<code> {birthdate}</code>
Country :<code> {country}</code>
Street :<code> {street}, {street1}</code>
City :<code> {city}</code>
State : <code>{state}</code>
Postal Code :<code> {postal}</code>
Email :<code> {email}</code></b>
</b>
""")


#####PAISES DISPONIBLES
@Client.on_message(filters.command(["pais"], ["/", "."]))
async def countrys(_, m: Message):
    
    
   
    await m.reply(f"""

<code>/rndF AU </code>AUSTRALIA 
<code>/rndF BR </code>BRASIL
<code>/rndF CA </code> CANADA
<code>/rndF CH </code>SUIZA 
<code>/rndF DE </code>ALEMANIA (GERMANY)
<code>/rndF DK </code>DINAMARCA 
<code>/rndF ES </code>ESPAÑA (SPAIN)
<code>/rndF FI </code>FINDLANDIA
<code>/rndF FR </code>FRANCIA 
<code>/rndF GB </code>REINO UNIDO 
<code>/rndF IE </code> IRLANDA
<code>/rndF IN </code> INDIA
<code>/rndF IR </code> IRAN
<code>/rndF MX </code>MEXICO 
<code>/rndF NL </code>NETHERLANDS
<code>/rndF NO </code>NORWAY
<code>/rndF NZ </code>HAMILTON
<code>/rndF RS </code>SERVIA
<code>/rndF TR </code>TURQUIA
<code>/rndF UA </code>UKRANIA
<code>/rndF US </code>ESTADOS UNIDOS

    """)
    