import discord
from discord import slash_command, commands
from utils.helpers.getbranches import GetBranches
from utils.data.getdata import info
class Branch(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.info = info()

    @commands.Cog.listener()
    async def on_ready(self):
        print('Branch cog loaded!')

    @slash_command(description='Only the owner of the bot can run this command', guild_ids=[955135608228024394])
    async def branch(self, ctx, branch: discord.Option(autocomplete=GetBranches, description='What branch to switch to', required=True)):
        if ctx.interaction.user.id != int(self.info['OwnerID']):
            return await ctx.respond("You don't have permission to use this command!", ephemeral=True)
        await ctx.respond(f'You selected {branch}', ephemeral=True)

def setup(bot):
    bot.add_cog(Branch(bot))
