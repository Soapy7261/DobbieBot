from discord import slash_command, Embed, utils, Color
from discord.ext import commands
class BotInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('BotInfo cog loaded!')

    @slash_command(description='Get info about the bot')
    async def botinfo(self, ctx):
        embed = Embed(
            title="DobbieBot",
            description = "The Dobbie bot",
            timestamp=utils.utcnow(),
            color=Color.embed_background())
        embed.add_field(name="Ping:",value=round(self.bot.latency * 1000, 2) + "ms")
        embed.add_field(name="Info about the bot",
            value="""this bot is made by Soapy7261#7261
            and Dobbie#4778. To teach Dobbie how 
            Discord bots work and how py-cord works!""")

        embed.add_field(name="Main commands", value="/math\n/info")
        embed.add_field(name="Github", value="https://github.com/Soapy7261/DobbieBot")
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(BotInfo(bot))
