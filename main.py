import os
import sys
import discord
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.all()
bot = discord.Bot(debug_guilds=[955135608228024394], 
    status=discord.Status.dnd,
    activity=discord.Activity(
    type=discord.ActivityType.listening, 
    name="keyboard noises and no errors"),
    intents=intents)

@bot.event
async def on_ready():
    """When the bot is ready, print a message to the console."""
    embed = discord.Embed(title="🟢 Online!\nTime to mess around!", timestamp=discord.utils.utcnow(),
        color=discord.Color.green())
    await bot.get_guild(955135608228024394).get_channel(1011649871511572500).send(embed=embed)
    print("Now ready!")


@bot.slash_command(description="Restart the bot")
async def restart(ctx):
    """Restart the bot"""
    await ctx.respond("Restarting.")
    embed = discord.Embed(title="🔄 Restarting...", timestamp=discord.utils.utcnow(), color=discord.Color.orange())
    await bot.get_guild(955135608228024394).get_channel(
        1048306173071347782).send(
        embed=embed)
    sys.exit()

@bot.slash_command(description="Run a calculation")
async def math(ctx, first: discord.Option(int, description="The first number"), second: discord.Option(int, description="The second number"), operation: discord.Option(description="What operation you want to run", choices=["+", "-", "*", "/"])):
    """Run a calculation"""
    await ctx.defer()
    if operation == "+":
        output = f"{first}+{second} = {first + second}"
    if operation == '-':
        output= f"{first}-{second} = {first - second}"
    if operation == '*':
        output= f"{first}*{second} = {first * second}"
    if operation == '/':
        if second == 0:
            output= "Can't divide by 0"
        if second != 0:
            output= f"{first}/{second} = {first / second}"
    embed=discord.Embed(title='Calculation', timestamp=discord.utils.utcnow(), color=discord.Color.green())
    embed.add_field(name='Your calculation is here!', value=output)
    await ctx.respond(embed=embed)
    print(f'command math called {output} {ctx.author}')

@bot.slash_command(description='Get info about the bot')
async def info(ctx):
    """Get info about the bot"""
    embed = discord.Embed(
        title="DobbieBot",
        description = "The Dobbie bot",
        timestamp=discord.utils.utcnow(),
        color=discord.Color.dark_gray())
    embed.add_field(name="Ping",value=(round(bot.latency * 1000)))
    embed.add_field(name="Info about the bot",
        value="""this bot is made by Soapy7261#8558
        and Dobbie#4778. To teach Dobbie how 
        Discord bots work and how py-cord works!""")

    embed.add_field(name="Main commands", value="/math\n/info")
    await ctx.respond(embed=embed)

@bot.slash_command(description='Say hello', guild_ids=[955135608228024394])
async def hello(ctx):
    """Say hello"""
    await ctx.respond(f"Hello {ctx.user.mention}!", ephemeral=True)

@bot.slash_command(description='Test command')
async def test(ctx):
    """Test command"""
    await ctx.send("te@st!")
    print("send command 'test!'")

@bot.slash_command(description="Say something through the bot")
async def say(ctx, message: discord.Option(str, description="The message to say")):
    """Say something"""
    await ctx.delete()
    await ctx.send(message)

@bot.event
async def on_command_error(ctx, error):
    """When an error occurs"""
    await ctx.reply(f"An error occurred```py\n{str(error)}\n```Message the owner for support\nThis has been logged.")
    embed = discord.Embed(title="Error :(", timestamp=discord.utils.utcnow(),color=discord.Color.red())
    embed.add_field(name = "Error:", value=str(error))

    await bot.get_guild(955135608228024394).get_channel(1017880577506017361).send(embed=embed)

@bot.event
async def on_message(message):
    """When a message is sent"""
    print ("message")
    print (message.content)
    if "dobbie" in message.content.lower():
        print('you got fans')
        #Add an eyes reaction
        await message.add_reaction("👀")

bot.run(os.getenv('TOKEN'))
