import os
import discord
from discord.ext import commands
from discord.ext.commands import slash_command
from discord.errors import ExtensionAlreadyLoaded, ExtensionNotLoaded, ExtensionFailed
from utils import Utils
class Cogs(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.info = Utils.info()

    @commands.Cog.listener()
    async def on_ready(self):
        print('Cogs cog loaded!')

    @slash_command(description='Load, unload, or reload cogs', guild_ids=[955135608228024394])
    async def cogs(self, ctx, action: discord.Option(choices=["Reload", "Load", "Unload"], description='What action to run', required=True), cog: discord.Option(autocomplete=Utils.get_cogs, description='The cog to run the action on', required=True)):
        if ctx.author.id != int(self.info['OwnerID']):
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
        except ExtensionAlreadyLoaded:
            await ctx.respond("Extension already loaded!", ephemeral=True)
            return
        except ExtensionNotLoaded:
            await ctx.respond("Extension not loaded!", ephemeral=True)
            return
        except ExtensionFailed as error:
            await ctx.respond(f"Extension failed to load!```py\n{str(error)}\n```", ephemeral=True)
            return
        await ctx.respond(f"{action}ed {cog}", ephemeral=True)

def setup(bot):
    bot.add_cog(Cogs(bot))
