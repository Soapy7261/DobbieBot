import discord
from discord.ext import commands
from discord.ext.commands import slash_command
from utils import Utils
class Branch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.info = Utils.info()

    @commands.Cog.listener()
    async def on_ready(self):
        print('Branch cog loaded!')

    @slash_command(description='Only the owner of the bot can run this command', guild_ids=[955135608228024394])
    async def branch(self, ctx, branch: discord.Option(autocomplete=Utils.GetBranches, description='What branch to switch to', required=True)):
        if ctx.interaction.user.id != int(self.info['OwnerID']):
            return await ctx.respond("You don't have permission to use this command!", ephemeral=True)
        await ctx.respond(f'You selected {branch}', ephemeral=True)

def setup(bot):
    bot.add_cog(Branch(bot))
