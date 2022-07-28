import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.playing, name="watching how bad I am at coding"))


@bot.listen()
async def on_ready():
    print("Now ready!")


@bot.command()
async def hello(ctx):
    await ctx.reply("Hello!")
    print("send command 'hello'.")


@bot.command()
async def test(ctx):
    await ctx.send("te@st!")
    print("send command 'test!'")


@bot.command()
async def add(ctx, a: int, b: int):
    await ctx.send(f"{a} + {b} = {a + b}")


@bot.command()
async def mutiplay(ctx, a: int, b: int):
    await ctx.send(f"{a} * {b} = {a * b}")


@bot.command()
async def divide(ctx, a: int, b: int):
    await ctx.send(f"{a} / {b} = {a / b}")
    print("command 'divide' runed")

@bot.command()
async def help1(ctx):
    await ctx.reply("the command you can use:/n test")


bot.run("")
