from asyncio import sleep as asyncsleep
import discord
from discord.ext.commands import slash_command
from discord.ext import commands
from utils import Utils
class Reload(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.info = Utils.info()

    @commands.Cog.listener()
    async def on_ready(self):
        print('Reload cog loaded!')

    @slash_command(description='Only the owner of the bot can run this command', guild_ids=[955135608228024394])
    async def reload(self, ctx):
        if ctx.author.id != int(self.info['OwnerID']):
            return await ctx.respond("You don't have permission to use this command!", ephemeral=True)
        await ctx.defer()
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f"Reloading commands, bot may be unresponsive | In {len(self.bot.guilds)} servers"), status=discord.Status.dnd)
        await asyncsleep(1)
        try:
            await self.bot.sync_commands()
        except Exception as error:
            await ctx.respond ("Failed to reload commands!")
            await ctx.respond ("```py\n" + str(error) + "\n```", ephemeral=True)
            await asyncsleep(3)
            return await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"my creator's keyboard | In {len(self.bot.guilds)} servers"), status=discord.Status.online)
        await asyncsleep(3)
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"my creator's keyboard | In {len(self.bot.guilds)} servers"), status=discord.Status.online)
        return await ctx.respond("Finished!", ephemeral=True)

def setup(bot):
    bot.add_cog(Reload(bot))
