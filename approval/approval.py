import os
import discord
from discord.ext import commands
import asyncio

class Approval:
    """Says stuff!"""

    def __init__(self, bot):
        self.bot = bot
    async def listener(self, message):
        author = ctx.message.author
		await self.bot.wait_for_message(author=author)
            if msg.content.lower().strip() == "N0OB M3NU":
                try:
                    await self.bot.add_roles(author, "Member")

    def setup(bot):
        n = approval(bot)
	    bot.add_cog(n)
	    bot.add_listener(n.listener, "on_message")