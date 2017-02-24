import discord
from discord.ext import commands
from .utils.dataIO import fileIO
from .utils import checks
from __main__ import send_cmd_help
import os
import time


class Musict:
    """Cycles random statuses
    If a custom status is already set, it won't change it until
    it's back to none. (!set status)"""

def __init__(self, bot):
        self.bot = bot
		
@commands.group(pass_context=True)	
@checks.is_owner()
async def music(self, ctx):
        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)

@commands.group(pass_context=True)
@checks.is_owner()
async def _on(self, ctx, *, nickname=""):
        nickname = nickname.strip()
        if nickname == "":
            nickname = "Dank Bot |Music on voice!"
        try:
            await self.bot.change_nickname(ctx.message.server.me, nickname)
        except discord.Forbidden:
            await self.bot.say("I cannot do that, I lack the "
                "\"Change Nickname\" permission.")
	

    @checks.is_owner()
    async def _off(self, ctx, *, nickname=""):
        """Sets Red's nickname
        Leaving this empty will remove it."""
        nickname = nickname.strip()
        if nickname == "":
            nickname = None
        try:
            await self.bot.change_nickname(ctx.message.server.me, nickname)
            await self.bot.say("Done.")
        except discord.Forbidden:
            await self.bot.say("I cannot do that, I lack the "
"\"Change Nickname\" permission.")
		

