import discord
from discord.ext import commands
from .utils.dataIO import dataIO

class Embedsay:
    """Says stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def autism(self):
    """Says stuff!"""
        embed=discord.Embed(title="Im saying", url='http://youhaveautism.com/', description="that u have autism ", color=0x0080ff)
        await self.bot.say(embed=embed)

def setup(bot):
    bot.add_cog(Embedsay(bot))