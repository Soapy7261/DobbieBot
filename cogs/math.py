from discord import slash_command, commands
import discord
class Math(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print('Math cog loaded!')

    @slash_command(description="Run a calculation")
    async def math(self, ctx, first: discord.Option(float, description="The first number"), second: discord.Option(float, description="The second number"), operation: discord.Option(description="What operation you want to run", choices=["+", "-", "*", "/"])):
        if operation == '+':
            oper = first + second
        if operation == '-':
            oper = first - second
        if operation == '*':
            oper = first * second
        if operation == '/':
            if second == 0:
                return await ctx.respond("You can't divide by 0!", ephemeral=True)
            oper = first / second
        embed=discord.Embed(title='Calculation', timestamp=discord.utils.utcnow(), color=discord.Color.green())
        embed.add_field(name='Your calculation is here!', value=f"{first}{operation}{second} = {oper}")
        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Math(bot))
