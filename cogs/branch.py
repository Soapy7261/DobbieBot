import discord
from discord import slash_command, commands
from utils.helpers.getbranches import GetBranches
from utils.data.getdata import info
info = info()
class Branch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Branch cog loaded!')

    @slash_command(description='Only the owner can use this command', guild_only=True)
    async def branch(self, ctx, branch: discord.Option(autocomplete=GetBranches, description='What branch to switch to', required=True)):
        if ctx.interaction.user.id != int(info['OwnerID']):
            return await ctx.respond("You don't have permission to use this command!", ephemeral=True)
        await ctx.respond(f'You selected {branch}', ephemeral=True)

def setup(bot):
    bot.add_cog(Branch(bot))
