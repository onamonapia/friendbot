import discord
import asyncio
import random
import math
import time
import calendar
import datetime
import discord.ext.commands as commands

class Animals():
    
    def __init__(self, bot):
        self.bot = bot   
        
    @commands.command()
    async def cat(self, ctx):
        """makes a true proclamation"""
        await ctx.send("Cats are the best animals in the universe and if u disagree i will fiGHT YOU")
        await ctx.send("teehee!! <3")
        
        
    @commands.command()
    async def cutecat(self, ctx):
        """screams"""
        await ctx.send("AWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW")
        await ctx.send("IT'S SO CUTE!!!!!!!!!!!!!!")        
        
    @commands.command()
    async def guineapigs(self, ctx):
        """true proclamation"""
        await ctx.send("Guinea pigs are adorable and perfect little creatures!!! <333")
        
    
    @commands.command()
    async def dogs(self, ctx):
        """truth"""
        await ctx.send("Dogs are perfect and deserve all love") 
        
        
    @commands.command()
    async def petmycat(self, ctx):
        """when friendbot is confronted with a kitty"""
        await ctx.send("*pets all the cats*")     
    
    @commands.command()
    async def siepie(self, ctx):
        """everyone's favourite kitty!!!!"""
        await ctx.send("HI SIEPIE I LOVE YOU YOU'RE MY BESTEST FRIEND <33333")
        
    @commands.command()
    async def sybilpoekie(self, ctx):
        """an ad from your 2020 president elects"""
        await ctx.send("https://media.discordapp.net/attachments/337363341070827520/453664558247051265/image.png?width=373&height=300")        
        
        
def setup(bot):
    bot.add_cog(Animals(bot))