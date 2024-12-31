from configss._def_main_ import *

premium_users = set()

with open('plugins/usuarios/premium.txt', 'r') as file:
    for line in file:
        premium_users.add(line.strip())

@Client.on_message(filters.command(["gen"], ["/", "."]))
async def gen(client, message):

    if message.from_user.id not in premium_users:
        return await message.reply("<b>No has comprado una membresía premium para usar este comando</b>")

    input = re.findall(r'[0-9]+', message.text)
    rank = get_user_rank(message.from_user.id)
    
    BIN = message.text[len("/bin"): 11]
    if len(BIN) < 6:
        return await message.reply("<b>Usar <code>/gen 456789|rnd|rdn|rdn</code></b>")
    if not BIN:
        return await message.reply("<b>Usar <code>/gen 456789|rnd|rdn|rdn</code></b>")
    
    inputms = message.text.split(None, 1)[1]
    bincode = 6
    BINS = inputms[:bincode]
    req = requests.get(f"https://bins.antipublic.cc/bins/{BINS}").json()
    brand = req['brand']
    country = req['country']
    country_name = req['country_name']
    country_flag = req['country_flag']
    country_currencies = req['country_currencies']
    bank = req['bank']
    level = req['level']
    typea = req['type']
    
    tiempoinicio = time.perf_counter()
    
    if len(input) == 1:
        cc = input[0]
        mes = 'x'
        ano = 'x'
        cvv = 'x'
    elif len(input) == 2:
        cc = input[0]
        mes = input[1]
        ano = 'x'
        cvv = 'x'
    elif len(input) == 3:
        cc = input[0]
        mes = input[1]
        ano = input[2]
        cvv = 'x'
    elif len(input) == 4:
        cc = input[0]
        mes = input[1]
        ano = input[2]
        cvv = input[3]
    else:
        cc = input[0]
        mes = input[1]
        ano = input[2]
        cvv = input[3]

    cc1, cc2, cc3, cc4, cc5, cc6, cc7, cc8, cc9, cc10 = cc_gen(cc, mes, ano, cvv)
    
    tiempofinal = time.perf_counter()
    text = f"""
    <b>Plutón 〻 ➼ 𝐶𝐶 𝐺𝑒𝑛
    ━━━━━━━━
    <code>{cc1}</code>
    <code>{cc2}</code>
    <code>{cc3}</code>
    <code>{cc4}</code>
    <code>{cc5}</code>
    <code>{cc6}</code>
    <code>{cc7}</code>
    <code>{cc8}</code>
    <code>{cc9}</code>
    <code>{cc10}</code>
    ━━━━━━━━
    𝘽𝙞𝙣: <code>{BINS}</code>
    𝙄𝙣𝙛𝙤: {brand} - {typea} - {level}
    𝘽𝙖𝙣𝙠: <code>{bank}{country_flag}</code>
    𝙂𝙚𝙣 𝙗𝙮: <code>@{message.from_user.username}</code> [{rank}]</b>"""
    
    await client.send_message(message.chat.id, f'{text}', reply_markup=InlineKeyboardMarkup(
        [[
            InlineKeyboardButton("𝗥𝗘-𝗚𝗘𝗡", callback_data="gen_pro")
        ]]
    ))