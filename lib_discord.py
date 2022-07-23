import discord
from get_data import get_localtime, set_var_dotenv
from message_notification import set_global_message

def set_base_embed(title, description, color):
    embed = discord.Embed(
        title = title,
        color = color,
        description = description
    )
    embed.set_footer(text = "JJPool |",
    icon_url = "https://yt3.ggpht.com/eK3t284KYCD1Vao7x068ZpisxAXZtQxAwlvkZh_Q7Xtn4sJKv3HHBcdIPWeaCRtbnUheQnN-Hw=s900-c-k-c0x00ffffff-no-rj")
    embed.timestamp = get_localtime()
    return (embed)

def set_embed_block(embed, field_name:str, message:str):
    # embed.set_thumbnail(url = "https://c.tenor.com/WpekNE8saNQAAAAi/crazypool-logo-spin.gif")
    embed.add_field(name = field_name, value = message, inline = False)
    return (embed)

async def send_notification_block(bot, last_block) -> None:
    channel = bot.get_channel((int)(set_var_dotenv("CHANNEL_ID")))
    global_stats = set_global_message(last_block)
    reward_stats:str = "Reward: " + (str)(last_block['reward']) + " ERG"
    embed = set_embed_block(set_base_embed("ERGO | New block found !", "", 0x1ABC9C), reward_stats, global_stats)
    await channel.send(embed = embed)
