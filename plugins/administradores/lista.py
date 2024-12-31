from pyrogram import Client, filters 

GIF_LISTA = "https://i.gifer.com/3OnOx.gif"  # Reemplaza con la URL de tu GIF

@Client.on_message(filters.command("lista")) 
async def start(client, message): 
    with open('plugins/usuarios/users.txt', 'r') as f: 
        Free = f.read().splitlines() 
    with open('plugins/usuarios/admins.txt', 'r') as f: 
        owner = f.read().splitlines() 
     
    Free = len(Free) 
    owner = len(owner) 
     
    await client.send_animation(
        chat_id=message.chat.id,
        animation=GIF_LISTA,
        caption=f"""<b> LISTA DE USUARIOS REGISTRADOS!!
<a href='https://t.me/Barry_op'>♰</a> usuarios Registrados <code>{Free}</code>  
</b>""",
    ) 