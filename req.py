import requests

headers = {
    'authority': 'api.stripe.com',
    'accept': 'application/json',
    'accept-language': 'es-ES,es;q=0.9',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://js.stripe.com',
    'referer': 'https://js.stripe.com/',
    'sec-ch-ua': '"Google Chrome";v="111", "Not(A:Brand";v="8", "Chromium";v="111"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36',
}

data = 'type=card&billing_details[name]=ewfwrfw+rweerwrw&billing_details[email]=ewrwrewrwerewrew3%40gmail.com&billing_details[address][line1]=stree+456&billing_details[address][line2]=&billing_details[address][city]=california&billing_details[address][state]=CA&billing_details[address][postal_code]=10080&billing_details[address][country]=US&card[number]=4189410000356705&card[cvc]=535&card[exp_month]=05&card[exp_year]=25&guid=1ae2c337-d23e-4968-ba44-cf67f6c46ba8a11185&muid=2f4f8f4c-25f4-4eba-8d5b-65c1e252034cfafc2c&sid=418bf4d5-1606-4532-b60f-3dac3ad0b36e978b76&payment_user_agent=stripe.js%2F94106e1ba1%3B+stripe-js-v3%2F94106e1ba1&time_on_page=105742&key=pk_live_SMtnnvlq4TpJelMdklNha8iD&_stripe_account=acct_1EXtuiBzOyZjK1DY'

response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
print(response.text)