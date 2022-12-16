import discord
from discord import slash_command, commands
class BotInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('BotInfo cog loaded!')

    @slash_command(description='Get info about the bot')
    async def botinfo(self, ctx):
        embed = discord.Embed(
            title="DobbieBot",
            description = "The Dobbie bot",
            timestamp=discord.utils.utcnow(),
            color=discord.Color.dark_gray())
        embed.add_field(name="Ping",value=(round(self.bot.latency * 1000)))
        embed.add_field(name="Info about the bot",
            value="""this bot is made by Soapy7261#8558
            and Dobbie#4778. To teach Dobbie how 
            Discord bots work and how py-cord works!""")

        embed.add_field(name="Main commands", value="/math\n/info")
        await ctx.respond(embed=embed)
        
def setup(bot):
    bot.add_cog(BotInfo(bot))