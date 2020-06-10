import random
import json
import requests
import asyncio
import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = '!') #Sets the command prefix to '!'

@bot.event #Checks if the bot is ready and sets the status to idle
async def on_ready():
    await bot.change_presence(status=discord.Status.online, activity=discord.Game('Type !ferret to receive a picture of a random ferret!'))
    print('Bot is ready.')

@commands.has_permissions(send_messages=True) #Checks if the user has permisions to send messages in the server
@commands.cooldown(1, 15, commands.BucketType.guild) #Puts on a cooldown of 15 seconds on the command

@bot.command() #Gets a random image of a ferret from Polecat's API
async def ferret(ctx):
    response = requests.get("https://polecat.me/api/ferret")
    jsonObjct = json.loads(response.text)
    url = jsonObjct["url"]
    if response.status_code == 200:
        await ctx.send(url)
        print('Successfully linked a ferret!')
    else:
        await ctx.send('Sorry! An error has occured :(')
        
     
bot.run('NzIwMDc2OTMwODI0Nzk4Mjkw.XuBCfQ.uAf0Og43Zpf4fnL6KrgwRAPcLuE')