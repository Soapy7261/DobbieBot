import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot =commands.Bot(debug_guilds=[955135608228024394], command_prefix="-", status=discord.Status.dnd,activity=discord.Activity(type=discord.ActivityType.listening, name="keyboard noises"),owner='820255805257023498',intents=intents,)


@bot.listen()
async def on_ready():
    print("Now ready!")
    embed = discord.Embed(title=":green_circle: Online!  \nTime to mess around!", timestamp=discord.utils.utcnow(), color=0x00ff00,)
    await bot.get_guild(955135608228024394).get_channel(1011649871511572500).send(embed=embed)



@bot.command()
async def hello(ctx):
    await ctx.reply("Hello!")
    print("send command 'hello'.")

@bot.command()
async def hello_hi(ctx):
   embed= discord.Embed(title="embed works", timestamp=discord.utils.utcnow(), color=0x00ff00,)
   await ctx.send(embed=embed)


@bot.command()
async def test(ctx):
    await ctx.send("te@st!")
    print("send command 'test!'")


@bot.command()
async def add(ctx, add1: int, add2: int):
    await ctx.send(f"{add1} + {add2} = {add2 + add2}")
    print("command used 'add'.")


@bot.command()
async def multi(ctx, multi1: int, multi2: int):
    await ctx.send(f"{multi1} * {multi2} = {multi1 * multi2}")
    print("command used 'muti'.")


@bot.command()
async def divide(ctx, divide1: int, divide2: int):
    if divide2 == 0:
        await ctx.send ("You fool. :smiling_imp: ")
        return
    await ctx.send(f"{divide1} / {divide2} = {divide1 / divide2}")
    print("command used 'divide'.")
    print(f"{divide1} / {divide2} = {divide1 / divide2}")


@bot.command()
async def sub(ctx, subt1: int, subt2: int):
    await ctx.send(f"{subt1}-{subt2} = {subt1-subt2}")
    print("command sub is used"+f"{subt1}-{subt2} = {subt1-subt2}")



@bot.command()
async def papa(ctx, b1 ):
    await ctx.send(b1)

@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.CommandError):
        await ctx.reply(f"oh noo! there is an error:  \n`{str(error)}`\nmessage the owner for support")
        print(error)


bot.run('')
