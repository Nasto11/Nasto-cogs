import discord
from discord.ext import commands
from cogs.utils import checks
from __main__ import set_cog
from .utils.dataIO import dataIO
from .utils.chat_formatting import pagify, box

import importlib
import traceback
import logging
import asyncio
import threading
import datetime
import glob
import os
import aiohttp


class Music:
    """Changes nickname when command is used"""

def __init__(self, bot):
        self.bot = bot
        self.setowner_lock = False
        self.file_path = "data/red/disabled_commands.json"
        self.disabled_commands = dataIO.load_json(self.file_path)
        self.session = aiohttp.ClientSession(loop=self.bot.loop)
				
@commands.group(pass_context=True)		
@checks.is_owner()
async def music(self, ctx):
        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)

@music.command(pass_context=True)
@checks.is_owner()
async def _on(self, ctx, *, nickname=""):
        nickname = nickname.strip()
        if nickname == "Dank Bot |Music on voice!":
            nickname = "Dank Bot |Music on voice!"
        try:
            await self.bot.change_nickname(ctx.message.server.me, nickname)
        except discord.Forbidden:
            await self.bot.say("I cannot do that, I lack the "
                "\"Change Nickname\" permission.")
	
@music.command(pass_context=True)	
@checks.is_owner()	
async def _off(self, ctx, *, nickname=""):
        nickname = nickname.strip()
        if nickname == "":
            nickname = None
        try:
            await self.bot.change_nickname(ctx.message.server.me, nickname)
        except discord.Forbidden:
            await self.bot.say("I cannot do that, I lack the "
                "\"Change Nickname\" permission.")

def setup(bot):
    bot.add_cog(Music(bot))

