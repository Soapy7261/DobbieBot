from discord import Bot, Intents, Status, Activity, ActivityType, Embed, Color, utils
from utils import Utils
info = Utils.info()
intents = Intents.all()
bot = Bot(debug_guilds=[955135608228024394], status=Status.dnd, activity=Activity(type=ActivityType.playing, name="Booting..."), intents=intents)
bot.load_extensions("cogs")
BOOTED = True

@bot.listen()
async def on_ready():
    global BOOTED
    if BOOTED is False:
        print ("Reconnected(?)")
    if BOOTED is True:
        embed = Embed(title="🟢 Online!\nTime to mess around!", timestamp=utils.utcnow(),
            color=Color.green())
        await bot.get_guild(955135608228024394).get_channel(1011649871511572500).send(embed=embed)
        await bot.change_presence(activity=Activity(type=ActivityType.listening,
            name=f"my creator's keyboard | In {len(bot.guilds)} servers"), status=Status.online)
        print(f"Ready! Logged in as {bot.user}")
        BOOTED = False

@bot.slash_command(description='Say hello', guild_ids=[955135608228024394])
async def hello(ctx):
    await ctx.respond(f"Hello {ctx.user.mention}!", ephemeral=True)

@bot.slash_command(description='Test command')
async def test(ctx):
    await ctx.send("te@st!")
    print("send command 'test!'")

@bot.listen()
async def on_command_error(ctx, error):
    await ctx.reply(f"An error occurred```py\n{str(error)}\n```Message the owner for support\nThis has been logged.")
    embed = Embed(title="Error :(", timestamp=utils.utcnow(), color=Color.red())
    embed.add_field(name = "Error:", value=str(error))

    await bot.get_guild(955135608228024394).get_channel(1017880577506017361).send(embed=embed)

@bot.listen()
async def on_message(message):
    print ("message")
    print (message.content)
    if "dobbie" in message.content.lower():
        print('you got fans')
        #Add an eyes reaction
        await message.add_reaction("👀")
bot.run(info['Token'])
