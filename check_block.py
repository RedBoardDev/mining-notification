from time import time
import requests
from discord.ext import tasks
from get_data import f_get_height, f_set_height

def request_json(url:str):
    try:
        return(requests.get(url).json())
    except requests.exceptions.ConnectionError:
        return (None)

async def send_notification_block(bot):
    role_id = "<@419926802366988292>"
    channel = bot.get_channel(933874035966754946)
    await channel.send(role_id + " | New blocks for solo mining !!!")

@tasks.loop(seconds = 10)
async def check_new_block(bot):
    rsp = request_json("https://minenice.newpool.pw:8201/stats_address?address=GSw7npbaVSrjNCYxuRnEyz8My1cn696HaS&longpoll=false")
    if (rsp == None):
        return (None)
    last_payments = rsp['payments'][0]
    l_last_payments = last_payments.split(':')
    if (l_last_payments[4] != f_get_height()):
        f_set_height(l_last_payments[4])
        await send_notification_block(bot)
