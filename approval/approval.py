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
        self.defaultrole = "data/approval/defaultrole.json"
        self.roleset = dataIO.load_json(self.defaultrole)
        

    def setdefaultrole(self, ctx, default_role):
        server = ctx.message.server
        count = 0
        for role in server.roles:
            if role.name.lower() == default_role.lower():
                break
            else:
                count += 1
        if count == len(server.roles):
            await self.bot.say("Role does not exist on this server. Please try again.")
            return
        if server.id not in self.roleset:
            self.roleset[server.id] = default_role
            dataIO.save_json(self.defaultrole, self.roleset)
        else:
            self.roleset[server.id] = default_role
            dataIO.save_json(self.defaultrole, self.roleset)
        await self.bot.say("Default role is now *role*!")

    async def listener(self, message):
        author = ctx.message.author
        await self.bot.wait_for_message(author=author)
            if msg.content.lower().strip() == "N0OB M3NU":
                try:
                    for role in server.roles:
                        if role.name.lower() == default_role.lower():
                            userrole = role
                            break
                    await self.bot.add_roles(author, userrole)

    def setup(bot):
        n = approval(bot)
	    bot.add_cog(n)
	    bot.add_listener(n.listener, "on_message")