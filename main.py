import discord
from discord.ext import commands

bot = commands.Bot(debug_guilds=[955135608228024394], command_prefix="-", status=discord.Status.dnd,activity=discord.Activity(type=discord.ActivityType.watching, name="how bad I am at coding"),owner='820255805257023498')


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
    print("command used 'add'.")


@bot.command()
async def multi(ctx, a: int, b: int):
    await ctx.send(f"{a} * {b} = {a * b}")
    print("command used 'muti'.")


@bot.command()
async def divide(ctx, a: int, b: int):
    await ctx.send(f"{a} / {b} = {a / b} :grinning:")
    print("command used 'divide'.")
    print(f"{a} / {b} = {a / b}"  )


@bot.command()
async def papa(ctx, b1 ):
    await ctx.send(papa)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.CommandError):
        await ctx.reply(f"oh noo! there is an error : {str(error)}\nmessage the owner for support")
        print(error)


bot.run("")
