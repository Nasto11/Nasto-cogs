import os
import discord
from discord.ext import commands

class Embedsay:
    """Says stuff!"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command(pass_context=True)
    async def embedsay(ctx, self, message, *):
        """Says stuff!"""

        text = " ".join(text)
        author = ctx.message.author
        server = ctx.message.server

        if not user:
            user = author

        embed=discord.Embed(description=text, color=0xff00bb)
        embed.set_author(name='{} says', icon_url=author)
        await self.bot.delete_message(ctx.message)
        await self.bot.say(embed=embed)

def setup(bot):
    bot.add_cog(Embedsay(bot))