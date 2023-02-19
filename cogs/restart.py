import discord
from discord.ext.commands import slash_command
from discord.ext import commands
from utils import Utils
class Restart(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.info = Utils.info()

    @commands.Cog.listener()
    async def on_ready(self):
        print('Restart cog loaded!')

    @slash_command(description="Restart the bot", guild_ids=[955135608228024394])
    async def restart(self, ctx):
        if ctx.author.id != int(self.info['OwnerID']):
            return await ctx.respond("You don't have permission to use this command!", ephemeral=True)
        await ctx.respond("Restarting.")
        embed = discord.Embed(title="🔄 Restarting...", timestamp=discord.utils.utcnow(), color=discord.Color.orange())
        await self.bot.get_guild(955135608228024394).get_channel(1048306173071347782).send(embed=embed)
        await self.bot.close()

def setup(bot):
    bot.add_cog(Restart(bot))
