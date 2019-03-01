import discord
import math
import discord.ext.commands as commands

#makes a number an integer or rounds it to the inputted value
def intTest(number, roundValue):
    if number == int(number):
        number = int(number)
    else:
        number = round(number, roundValue)
        
    return number

#tests whether the input is correct or not
def numberTest(inputted):
    try:
        inputted = float(inputted)
        return True
    except ValueError:
        return False    
    
def inputTest(inputted, character):
    for i in range(0, len(inputted) - 1):
        if inputted[i] != ' ' and inputted[i] != '.' and inputted[i] != character:
            if numberTest(inputted[i]) == False:
                return False
    return True
    
  

class Math():
    
    def __init__(self, bot):
        self.bot = bot    
        
    """~~~~~~~~~~~~~~~~~~~~ARITHMETIC FUNCTIONS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~``"""
    
    @commands.command()
    async def math(self, ctx, *, arg):
        
        """Solves an inputted arithmetic equation."""
        
        if inputTest(arg, '+') == False and inputTest(arg, '-') == False and inputTest(arg, '*') == False and inputTest(arg, 'x') == False and inputTest(arg, '/') == False:
            await ctx.send("AHHHHHHHHHHHHHHHHHHHHH") 
            
        
        i = 0
        number1 = ""
        while arg[i] != '+' and arg[i] != '-' and arg[i] != '*' and arg[i] != 'x' and arg[i] != '/':
            number1 = number1 + arg[i]
            i = i + 1
            
        operator = arg[i]
        arg = arg[i + 1:]
        
        number1 = float(number1)
        
        number1 = intTest(number1, 2)
        number2 = intTest(float(arg), 2)
        
        if operator == '+':
            answer = number1 + number2

        elif operator == '-':
            answer = number1 - number2

        elif operator == '*' or operator == 'x':
            answer = number1 * number2
            
        elif operator == '/':
            answer = number1 / number2       
        
        answer = intTest(answer, 2)
            
        await ctx.send(answer)    
        
        
    @commands.command()
    async def add(self, ctx, *, arg):
        
        """Solves an inputted addition problem."""
        
        if inputTest(arg, '+') == False:
            await ctx.send("AHHHHHHHHHHHHHHHHHHHHH") 
            
        i = 0
        number1 = ""
        while arg[i] != '+':
          
            number1 = number1 + arg[i]
            i = i + 1
            
        arg = arg[i + 1:]
        
        number1 = float(number1)
        
        number1 = intTest(number1, 2)
        number2 = intTest(float(arg), 2)
        
        await ctx.send(intTest(number1 + number2, 2))     
        
        
        
    @commands.command()
    async def subtract(self, ctx, *, arg):
        
        """Solves an inputted subtraction problem."""
        
        if inputTest(arg, '-') == False:
            await ctx.send("AHHHHHHHHHHHHHHHHHHHHH") 
            
        i = 0
        number1 = ""
        while arg[i] != '-':
          
            number1 = number1 + arg[i]
            i = i + 1
            
        arg = arg[i + 1:]
        
        number1 = float(number1)
        
        number1 = intTest(number1, 2)
        number2 = intTest(float(arg), 2)
        
        await ctx.send(intTest(number1 - number2, 2)) 
        
        
    @commands.command()
    async def multiply(self, ctx, *, arg):
        """Solves an inputted multiplication problem."""
        
        if inputTest(arg, '*') == False and inputTest(arg, 'x') == False:
            await ctx.send("AHHHHHHHHHHHHHHHHHHHHH")

        i = 0
        number1 = ""
        while arg[i] != '*' and arg[i] != 'x':
          
            number1 = number1 + arg[i]
            i = i + 1
            
        arg = arg[i + 1:]
        
        number1 = float(number1)

        number1 = intTest(number1, 2)
        number2 = intTest(float(arg), 2)
        
        await ctx.send(intTest(number1 * number2, 2)) 
        
        
    @commands.command()
    async def divide(self, ctx, *, arg):
        """Solves an inputted division problem."""
        
        if inputTest(arg, '/') == False:
            await ctx.send("AHHHHHHHHHHHHHHHHHHHHH") 
            
        i = 0
        number1 = ""
        while arg[i] != '/':
          
            number1 = number1 + arg[i]
            i = i + 1
            
        arg = arg[i + 1:]
        
        number1 = float(number1)
        
        number1 = intTest(number1, 2)
        number2 = intTest(float(arg), 2)
        
        await ctx.send(intTest(number1 / number2, 2)) 
        
    """~~~~~~~~~~~~~~~CONVERSION FUNCTIONS~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"""
    
    @commands.command()
    async def ctof(self, ctx, *, arg):
        """Converts a temperature given in Celsius to Fahrenheit."""
        
        if numberTest(arg) == False:
            await ctx.send("AHHHHHHHHHHHHHHHHHHHHH")
            
        celsius = float(arg)
        returnValue = celsius * (9 / 5)
        returnValue = returnValue + 32
        fahrenheit = returnValue
        
        celsius = intTest(celsius, 1)
        fahrenheit = intTest(fahrenheit, 1)
        
        await ctx.send("{0}\u00B0C is equal to {1}\u00B0F.".format(celsius, fahrenheit)) 
        
        
    @commands.command()
    async def ftoc(self, ctx, *, arg): 
        """Converts a temperature given in Fahrenheit to Celsius."""
            
        if numberTest(arg) == False:
            await ctx.send("AHHHHHHHHHHHHHHHHHHHHH")
        
        fahrenheit = float(arg);
        celsius = fahrenheit - 32
        celsius = celsius * (5 / 9)
        
        celsius = intTest(celsius, 1)
            
        fahrenheit = intTest(fahrenheit, 1)
        
        await ctx.send("{0}\u00B0F is equal to {1}\u00B0C.".format(fahrenheit, celsius))
        
        
    @commands.command()
    async def cmtoft(self, ctx, *, arg): 
        """Converts from centimetres to feet and inches."""
            
        if numberTest(arg) == False:
            await ctx.send("AHHHHHHHHHHHHHHHHHHHHH")
            
        
        cm = float(arg);
        inches = cm * (1 / 2.54)
        feet = 0
        while inches >= 12:
            inches = inches - 12
            feet = feet + 1
            
        inches = intTest(inches, 2)
        cm = intTest(cm, 2)

        await ctx.send("{0} cm is equal to {1} feet and {2} inches.".format(cm, feet, inches))    
        
    @commands.command()
    async def intocm(self, ctx, *, arg): 
        """Converts from inches to centimetres."""
            
        if numberTest(arg) == False:
            await ctx.send("AHHHHHHHHHHHHHHHHHHHHH")
            
        
        inches = float(arg);
        cm = inches * 2.54
        
        feet = 0
        while inches >= 12:
            inches = inches - 12
            feet = feet + 1     
            
        inches = intTest(inches, 2)
        cm = intTest(cm, 2)

        await ctx.send("{0} ft and {1} in is equal to {2} cm.".format(feet, inches, cm))         

   
    @commands.command()
    async def fttocm(self, ctx, *, arg):
        """Converts from feet and inches to centimetes. """
        
        if inputTest(arg, '\'') == False:
            await ctx.send("AHHHHHHHHHHHHHHHHHHHHH") 
            
        i = 0
        feet = ""
        while arg[i] != '\'':
            feet = feet + arg[i]
            i = i + 1
            
        arg = arg[i + 1:]
        inches = arg
        
        inches = float(inches)
        feet = float(feet)
        
        inches2 = inches + (12 * feet)
        
        cm = inches2 * 2.54
        
        feet = 0
        while inches2 >= 12:
            inches2 = inches2 - 12
            feet = feet + 1
        
        inches = intTest(inches2, 2)
        cm = intTest(cm, 2)
        
        await ctx.send("{0} ft and {1} in is equal to {2} cm.".format(feet, inches, cm))
  
    @commands.command()
    async def kmtomi(self, ctx, *, arg): 
        """Converts from kilometres to miles."""
            
        if numberTest(arg) == False:
            await ctx.send("AHHHHHHHHHHHHHHHHHHHHH")
            
        
        km = float(arg);
        mi = km * 1.609344 
        
        km = intTest(km, 2)
        mi = intTest(mi, 2)
        if mi == 1:
            await ctx.send("{0} km is equal to {1} mile.".format(km, mi))       
        else:
            await ctx.send("{0} km is equal to {1} miles.".format(km, mi));
            
    @commands.command()
    async def mitokm(self, ctx, *, arg): 
        """Converts from miles to kilometres."""
            
        if numberTest(arg) == False:
            await ctx.send("AHHHHHHHHHHHHHHHHHHHHH")
            
        
        mi = float(arg);
        km = mi * 0.62137119 
        
        km = intTest(km, 2)
        mi = intTest(mi, 2)
        if  mi == 1:
            await ctx.send("{0} mile is equal to {1} km.".format(mi, km))       
        else:
            await ctx.send("{0} miles is equal to {1} km.".format(mi, km));
        
        
    @commands.command()
    async def f4(self, ctx):
        """prints the number 4, because it is very useful"""
        await ctx.send("4");

def setup(bot):
    bot.add_cog(Math(bot))