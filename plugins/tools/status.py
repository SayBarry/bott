import requests 
from pyrogram import Client, filters
import time
from psutil import cpu_percent, virtual_memory, disk_usage, boot_time

bot_uptime = int(time.time())
from platform import python_version

def get_readable_time(seconds: int) -> str:
    count = 0
    ping_time = ""
    time_list = []
    time_suffix_list = ["s", "m", "h", "days"]
    while count < 4:
        count += 1
        if count < 3:
            remainder, obtained = divmod(seconds, 60)
        else:
            remainder, obtained = divmod(seconds, 24)
        if seconds == 0 and remainder == 0:
            break
        time_list.append(int(obtained))
        seconds = int(remainder)
    for i in range(len(time_list)):
        time_list[i] = str(time_list[i]) + time_suffix_list[i]
    if len(time_list) == 4:
        ping_time += time_list.pop() + ", "
    time_list.reverse()
    ping_time += ":".join(time_list)
    return ping_time

from pyrogram import filters, __version__
#Uptime
@Client.on_message(filters.command("pc"))
async def status(client, message):
    ram = virtual_memory().percent
    
    cpu = cpu_percent()
    
    disk = disk_usage("/").percent

    infopc= f"""<b>
Estado de mi pc

Fecha : `{get_readable_time((bot_uptime))}`
Cpu : {cpu}%
RAM:`{ram}%`
Disk:`{disk}%`
Python Version:`{python_version}`
Library:`Pyrogram`
Pyrogram Version:`{__version__}`" 
    </b>"""
    
    await message.reply_text(infopc)