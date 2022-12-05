import os, discord
from discord import slash_command, commands
from utils.helpers.getcogs import getcogs
from utils.data.getdata import info
info = info()
class Cogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Cogs cog loaded!')

    @slash_command(description='Load, unload, or reload cogs', guild_only=True)
    async def cogs(self, ctx, action: discord.Option(choices=["Reload", "Load", "Unload"], description='What action to run', required=True), cog: discord.Option(autocomplete=getcogs, description='The cog to run the action on', required=True)):
        if ctx.author.id != int(info['OwnerID']):
            return await ctx.respond("You don't have permission to use this command!", ephemeral=True)
        if cog not in [f"{fn[:-3]}" for fn in os.listdir("commands")]:
            await ctx.respond("That cog doesn't exist!", ephemeral=True)
            return
        await ctx.defer(ephemeral=True)
        try:
            if action == "Load":
                self.bot.load_extension(f"commands.{cog}")
            if action == "Unload":
                self.bot.unload_extension(f"commands.{cog}")
            if action == "Reload":
                self.bot.reload_extension(f"commands.{cog}")
        except Exception as e:
            await ctx.respond(f"```py\n{e}\n```", ephemeral=True)
            return
        await ctx.respond(f"{action}ed {cog}", ephemeral=True)

def setup(bot):
    bot.add_cog(Cogs(bot))
