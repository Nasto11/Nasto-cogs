import os
import discord
from discord.ext import commands

class Embedsay:
    """Says stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def embedsay(self, message, ctx, *text):
        """Says stuff!"""

        text = " ".join(text)
        embed=discord.Embed(title="says", description=text, color=0xff00bb)
        embed.set_author(name='{} says'.format(author.display_name), icon_url=avatar)
        await self.bot.delete_message(ctx.message)
        await self.bot.say(embed=embed)

def setup(bot):
bot.add_cog(Embedsay(bot))