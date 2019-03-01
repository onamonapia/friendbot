import discord
import asyncio
import random
import math
import time
import calendar
import datetime
import discord.ext.commands as commands

class Utilities():
    
    def __init__(self, bot):
        self.bot = bot   
        
        
        
    @commands.command()
    async def flipcoin(self, ctx):
        
        """Flips a coin."""
        
        cointoss = random.choice(["Heads", "Tails"])
        await ctx.send(str(cointoss))    
      
    @commands.command()  
    async def shouldi(self, ctx, *, arg):
        """Tells you if you should do something."""
        if arg == "die":
            await ctx.send("NO")

        else:  
            choice = random.choice(["Yes", "Probably", "No", "Maybe", "If you're asking then probably", "absolutely not", "I don't know I'm just 100 lines of code... sorry :(", "Yes", "Probably", "No", "Maybe", "If you're asking then probably", "absolutely not"])
            await ctx.send(str(choice))    
                
                
    @commands.command()
    async def why(self, ctx):
        """for all your programming needs"""
        await ctx.send("IM SORRY THE COMPUTER IS LYING TO YOU <3 it'll work soon!!!")    
    
    
    @commands.command()
    async def scream(self, ctx):
        """same"""
        await ctx.send("AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")   
        
        
    @commands.command()
    async def remind(self, ctx, *, arg):
        await ctx.send(arg)

        
def setup(bot):
    bot.add_cog(Utilities(bot))