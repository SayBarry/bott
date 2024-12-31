def get_user_rank(user_id):
    # Lee los archivos admins.txt, admins1.txt y Owner.txt
    with open('plugins/usuarios/premium.txt', 'r') as f:
        Premium = f.read().splitlines()
    with open('plugins/usuarios/dev.txt', 'r') as f:
        Dev = f.read().splitlines()
    with open('plugins/usuarios/seller.txt', 'r') as f:
        sellers = f.read().splitlines()
    with open('plugins/usuarios/users.txt', 'r') as f:
        Free = f.read().splitlines()
    with open('plugins/usuarios/admins.txt', 'r') as f:
        owner = f.read().splitlines()
   
    if str(user_id) in owner:
        return 'owner'
    elif str(user_id) in sellers:
        return 'SELLER'
    elif str(user_id) in Premium:
        return 'Premium'
    elif str(user_id) in Free:
        return 'Free User'
    if str(user_id) in Dev:
        return 'Co-funder'

