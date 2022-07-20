import os
from dotenv import load_dotenv
import discord
from check_block import check_new_block

#========================== INITIALIZE VARIABLE ==========================#
bot = discord.Client()

#========================== MAIN ==========================#

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
@bot.event
async def on_ready():
    if not check_new_block.is_running():
        check_new_block.start(bot)
bot.run(TOKEN)
