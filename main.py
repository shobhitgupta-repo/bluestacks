# import modules
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import re
import gsearch
from helpers import predicate,formatMessage,printList

#load env file
load_dotenv()

# Fetch discord token from env file
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

# initialize discord client
bot = commands.Bot(command_prefix="!")

#Event listener for bot online status
@bot.event
async def on_ready():
    print("bot is ready")

#Event listner for any new message
@bot.event
async def on_message(message):
    #reply hey to hi
    if(message.content=="hi"):
        await message.channel.send("hey")

    await bot.process_commands(message)

#commands for processing
#"!google query" to fetch google results
@bot.command(name="google")
async def search(ctx,*,query:str):
    gobj=gsearch.GoogleSearch(query)
    results=gobj.search()
    for link in results:
        await ctx.channel.send(link)


#"!recent query" fetch google search history
@bot.command(name="recent")
async def history(ctx,*,word:str):
    messages = await ctx.channel.history(limit=2000).filter(predicate).flatten()
    response = []
    for msg in messages:
        if (word in msg.content):
            response.append(formatMessage(msg.content))
    #REMOVE DUPLICATES and Pretty print the array
    response = printList(list(set(response)))
    await ctx.channel.send(response)

#RUN THE BOT
bot.run(DISCORD_TOKEN)
