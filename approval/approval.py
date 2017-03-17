import os
import discord
from discord.ext import commands
import asyncio

class Approval:
    """"""

    def __init__(self, bot):
        self.bot = bot        
    async def listener(self, message):
        author = message.author
        server = author.server
        rolename = discord.utils.get(server.roles, name="Member")
        if message.content == "N0OB M3NU": 
            try:             
                await self.bot.add_roles(author, rolename)
                await self.bot.delete_message(message)
            except discord.Forbidden:
                pass
            except discord.HTTPException:
                pass

def setup(bot):
    n = Approval(bot)
    bot.add_listener(n.listener, 'on_message')
    bot.add_cog(n)