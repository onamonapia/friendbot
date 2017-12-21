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
    await bot.say(str(arg))
    
@bot.command()
async def areyoustillhere():
    await bot.say("hi im here")
    
@bot.command()
async def areyouhere():
    await bot.say("hi im here")
    
@bot.command()
async def hello():
    """says hello!"""
    await bot.say("Hello friend! <3")

@bot.command()    
async def hi():
    """says hi!"""
    await bot.say("Hi friend! <3")
    
@bot.command()
async def bemyfriend():
    """makes a friend! <3"""
    await bot.say("Ok new friend! <3")
    friendcount += 1
    
@bot.command()
async def be(*, arg):
    """becomes whatever u want it to be"""
    arg = str(arg)
    await bot.say("Ok now I'm " + arg)
    
@bot.command()
async def cat():
    """makes a true proclamation"""
    await bot.say("Cats are the best animals in the universe and if u disagree i will fiGHT YOU")
    await bot.say("teehee!! <3")
    
@bot.command()
async def cats():
    """makes a true proclamation"""
    await bot.say("Cats are the best animals in the universe and if u disagree i will fiGHT YOU")
    await bot.say("teehee!! <3")
    
@bot.command()
async def cutecat():
    """screams"""
    await bot.say("AWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW")
    await bot.say("IT'S SO CUTE!!!!!!!!!!!!!!")
    
@bot.command()
async def shouldi(*arg):
    """tells you if you should do something!"""
    choice = random.choice(["Yes", "Probably", "No", "Maybe", "If you're asking then probably", "absolutely not", "I don't know I'm just 100 lines of code... sorry :(", "Yes", "Probably", "No", "Maybe", "If you're asking then probably", "absolutely not"])
    await bot.say(str(choice))
    
@bot.command()
async def why():
    """for all your programming needs"""
    await bot.say("IM SORRY THE COMPUTER IS LYING TO YOU <3 it'll work soon!!!")
    
@bot.command()
async def no():
    """for meanies only"""
    await bot.say(":(")
    
@bot.command()
async def thankyou():
    """says thank you to the bot! <3"""
    await bot.say("No problem friend! :)")
    
@bot.command()
async def heart():
    """sends a heart to friendbot!"""
    await bot.say("<3")
    
@bot.command()
async def talktome():
    """starts a conversation"""
    await bot.say("How are you today?")
    
@bot.command()
async def good():
    """answer to 'how are you?'"""
    await bot.say("Yay! that's good!")

@bot.command()
async def bad():
    """answer to 'how are you?'"""
    await bot.say("Aw :( I hope tomorrow will be better <3")
    
@bot.command()
async def howareyou():
    """asks the bot how they are!"""
    choice = random.choice(["I am wonderful, thank you for asking!", "It's always a good day when I'm talking to you! <3", "The only thing that could make me better is cats!"])
    await bot.say(choice)
    
@bot.command()
async def saythankyou():
    """to make the bot be polite"""
    await bot.say("Thank you so much friend!!!!!! <3")
    
@bot.command()
async def wordcountgoal():
    """gives you a word count goal for the day"""
    wordcount = random.randint(300, 1000)
    await bot.say("I bet you can write {0} words or more today!".format(wordcount))
    
@bot.command()
async def talos():
    """tries to make a friend but is brutally rejected"""
    await bot.say("Talos is my friend!")
    await bot.say("^hi")
    
@bot.command()
async def goodnight():
    """says goodnight to the bot"""
    await bot.say("Good night friend! Sleep well! <3")
    
@bot.command()
async def whatthefuckareyou():
    """@jame"""
    await bot.say("I am your friend! :)")
    
@bot.command()
async def youarenotmyfriend():
    """meanie command"""
    await bot.say(":(")
    
@bot.command()
async def youretoohappy():
    """@jame"""
    await bot.say("There can never be enough joy and happiness in the world! <3")
    
@bot.command()
async def teeheemyass():
    """@jame"""
    await bot.say(":(")

@bot.command()
async def scream():
    """same"""
    await bot.say("AHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHHH")
    
@bot.command()
async def goodmorning():
    """says good morning to the bot"""
    await bot.say("Good morning friend! <3")

@bot.command()
async def youscareme():
    """@jame"""
    await bot.say(":( I'm sorry friendo :(")
    
@bot.command()
async def stopcallingmefriend():
    """@jame"""
    await bot.say(":(")

@bot.command()
async def ursocute():
    #makes the bot happy!
    await bot.say("<3")
 
