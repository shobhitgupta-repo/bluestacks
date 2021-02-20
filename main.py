# import modules
import discord
import os
from dotenv import load_dotenv

#load env file
load_dotenv()

# Fetch discord token from env file
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# initialize discord client
bot = discord.Client()

#Event listener for bot online status
@bot.event
async def on_ready():
    guild_count = 0

    for guild in bot.guilds:
        print(guild.id, "name",guild.name)
        guild_count+=1
    print("bot in ",str(guild_count),guilds)

#Event listner for any new message
@bot.event
async def on_message(message):
    if(message.content=="hello"):
        await message.channel.send("hi")

bot.run(DISCORD_TOKEN)
