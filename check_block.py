import requests
from discord.ext import tasks
from get_data import f_get_height, f_set_height

def request_json(url:str):
    try:
        return(requests.get(url).json())
    except requests.exceptions.ConnectionError:
        return (None)

async def send_notification_block(bot, block_l):
    role_id = "<@419926802366988292>"
    channel = bot.get_channel(933874035966754946)
    await channel.send(role_id + " | New blocks for solo ERGO !!!")

@tasks.loop(seconds = 10)
async def check_new_block(bot):
    rsp = request_json("https://solo-erg.2miners.com/api/blocks")
    if (rsp == None):
        return (None)
    candidates:list = rsp['candidates']
    for block_l in candidates:
        height:int = int(block_l['height'])
        block_adress:str = block_l['finder']
        if (height > f_get_height() and block_adress == '9fgtyaC2oMUssJCWRS1AcPtSZsxcx1MmvhmySk2QNxA3i3KvCio'):
            f_set_height(height)
            await send_notification_block(bot, block_l)
