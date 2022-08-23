import discord
from discord.ext import commands

bot = commands.Bot(debug_guilds=[955135608228024394], command_prefix="-", status=discord.Status.dnd,activity=discord.Activity(type=discord.ActivityType.listening, name="keyboard noises"),owner='820255805257023498')


@bot.listen()
async def on_ready():
    print("Now ready!")
    embed = discord.Embed(title="Online!", timestamp=discord.utils.utcnow(), color=0x00ff00)
    await bot.get_guild(955135608228024394).get_channel(1011649871511572500).send(embed=embed)

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
    if b == 0:
        await ctx.send ("You fool.")
        return
    await ctx.send(f"{a} / {b} = {a / b} :grinning:")
    print("command used 'divide'.")
    print(f"{a} / {b} = {a / b}"  )


@bot.command()
async def papa(ctx, b1 ):
    await ctx.send(b1)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.CommandError):
        await ctx.reply(f"oh noo! there is an error : {str(error)}\nmessage the owner for support")
        print(error)


bot.run("")
