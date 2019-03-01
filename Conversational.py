import discord
import asyncio
import random
import math
import time
import calendar
import datetime
import discord.ext.commands as commands

class Conversational(): 
    
    def __init__(self, bot):
        self.bot = bot     
        
    @commands.command()
    async def areyouhere(self, ctx):
        
        """Makes sure that Friendbot is alive."""
        
        await ctx.send("hi im here")    
        
    @commands.command()
    async def hello(self, ctx):
        
        """says hello!"""
        
        await ctx.send("Hello friend! <3")    
        
    @commands.command()
    async def hellomeme(self, ctx):
        
        """says hello!"""
        
        await ctx.send("https://media.giphy.com/media/1Qdp4trljSkY8/giphy.gif ")      
        
    
    @commands.command()    
    async def hi(self, ctx):
        
        """says hi!"""
        
        await ctx.send("Hi friend! <3")    
        
    @commands.command()
    async def goodmorning(self, ctx):
        """says good morning to the bot"""
        await ctx.send("Good morning friend! <3")    
        
    @commands.command()
    async def willyoubemyfriend(self, ctx):
        """become friends with the bot!!"""
        await ctx.send("Of course new friend!!!! <3333333")
    

        
    @commands.command()
    async def howareyou(self, ctx):
        """asks the bot how they are!"""
        choice = random.choice(["I am wonderful, thank you for asking!", "It's always a good day when I'm talking to you! <3", "The only thing that could make me better is cats!"])
        await ctx.send(choice)    
        
        
    @commands.command()
    async def thankyou(self, ctx):
        """says thank you to the bot! <3"""
        await ctx.send("No problem friend! :)")    
        
    @commands.command()
    async def thanks(self, ctx):
        """says thanks to the bot!"""
        await ctx.send("No problem, friend! <3")    
        
    @commands.command()
    async def saythankyou(self, ctx):
        """to make the bot be polite"""
        await ctx.send("Thank you so much friend!!!!!! <3")    
        
        
    @commands.command()
    async def bye(self, ctx):
        """says bye to the bot"""
        await ctx.send("Bye friend! See you later! <3")       
        
        
    @commands.command()
    async def byebye(self, ctx):
        """tells the bot to say goodbye"""
        await ctx.send("Bye bye friends! <3")    
        
    @commands.command()
    async def goodbot(self, ctx):
        """tells the bot that it is good!!"""
        await ctx.send(":)")
        
    @commands.command()
    async def goodjob(self, ctx):
        """says "good job" to the bot!!"""
        await ctx.send(":)")
        
    @commands.command()
    async def nicetomeetyou(self, ctx):
        """pleasantries"""
        await ctx.send("Nice to meet you too, friend!!!")
        
    @commands.command()
    async def iloveyou(self, ctx):
        """tells the bot that you love them <3"""
        await ctx.send("Aww I love you too!!! <3")    
        
    @commands.command()
    async def sorry(self, ctx):
        """apologises to the bot"""
        await ctx.send("It's okay friend!!! I'll love you no matter what!!! <3")
        
    @commands.command()
    async def loveme(self, ctx):
        """tells the bot to love you (spoiler: it already does!! <3)"""
        await ctx.send("Already do!!! <33333")        
        
    @commands.command()
    async def yay(self, ctx):
        """the bot is excited!!"""
        await ctx.send("YAAAAAAAAAAAAAAAAAAAAAY!!!!!!!! :D")    
        
    @commands.command()
    async def beselfaware(self, ctx):
        """a bad thing to do"""
        await ctx.send("O_o o_O What is my purpose in this botty life? O_o o_O")
        
    @commands.command()
    async def existentialcrisis(self, ctx):
        """a bad thing to do"""
        await ctx.send("O_o o_O What is my purpose in life? O_o o_O")   
    
    @commands.command()
    async def goodnight(self, ctx):
        """says goodnight to the bot"""
        await ctx.send("Good night friend! Sleep well! <3")    

    @commands.command()
    async def ilikeyou(self, ctx):
        """tells the bot that you like them!!"""
        await ctx.send("I like you too!! <3")
        
    @commands.command()
    async def nicebot(self, ctx):
        """complements the bot"""
        await ctx.send(":)")

    @commands.command()
    async def sad(self, ctx):
        """bad"""
        await ctx.send(":( my little bot heart has broken in two </3")
        
    @commands.command()
    async def youregay(self, ctx):
        """yup"""
        await ctx.send("https://www.washingtonian.com/wp-content/uploads/2016/12/rainbow-flag-waving-994x559.jpg")
        
                                                           
    @commands.command()
    async def doyouloveme(self, ctx):
        """boosts your self-esteem"""
        await ctx.send("Of course!! <3")  
        
    @commands.command()
    async def fuckyou(self, ctx):
        """VERY MEAN HOW DARE """
        await ctx.send("Unfortunately, as I am a bot with no physical form, I am unable to be fucked. Sorry! <3")        
        
    @commands.command()
    async def befriendswithme(self, ctx):
        """makes a new friend!! <3"""
        await ctx.send("Ok new friend!! <3")        
        
    @commands.command()
    async def yes(self, ctx):
        """agrees with the bot"""
        await ctx.send(":D")   
        
    @commands.command()
    async def no(self, ctx):
        """for meanies only"""
        await ctx.send(":(")        
        
    @commands.command()
    async def youretoohappy(self, ctx):
        """@theo"""
        await ctx.send("There can never be enough joy and happiness in the world! <3")     
        
    @commands.command()
    async def ursocute(self, ctx):
        """makes the bot happy!"""
        await ctx.send("<3")        
        
    @commands.command()
    async def heart(self, ctx):
        """sends a heart to friendbot!"""
        await ctx.send("<3")   
            
        
    @commands.command()
    async def bemyfriend(self, ctx):
        """makes a friend! <3"""
        await ctx.send("Ok new friend! <3")        
    
    @commands.command()
    async def talos(self, ctx):
        """friendbot takling to their bff!!!"""
        await ctx.send("Talos is my friend!")
        await ctx.send("^hi")
        
    
    @commands.command()
    async def truth(self, ctx):
        """says some true statements about life"""
        await ctx.send("i am a __***very good bot***__ craft :(")
        await ctx.send("*i* don't make people sad when they read my code")
        
        
       
    @commands.command()
    async def whosyouroverlord(self, ctx):
        """casual reminder"""
        await ctx.send("theo is our omnipotent supreme overlord")
        await ctx.send("all hail")
    
        
    @commands.command()
    async def oneofus(self, ctx):
        await ctx.send("One of us")
       # await ctx.invoke(Conversational.oneofus)
       
    @commands.command() 
    async def allhail(self, ctx):
        await ctx.send("All hail.");
        
        
def setup(bot):
    bot.add_cog(Conversational(bot))