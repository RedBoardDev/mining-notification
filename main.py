import discord
from dotenv import load_dotenv
from get_data import set_var_dotenv
from check_block import check_new_block

#========================== INITIALIZE VARIABLE ==========================#
bot = discord.Client()
#========================== MAIN ==========================#

load_dotenv(override = True)
TOKEN = set_var_dotenv("DISCORD_TOKEN")
@bot.event
async def on_ready():
    if not check_new_block.is_running():
        check_new_block.start(bot)
bot.run(TOKEN)
