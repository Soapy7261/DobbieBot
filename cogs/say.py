from discord import slash_command, Option, Embed, utils, Color
from discord.ext import commands
class Say(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Say cog loaded!')

    @slash_command(description="Say something through the bot")
    async def say(ctx, message: Option(str, description="The message to say")):
        await ctx.delete()
        embed = Embed(title="Message from " + ctx.user.name, description=message, timestamp=utils.utcnow(), color=Color.embed_background())
        embed.timestamp = utils.utcnow()
        await ctx.send(embed=embed)
        
def setup(bot):
    bot.add_cog(Say(bot))