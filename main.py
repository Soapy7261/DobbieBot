import discord
from utils.data.getdata import info
info = info()
intents = discord.Intents.all()
bot = discord.Bot(debug_guilds=[955135608228024394],
    status=discord.Status.dnd,
    activity=discord.Activity(type=discord.ActivityType.playing,
    name="Booting..."),
    intents=intents)
bot.load_extensions("cogs")
global first
first = False
@bot.event
async def on_ready():
    global first
    embed = discord.Embed(title="🟢 Online!\nTime to mess around!", timestamp=discord.utils.utcnow(),
        color=discord.Color.green())
    await bot.get_guild(955135608228024394).get_channel(1011649871511572500).send(embed=embed)
    print(f"Ready! Logged in as {bot.user}")
    if first == True:
        await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, 
            name=f"my creator's keyboard | In {len(bot.guilds)} servers"), status=discord.Status.online)
        first = False

@bot.slash_command(description='Say hello', guild_ids=[955135608228024394])
async def hello(ctx):
    await ctx.respond(f"Hello {ctx.user.mention}!", ephemeral=True)

@bot.slash_command(description='Test command')
async def test(ctx):
    await ctx.send("te@st!")
    print("send command 'test!'")

@bot.slash_command(description="Say something through the bot")
async def say(ctx, message: discord.Option(str, description="The message to say")):
    await ctx.delete()
    await ctx.send(message)

@bot.event
async def on_command_error(ctx, error):
    await ctx.reply(f"An error occurred```py\n{str(error)}\n```Message the owner for support\nThis has been logged.")
    embed = discord.Embed(title="Error :(", timestamp=discord.utils.utcnow(), color=discord.Color.red())
    embed.add_field(name = "Error:", value=str(error))

    await bot.get_guild(955135608228024394).get_channel(1017880577506017361).send(embed=embed)

@bot.event
async def on_message(message):
    print ("message")
    print (message.content)
    if "dobbie" in message.content.lower():
        print('you got fans')
        #Add an eyes reaction
        await message.add_reaction("👀")
bot.run(info['Token'])
