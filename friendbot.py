import discord
import asyncio
import random
import math
import time
import calendar
import datetime
from discord.ext import commands




bot = commands.Bot(command_prefix='*')
friendcount = 0

@bot.command()
async def test(*arg):
    await ctx.send(str(arg))
    
@bot.command()
async def areyoustillhere(ctx):
    await ctx.send("hi im here")
    
@bot.command()
async def areyouhere(ctx):
    await ctx.send("hi im here")
    
@bot.command()
async def hello(ctx):
    """says hello!"""
    await ctx.send("Hello friend! <3")

@bot.command()    
async def hi(ctx):
    """says hi!"""
    await ctx.send("Hi friend! <3")
    
@bot.command()
async def bemyfriend(ctx):
    """makes a friend! <3"""
    await ctx.send("Ok new friend! <3")
    friendcount += 1
    
@bot.command()
async def be(ctx, *, arg):
    """becomes whatever u want it to be"""
    arg = str(arg)
    await ctx.send("Ok now I'm " + arg)
    
@bot.command()
async def cat(ctx):
    """makes a true proclamation"""
    await ctx.send("Cats are the best animals in the universe and if u disagree i will fiGHT YOU")
    await ctx.send("teehee!! <3")
    
@bot.command()
async def cats(ctx):
    """makes a true proclamation"""
    await ctx.send("Cats are the best animals in the universe and if u disagree i will fiGHT YOU")
    await ctx.send("teehee!! <3")
    
@bot.command()
async def cutecat(ctx):
    """screams"""
    await ctx.send("AWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW")
    await ctx.send("IT'S SO CUTE!!!!!!!!!!!!!!")
    
@bot.command()
async def shouldi(*arg):
    """tells you if you should do something!"""
    choice = random.choice(["Yes", "Probably", "No", "Maybe", "If you're asking then probably", "absolutely not", "I don't know I'm just 100 lines of code... sorry :(", "Yes", "Probably", "No", "Maybe", "If you're asking then probably", "absolutely not"])
    await ctx.send(str(choice))
    
@bot.command()
async def why(ctx):
    """for all your programming needs"""
    await ctx.send("IM SORRY THE COMPUTER IS LYING TO YOU <3 it'll work soon!!!")
    
@bot.command()
async def no(ctx):
    """for meanies only"""
    await ctx.send(":(")
    
@bot.command()
async def thankyou(ctx):
    """says thank you to the bot! <3"""
    await ctx.send("No problem friend! :)")
    
@bot.command()
async def heart(ctx):
    """sends a heart to friendbot!"""
    await ctx.send("<3")
    
@bot.command()
async def talktome(ctx):
    """starts a conversation"""
    await ctx.send("How are you today?")
    
@bot.command()
async def good(ctx):
    """answer to 'how are you?'"""
    await ctx.send("Yay! that's good!")

@bot.command()
async def bad(ctx):
    """answer to 'how are you?'"""
    await ctx.send("Aw :( I hope tomorrow will be better <3")
    
@bot.command()
async def howareyou(ctx):
    """asks the bot how they are!"""
    choice = random.choice(["I am wonderful, thank you for asking!", "It's always a good day when I'm talking to you! <3", "The only thing that could make me better is cats!"])
    await ctx.send(choice)
    
@bot.command()
async def saythankyou(ctx):
    """to make the bot be polite"""
    await ctx.send("Thank you so much friend!!!!!! <3")
    
@bot.command()
async def wordcountgoal(ctx):
    """gives you a word count goal for the day"""
    wordcount = random.randint(300, 1000)
    await ctx.send("I bet you can write {0} words or more today!".format(wordcount))
    
@bot.command()
async def talos(ctx):
    """tries to make a friend but is brutally rejected"""
    await ctx.send("Talos is my friend!")
    await ctx.send("^hi")
    
@bot.command()
async def goodnight(ctx):
    """says goodnight to the bot"""
    await ctx.send("Good night friend! Sleep well! <3")
    
