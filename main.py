import discord
from discord import message
from discord.ext import commands
import os
import dotenv
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(debug_guilds=[955135608228024394], command_prefix="-", status=discord.Status.dnd,
                   activity=discord.Activity(type=discord.ActivityType.listening, name="keyboard noises"),
                   owner='820255805257023498', intents=intents, )


@bot.listen()
async def on_ready():
    print("Now ready!")
    embed = discord.Embed(title=":green_circle: Online!\nTime to mess around!", timestamp=discord.utils.utcnow(),
                          color=0x00ff00, )
    await bot.get_guild(955135608228024394).get_channel(1011649871511572500).send(embed=embed)


@bot.hybrid_command()
async def hello(ctx):
    await ctx.reply("Hello!")
    print("send command 'hello'.")


@bot.command()
async def hello_hi(ctx):
    embed = discord.Embed(title="embed works", timestamp=discord.utils.utcnow(), color=0x00ff55, )
    await ctx.send(embed=embed)


@bot.command()
async def test(ctx):
    await ctx.send("te@st!")
    print("send command 'test!'")


@bot.command()
async def add(ctx, add1: int, add2: int):
    add.thing='this command is now merged in to the -call command use `-call', add1 ,  add2, ' and then whitout those stupid marks'
    await ctx.send (add.thig)
    print("command used 'add'.")


@bot.command()
async def multi(ctx, multi1: int, multi2: int):
    await ctx.send(f"{multi1} * {multi2} = {multi1 * multi2}")
    print("command used 'muti'.")


@bot.command()
async def divide(ctx, divide1: int, divide2: int):
    if divide2 == 0:
        await ctx.send("You fool. :smiling_imp: ")
        return
    await ctx.send(f"{divide1} / {divide2} = {divide1 / divide2}")
    print("command used 'divide'.")
    print(f"{divide1} / {divide2} = {divide1 / divide2}")


@bot.command()
async def sub(ctx, subt1: int, subt2: int):
    await ctx.send(f"{subt1}-{subt2} = {subt1 - subt2}")
    print("command sub is used" + f"{subt1}-{subt2} = {subt1 - subt2}")


@bot.command()
async def papa(ctx, *, b1):
    await ctx.send(b1)
@bot.command()
async def cal(ctx,nr1: int, mark, nr2:int ):

    if mark==("+"):
        calcu=(f"{nr1}+{nr2} = {nr1 + nr2}")
    if mark==('-'):
        calcu=(f"{nr1}-{nr2} = {nr1 - nr2}")
    if mark==('*', 'x'):
        if nr2!= 0:
            calcu=(f"{nr1} {mark} {nr2} = {nr1 * nr2}")
    else:
        calcu=("0 what did you hope for?")
    if mark== '/':
        if nr2 !=0:
            calcu=(f"{nr1}/{nr2} = {nr1 / nr2}")
        else:
            calcu=("you fool!")



    embed=discord.Embed(title='calculation',timestamp=discord.utils.utcnow(),color=0x00ff00,)
    embed.add_field(name='your calculation is here!', value=calcu)
    await ctx.send(embed=embed)
    print('command cal runned; '+calcu)
    calcu=("n")





@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, discord.ext.commands.CommandError):
        await ctx.reply(f"oh noo! there is an error:  \n`{str(error)}`\nmessage the owner for support")
        embed = discord.Embed(title="Error :(", timestamp=discord.utils.utcnow(),color=0xff0000, )
        #embed.add_field(name = "Author:", value=message.author)
        #embed.add_field(name = "Author ID:", value = message.author.id)
        embed.add_field(name = "Error:", value=str(error))

        await bot.get_guild(955135608228024394).get_channel(1017880577506017361).send(embed=embed)

bot.run(os.getenv('TOKEN'))
