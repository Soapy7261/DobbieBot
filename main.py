import discord
from discord.ext import commands
bot = commands.Bot(command_prefix="!", status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing, name="games"))
@bot.listen()
async def on_ready():
    print ("Now ready!")

@bot.command()
async def hello(ctx):
    await ctx.reply ("Hello!")
    print("send command 'hello'.")
@bot.command()
async def test(ctx):
    await ctx.send ("test!")
    print("send command 'test!'")
bot.run("")
