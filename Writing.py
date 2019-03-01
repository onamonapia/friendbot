import discord
import asyncio
import random
import math
import time
import calendar
import datetime
import discord.ext.commands as commands

class Writing():
    
    def __init__(self, bot):
        self.bot = bot     
        
        
    @commands.command()
    async def wordcountchallenge(self, ctx, *, arg = None):
        
        """Gives you a writing challenge! Input your wpm (or don't, that's ok too)"""
        
        if arg == None:
            words = random.randint(50, 1000)
            minminutes = math.ceil(words / 120)
            maxminutes = math.ceil(words / 30)
            minutes = random.randint(minminutes, maxminutes)
            if minutes == 0:
                minutes =1
            await ctx.send("I bet you can write {0} words in {1} minutes!".format(words, minutes))    
            
    
        else: 
            wpm = int(arg)
            words = random.randint(50, 1000)
            if wpm != 0 and wpm > 20:
                minminutes = math.ceil(words / (wpm + 20))
                maxminutes = math.ceil(words / (wpm - 20))
                minutes = random.randint(minminutes, maxminutes)
            else:
                words = random.randint(50, 1000)
                minminutes = math.ceil(words / 120)
                maxminutes = math.ceil(words / 30)
                minutes = random.randint(minminutes, maxminutes)
            if minutes == 0:
                minutes = 1
            await ctx.send("I bet you can write {0} words in {1} minutes!".format(words, minutes))    
        
        
    @commands.command()
    async def nanocountdown(self, ctx):
        
        """Counts down to the next NaNo event."""
        
        nano = datetime.date(1, 11, 1)
        camp1 = datetime.date(1, 4, 1)
        camp2 = datetime.date(1, 7, 1)
        now = datetime.datetime.today()    
        if now.month == nano.month:
            await ctx.send("It's NaNo!")
            timeleft = datetime.datetime(now.year, 12, 1, 0, 0, 0) - now
            hours = timeleft.seconds // 3600
            minutes = (timeleft.seconds - (hours * 3600)) // 60
            seconds = timeleft.seconds - (hours * 3600) - (minutes * 60)
            await ctx.send("There are {0} days, {1} hours, {2} minutes, and {3} seconds left of NaNo!".format(timeleft.days, hours, minutes, seconds)) 
        else:
            if now.month != 12:
                timeleft = datetime.datetime(now.year, 11, 1, 0, 0, 0) - now
            else:
                timeleft = datetime.datetime(now.year + 1, 11, 1, 0, 0, 0) - now
            hours = timeleft.seconds // 3600
            minutes = (timeleft.seconds - (hours * 3600)) // 60
            seconds = timeleft.seconds - (hours * 3600) - (minutes * 60)
            await ctx.send("There are {0} days, {1} hours, {2} minutes, and {3} seconds left until NaNo!".format(timeleft.days, hours, minutes, seconds))
            
        if now.month == camp1.month:
            await ctx.send("It's Camp NaNo!")
            timeleft = datetime.datetime(now.year, 5, 1, 0, 0, 0) - now
            hours = timeleft.seconds // 3600
            minutes = (timeleft.seconds - (hours * 3600)) // 60
            seconds = timeleft.seconds - (hours * 3600) - (minutes * 60)
            await ctx.send("There are {0} days, {1} hours, {2} minutes, and {3} seconds left of Camp NaNo!".format(timeleft.days, hours, minutes, seconds)) 
        else:
            if now.month != 12 and now.month != 11 and now.month != 10 and now.month != 9 and now.month != 8 and now.month != 7 and now.month != 6 and now.month != 5:
                timeleft = datetime.datetime(now.year, 4, 1, 0, 0, 0) - now
            else:
                timeleft = datetime.datetime(now.year + 1, 4, 1, 0, 0, 0) - now
            hours = timeleft.seconds // 3600
            minutes = (timeleft.seconds - (hours * 3600)) // 60
            seconds = timeleft.seconds - (hours * 3600) - (minutes * 60)
            await ctx.send("There are {0} days, {1} hours, {2} minutes, and {3} seconds left until April's Camp!".format(timeleft.days, hours, minutes, seconds))
      
        if now.month == camp2.month:
            await ctx.send("It's Camp NaNo!")
            timeleft = datetime.datetime(now.year, 8, 1, 0, 0, 0) - now
            hours = timeleft.seconds // 3600
            minutes = (timeleft.seconds - (hours * 3600)) // 60
            seconds = timeleft.seconds - (hours * 3600) - (minutes * 60)
            await ctx.send("There are {0} days, {1} hours, {2} minutes, and {3} seconds left of Camp NaNo!".format(timeleft.days, hours, minutes, seconds)) 
        else:
            if now.month != 12 and now.month != 11 and now.month != 10 and now.month != 9 and now.month != 8:
                timeleft = datetime.datetime(now.year, 7, 1, 0, 0, 0) - now
            else:
                timeleft = datetime.datetime(now.year + 1, 7, 1, 0, 0, 0) - now
            hours = timeleft.seconds // 3600
            minutes = (timeleft.seconds - (hours * 3600)) // 60
            seconds = timeleft.seconds - (hours * 3600) - (minutes * 60)
            await ctx.send("There are {0} days, {1} hours, {2} minutes, and {3} seconds left until July's Camp!".format(timeleft.days, hours, minutes, seconds))  
            
            
    @commands.command()
    async def wordcountgoal(self, ctx):
        """Gives you a word count goal for the day."""
        
        wordcount = random.randint(300, 1000)
        await ctx.send("I bet you can write {0} words or more today!".format(wordcount))    
    
    @commands.command()
    async def generatename(self, ctx):
        
        """Generates a name."""
        
        name = random.choice(["Bob", "Joe", "Cthulhu", "Satan"])
        await ctx.send(str(name))        
        
    @commands.command()
    async def encourageme(self, ctx):
        """ gives writerly encouragement """
        answer = random.choice(["Write!!! You're supposed to be a writer!!!!!!", "You can write! Just write for a few minutes; you can do it!!", "Your story needs to be heard! Go write it!", "Write!!! You're supposed to be a writer!!!!!!", "You can write! Just write for a few minutes; you can do it!!", "Your story needs to be heard! Go write it!", "if u dont write rn im gonna kill ur friends and family is that what you want"])
        await ctx.send(str(answer))
        
def setup(bot):
    bot.add_cog(Writing(bot))