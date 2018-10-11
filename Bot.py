import discord
import youtube_dl
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio


bot = commands.Bot(command_prefix='your prefixprefix')



@bot.event
async def on_ready():
    print("Devteam: Successfully Booted Up!")  
    print("Errors: ")
    
    
Bot.run("Token") 