@bot.command()
async def bye():
    #says bye to the bot
    await bot.say("Bye friend! See you later! <3")
    
@bot.command()
async def truth():
    #says some true statements about life
    await bot.say("i am a __***very good bot***__ craft :(")
    await bot.say("*i* don't make people sad when they read my code")
    
@bot.command()
async def yes():
    #agrees with the bot
    await bot.say(":D")
    
@bot.command()
async def beselfaware():
    #a bad thing to do
    await bot.say("O_o o_O What is my purpose in life? O_o o_O")
    
@bot.command()
async def existentialcrisis():
    #a bad thing to do
    await bot.say("O_o o_O What is my purpose in life? O_o o_O")
    
@bot.command()
async def howmanyfriendsdoyouhave():
    #prints number of friends
    await bot.say(str(friendcount))
    
@bot.command()
async def truefriends():
    await bot.say("yay true friendship!!!!! <3")
    
    
@bot.command()
async def imtheoverlord():
    await bot.say("all hail")
    
@bot.command()
async def whosyouroverlord():
    await bot.say("Jame is our omnipotent supreme overlord")
    await bot.say("all hail")
    
@bot.command()
async def whowantstoww():
    await bot.say("I do!!!!!!!!!")
    
@bot.command()
async def ilikeyounow():
    await bot.say("Yay! <3 :D")
    
@bot.command()
async def befriendswith(*, arg):
    await bot.say(str(arg) + " is my new friend! <3")
    
@bot.command()
async def byebye():
    await bot.say("Bye bye friends! <3")
    
@bot.command()
async def yay():
    await bot.say("YAAAAAAAAAAAAAAAAAAAAAY!!!!!!!! :D")
    
@bot.command()
async def nicetomeetyou():
    await bot.say("Nice to meet you too, friend!!!")
    
@bot.command()
async def iloveyou():
    await bot.say("Aww I love you too!!! <3")
    
@bot.command()
async def thanks():
    await bot.say("No problem, friend! <3")
    
@bot.command()
async def generatename():
    name = random.choice(["Bob", "Joe", "Cthulhu", "Satan"])
    await bot.say(str(name))
    
    
@bot.command()
async def wordcountchallenge():
    words = random.randint(50, 1000)
    minminutes = math.ceil(words / 150)
    maxminutes = math.ceil(words / 50)
    minutes = random.randint(minminutes, maxminutes)
    if minutes == 0:
        minutes =1
    await bot.say("I bet you can write {0} words in {1} minutes!".format(words, minutes))
    
@bot.command()
async def goodbot():
    await bot.say(":)")
    
@bot.command()
async def goodjob():
    await bot.say(":)")

    
    
@bot.command()
async def flipcoin():
    cointoss = random.choice(["Heads", "Tails"])
    await bot.say(str(cointoss))
    
@bot.command()
async def willyoubemyfriend():
    await bot.say("Of course new friend!!!! <3333333")
    
@bot.command()
async def guineapigs():
    await bot.say("Guinea pigs are adorable and perfect little creatures!!! <333")
    
@bot.command()
async def guineapig():
    await bot.say("Guinea pigs are adorable and perfect little creatures!!! <333")
    
@bot.command()
async def dog():
    await bot.say("Dogs are perfect and deserve all love")

@bot.command()
async def dogs():
    await bot.say("Dogs are perfect and deserve all love")


@bot.command()
async def befriendswithme():
    await bot.say("Ok new friend!! <3")
    
@bot.command()
async def fuckyou():
    await bot.say("Unfortunately, as I am a bot with no physical form, I am unable to be fucked. Sorry! <3")

@bot.command()
async def sorry():
    await bot.say("It's okay friend!!! I'll love you no matter what!!! <3")
    
@bot.command()
async def loveme():
    await bot.say("Already do!!! <33333")
    
"""@bot.command()
async def nanocountdown():
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
        await bot.say("It's NaNoWriMo!")
        days = 30 - int(currentdate[2])
        hours = 23 - int(currentdate[3][0])
        minutes = 59 - int(currentdate[3][1])
        seconds = 60 - int(currentdate[3][2])
        await bot.say("There are {0} days, {1} hours, {2} minutes, and {3} seconds left of NaNo! (Eastern Time)".format(days, hours, minutes, seconds))  
    else:
        await bot.say("fail")
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
        await bot.say("There are {0} days, {1} hours, {2} minutes, and {3} seconds until NaNo! (Eastern Time)".format(days, hours, minutes, seconds)) """

