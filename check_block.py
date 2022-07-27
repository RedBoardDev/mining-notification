
from time import sleep
import requests
from discord.ext import tasks
from get_data import f_get_height, f_set_height
from lib_discord import send_notification_block

def request_json(url:str):
    try:
        return(requests.get(url).json())
    except requests.exceptions.ConnectionError:
        return (None)

@tasks.loop(seconds = 30)
async def check_new_block(bot):
    rsp = request_json("https://ergo-stratum.jjpool.fr/api/pools/ergo1/blocks")
    if (rsp == None):
        return (None)
    last_block = rsp[0]
    if (last_block['blockHeight'] != f_get_height()):
        f_set_height(last_block['blockHeight'])
        sleep(20)
        await send_notification_block(bot, last_block)