@bot.command()
async def whatthefuckareyou(ctx):
    """@jame"""
    await ctx.send("I am your friend! :)")
    
@bot.command()
async def youarenotmyfriend(ctx):
    """meanie command"""
    await ctx.send(":(")
    
@bot.command()
async def youretoohappy(ctx):
    """@jame"""
    await ctx.send("There can never be enough joy and happiness in the world! <3")
    
@bot.command()
async def teeheemyass(ctx):
    """@jame"""
    await ctx.send(":(")

@bot.command()
async def scream(ctx):
    """same"""
    await ctx.send("AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
    
@bot.command()
async def goodmorning(ctx):
    """says good morning to the bot"""
    await ctx.send("Good morning friend! <3")

@bot.command()
async def youscareme(ctx):
    """@jame"""
    await ctx.send(":( I'm sorry friendo :(")
    
@bot.command()
async def stopcallingmefriend(ctx):
    """@jame"""
    await ctx.send(":(")

@bot.command()
async def ursocute(ctx):
    #makes the bot happy!
    await ctx.send("<3")
 
@bot.command()
async def bye(ctx):
    #says bye to the bot
    await ctx.send("Bye friend! See you later! <3")
    
@bot.command()
async def truth(ctx):
    #says some true statements about life
    await ctx.send("i am a __***very good bot***__ craft :(")
    await ctx.send("*i* don't make people sad when they read my code")
    
@bot.command()
async def yes(ctx):
    #agrees with the bot
    await ctx.send(":D")
    
@bot.command()
async def beselfaware(ctx):
    #a bad thing to do
    await ctx.send("O_o o_O What is my purpose in life? O_o o_O")
    
@bot.command()
async def existentialcrisis(ctx):
    #a bad thing to do
    await ctx.send("O_o o_O What is my purpose in life? O_o o_O")
    
@bot.command()
async def howmanyfriendsdoyouhave(ctx):
    #prints number of friends
    await ctx.send(str(friendcount))
    
@bot.command()
async def truefriends(ctx):
    await ctx.send("yay true friendship!!!!! <3")
    
    
@bot.command()
async def imtheoverlord(ctx):
    await ctx.send("all hail")
    
@bot.command()
async def whosyouroverlord(ctx):
    await ctx.send("Jame is our omnipotent supreme overlord")
    await ctx.send("all hail")
    
@bot.command()
async def whowantstoww(ctx):
    await ctx.send("I do!!!!!!!!!")
    
@bot.command()
async def ilikeyounow(ctx):
    await ctx.send("Yay! <3 :D")
    
@bot.command()
async def befriendswith(ctx, *, arg):
    await ctx.send(str(arg) + " is my new friend! <3")
    
@bot.command()
async def byebye(ctx):
    await ctx.send("Bye bye friends! <3")
    
@bot.command()
async def yay(ctx):
    await ctx.send("YAAAAAAAAAAAAAAAAAAAAAY!!!!!!!! :D")
    
@bot.command()
async def nicetomeetyou(ctx):
    await ctx.send("Nice to meet you too, friend!!!")
    
@bot.command()
async def iloveyou(ctx):
    await ctx.send("Aww I love you too!!! <3")
    
@bot.command()
async def thanks(ctx):
    await ctx.send("No problem, friend! <3")
    
@bot.command()
async def generatename(ctx):
    name = random.choice(["Bob", "Joe", "Cthulhu", "Satan"])
    await ctx.send(str(name))
    
    
@bot.command()
async def wordcountchallenge(ctx):
    words = random.randint(50, 1000)
    minminutes = math.ceil(words / 150)
    maxminutes = math.ceil(words / 50)
    minutes = random.randint(minminutes, maxminutes)
    if minutes == 0:
        minutes =1
    await ctx.send("I bet you can write {0} words in {1} minutes!".format(words, minutes))
    
@bot.command()
async def goodbot(ctx):
    await ctx.send(":)")
    
@bot.command()
async def goodjob(ctx):
    await ctx.send(":)")

    
    
@bot.command()
async def flipcoin(ctx):
    cointoss = random.choice(["Heads", "Tails"])
    await ctx.send(str(cointoss))
    
@bot.command()
async def willyoubemyfriend(ctx):
    await ctx.send("Of course new friend!!!! <3333333")
    
@bot.command()
async def guineapigs(ctx):
    await ctx.send("Guinea pigs are adorable and perfect little creatures!!! <333")
    
@bot.command()
async def guineapig(ctx):
    await ctx.send("Guinea pigs are adorable and perfect little creatures!!! <333")
    
@bot.command()
async def dog(ctx):
    await ctx.send("Dogs are perfect and deserve all love")

@bot.command()
async def dogs(ctx):
    await ctx.send("Dogs are perfect and deserve all love")


@bot.command()
async def befriendswithme(ctx):
    await ctx.send("Ok new friend!! <3")
    
@bot.command()
async def fuckyou(ctx):
    await ctx.send("Unfortunately, as I am a bot with no physical form, I am unable to be fucked. Sorry! <3")

@bot.command()
async def sorry(ctx):
    await ctx.send("It's okay friend!!! I'll love you no matter what!!! <3")
    
@bot.command()
async def loveme(ctx):
    await ctx.send("Already do!!! <33333")
    
"""@bot.command()
async def nanocountdown(ctx):
    currentdate = time.ctime()
    currentdate = currentdate.split(" ")
    currentdate[3] = currentdate[3].split(":")
    yearlist = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    if currentdate[0] % 4 == 0 and currentdate[0] % 100 != 0:
        monthlist = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    elif currentdate[0] % 4 != 0:
        monthlist = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    elif currentdate[0] % 100 == 0 and currentdate[0] % 400 == 0:
        monthlist = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        monthlist = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if currentdate[1] == "Nov":
        await ctx.send("It's NaNoWriMo!")
        days = 30 - int(currentdate[2])
        hours = 23 - int(currentdate[3][0])
        minutes = 59 - int(currentdate[3][1])
        seconds = 60 - int(currentdate[3][2])
        await ctx.send("There are {0} days, {1} hours, {2} minutes, and {3} seconds left of NaNo! (Eastern Time)".format(days, hours, minutes, seconds))  
    else:
        await ctx.send("fail")
    else:
        month = yearlist.index(currentdate[1])
        days = monthlist[month] - int(currentdate[2])
        if month != 12:
            month += 1
        elif month == 12:
            month = 1
        while month != 11:
            days += monthlist[month]
        hours = 23 - int(currentdate[3][0])
        minutes = 59 - int(currentdate[3][1])
        seconds = 60 - int(currentdate[3][2])    
        await ctx.send("There are {0} days, {1} hours, {2} minutes, and {3} seconds until NaNo! (Eastern Time)".format(days, hours, minutes, seconds)) """

@bot.command()
async def nanocountdown(ctx):
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
        
@bot.command()
async def doyoulikeme(ctx):
    await ctx.send("Of course!! <3")
                                                       
@bot.command()
async def doyouloveme(ctx):
    await ctx.send("Of course!! <3")            
    
@bot.command()
async def doyouwannabemyfriend(ctx):
    await ctx.send("Of course!! <3")
    
@bot.command()
async def ifyoudocheckyesorno(ctx):
    await ctx.send("*checks yes*")
    
@bot.command()
async def sad(ctx):
    await ctx.send(":( my little bot heart has broken in two </3")
    
@bot.command()
async def petmycat(ctx):
    await ctx.send("*pets all the cats*")

@bot.command()
async def ilikeyou(ctx):
    await ctx.send("I like you too!! <3")
    
@bot.command()
async def nicebot(ctx):
    await ctx.send(":)")

bot.run("")