@bot.command()
async def nanocountdown():
    nano = datetime.date(1, 11, 1)
    camp1 = datetime.date(1, 4, 1)
    camp2 = datetime.date(1, 7, 1)
    now = datetime.datetime.today()    
    if now.month == nano.month:
        await bot.say("It's NaNo!")
        timeleft = datetime.datetime(now.year, 12, 1, 0, 0, 0) - now
        hours = timeleft.seconds // 3600
        minutes = (timeleft.seconds - (hours * 3600)) // 60
        seconds = timeleft.seconds - (hours * 3600) - (minutes * 60)
        await bot.say("There are {0} days, {1} hours, {2} minutes, and {3} seconds left of NaNo!".format(timeleft.days, hours, minutes, seconds)) 
    else:
        if now.month != 12:
            timeleft = datetime.datetime(now.year, 11, 1, 0, 0, 0) - now
        else:
            timeleft = datetime.datetime(now.year + 1, 11, 1, 0, 0, 0) - now
        hours = timeleft.seconds // 3600
        minutes = (timeleft.seconds - (hours * 3600)) // 60
        seconds = timeleft.seconds - (hours * 3600) - (minutes * 60)
        await bot.say("There are {0} days, {1} hours, {2} minutes, and {3} seconds left until NaNo!".format(timeleft.days, hours, minutes, seconds))
        
    if now.month == camp1.month:
        await bot.say("It's Camp NaNo!")
        timeleft = datetime.datetime(now.year, 5, 1, 0, 0, 0) - now
        hours = timeleft.seconds // 3600
        minutes = (timeleft.seconds - (hours * 3600)) // 60
        seconds = timeleft.seconds - (hours * 3600) - (minutes * 60)
        await bot.say("There are {0} days, {1} hours, {2} minutes, and {3} seconds left of Camp NaNo!".format(timeleft.days, hours, minutes, seconds)) 
    else:
        if now.month != 12 and now.month != 11 and now.month != 10 and now.month != 9 and now.month != 8 and now.month != 7 and now.month != 6 and now.month != 5:
            timeleft = datetime.datetime(now.year, 4, 1, 0, 0, 0) - now
        else:
            timeleft = datetime.datetime(now.year + 1, 4, 1, 0, 0, 0) - now
        hours = timeleft.seconds // 3600
        minutes = (timeleft.seconds - (hours * 3600)) // 60
        seconds = timeleft.seconds - (hours * 3600) - (minutes * 60)
        await bot.say("There are {0} days, {1} hours, {2} minutes, and {3} seconds left until April's Camp!".format(timeleft.days, hours, minutes, seconds))
  
    if now.month == camp2.month:
        await bot.say("It's Camp NaNo!")
        timeleft = datetime.datetime(now.year, 8, 1, 0, 0, 0) - now
        hours = timeleft.seconds // 3600
        minutes = (timeleft.seconds - (hours * 3600)) // 60
        seconds = timeleft.seconds - (hours * 3600) - (minutes * 60)
        await bot.say("There are {0} days, {1} hours, {2} minutes, and {3} seconds left of Camp NaNo!".format(timeleft.days, hours, minutes, seconds)) 
    else:
        if now.month != 12 and now.month != 11 and now.month != 10 and now.month != 9 and now.month != 8:
            timeleft = datetime.datetime(now.year, 7, 1, 0, 0, 0) - now
        else:
            timeleft = datetime.datetime(now.year + 1, 7, 1, 0, 0, 0) - now
        hours = timeleft.seconds // 3600
        minutes = (timeleft.seconds - (hours * 3600)) // 60
        seconds = timeleft.seconds - (hours * 3600) - (minutes * 60)
        await bot.say("There are {0} days, {1} hours, {2} minutes, and {3} seconds left until July's Camp!".format(timeleft.days, hours, minutes, seconds))
        
@bot.command()
async def doyoulikeme():
    await bot.say("Of course!! <3")
                                                       
@bot.command()
async def doyouloveme():
    await bot.say("Of course!! <3")            
    
@bot.command()
async def doyouwannabemyfriend():
    await bot.say("Of course!! <3")
    
@bot.command()
async def ifyoudocheckyesorno():
    await bot.say("*checks yes*")
    
@bot.command()
async def sad():
    await bot.say(":( my little bot heart has broken in two </3")
    
@bot.command()
async def petmycat():
    await bot.say("*pets all the cats*")

@bot.command()
async def ilikeyou():
    await bot.say("I like you too!! <3")
    
@bot.command()
async def nicebot():
    await bot.say(":)")

bot.run("")

