def parse_error_msg(message: str):
	if 'Thank you for your order.' in message:
		return {'status': 'success', 'message': 'Thank you for your order.'}
	elif 'Thank You' in message:
		return {'status': 'success', 'message': 'Thank You'}
	else:
		return message




def getTypeCard_Chase(card: str):
	if card[0] == '4':
		return "Visa"
	elif card[0] == '5':
		return "MasterCard"
	elif card[0] == '3':
		return "American Express"
	elif card[0] == '6':
		return "Discover"
	else:
		return "Unknown"

