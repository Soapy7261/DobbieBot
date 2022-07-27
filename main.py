import discord
from discord.ext import commands
bot = commands.Bot(command_prefix="!", status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing, name="games"))
@bot.listen()
async def on_ready():
    print ("Now ready!")

@bot.slash_command(description="Hello!")
async def hello(ctx):
    await ctx.reply ("Hello!")
bot.run("BOTTOKENHERE")
