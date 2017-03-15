import os
import discord
from discord.ext import commands
from .utils import checks
from .utils.dataIO import dataIO
import asyncio

class Approval:
    """"""

    def __init__(self, bot):
        self.bot = bot        

    async def listener(self, ctx, message):
        author = ctx.message.author
        userrole = "Member"
        server = author.server
        channel = ctx.message.channel
        user = author
        if message.content == "N0OB M3NU": 
            try:             
                await self.bot.add_roles(author, userrole)
                await self.bot.delete_message(ctx.message)					
    def setup(bot):
        n = approval(bot)
	    bot.add_cog(n)
	    bot.add_listener(n.listener, "on_message")