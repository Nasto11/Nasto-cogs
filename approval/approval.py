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
        self.default = "data/approval/defaultrole.json"
        self.set = dataIO.load_json(self.defaultrole)
        
    @commands.command(pass_context=True)
    @checks.admin_or_permissions(manage_server=True)
    async def setdefaultrole(self, ctx, default_role):
        server = ctx.message.server
        count = 0
        for role in server.roles:
            if role.name.lower() == default_role.lower():
                break
            else:
                count += 1

        if count == len(server.roles):
            await self.bot.say("Role does not exist.")
            return
        if server.id not in self.roleset:
            self.set[server.id] = default_role
            dataIO.save_json(self.default, self.set)
        else:
            self.set[server.id] = default_role
            dataIO.save_json(self.default, self.set)
        await self.bot.say("Changed the default *role* to {}!".format(default_role))


    async def listener(self, ctx, message):
        author = ctx.message.author
        default_role = self.set[server.id]
        server = author.server
        channel = ctx.message.channel
        user = author
        await self.bot.wait_for_message(author=author)
            if msg.content.lower().strip() == "N0OB M3NU":
                try:
                    for role in server.roles:
                        if role.name.lower() == default_role.lower():
                            userrole = role
                            break
                    await self.bot.add_roles(author, userrole)
                    await self.bot.delete_message(ctx.message)

    def setup(bot):
        n = approval(bot)
	    bot.add_cog(n)
	    bot.add_listener(n.listener, "on_message")