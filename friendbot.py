import discord
import asyncio
import random
import math
import time
import calendar
import datetime
import discord.ext.commands as commands


bot = commands.Bot(command_prefix='{')

bot.load_extension("Math")
bot.load_extension("Writing")
bot.load_extension("Utilities")
bot.load_extension("Conversational")
bot.load_extension("Animals")



@bot.command()
async def test(ctx, *arg):
    """for when i hate myself"""
    await ctx.send(str(arg))
    
@bot.command()
async def doc(ctx, *arg):
    """to write down bugs, suggestions, things to make me cry, etc"""
    await ctx.send("Found a bug? Have a suggestion? Want me to hate myself????? Write it here!")
    await ctx.send("https://docs.google.com/document/d/1sMNqlO4PdlO4vdNd9Frkzp0PtYikKn9ZPCeW4NBEq6g/edit?usp=sharing")
    
@bot.command()
async def kill(ctx, *arg):
    """actual murder v bad"""
    await ctx.send(":(")
    await bot.logout()
    
@bot.command()
async def setPlay(ctx, *, arg):
    await bot.change_presence(activity=discord.Game(name=arg))


bot.run("Mzc2MTYxNTk0NTcwMTc4NTYy.DiA2Nw.eS70fGrbdHalt1GOfRWHdEfnnIU")

