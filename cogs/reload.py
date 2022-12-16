import discord
from discord import slash_command, commands, asyncio
from utils.data.getdata import info
info = info()
class Reload(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Reload cog loaded!')

    @slash_command(description='Only the owner of the bot can run this command', guild_only=True)
    async def reload(self, ctx):
        if ctx.author.id != int(info['OwnerID']):
            return await ctx.respond("You don't have permission to use this command!", ephemeral=True)
        await ctx.defer()
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=f"Reloading commands, bot may be unresponsive | In {len(self.bot.guilds)} servers"), status=discord.Status.dnd)
        await asyncio.sleep(1)
        try:
            await self.bot.sync_commands()
        except Exception as e:
            await ctx.respond ("Failed to reload commands!")
            await ctx.respond ("```py\n" + str(e) + "\n```", ephemeral=True)
        await asyncio.sleep(3)
        await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"my creator's keyboard | In {len(self.bot.guilds)} servers"), status=discord.Status.online)
        return await ctx.respond("Finished!", ephemeral=True)

def setup(bot):
    bot.add_cog(Reload(bot))
