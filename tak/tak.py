import discord
from discord.ext import commands
from .utils.dataIO import fileIO
from .utils import checks
from __main__ import send_cmd_help
from random import choice as rndchoice
import os
import time



def __init__(self, bot):
        self.bot = bot
        self.setowner_lock = False
		
		
@checks.is_owner()
async def animate(self, ctx):
        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)



async def _on(self, ctx, *, nickname=""):
        nickname = nickname.strip()
        if nickname == "":
            nickname = Dank Bot |Music on voice!
        try:
            await self.bot.change_nickname(ctx.message.server.me, nickname)
        except discord.Forbidden:
            await self.bot.say("I cannot do that, I lack the "
                "\"Change Nickname\" permission.")
	
	
	
async def _off(self, ctx, *, nickname=""):
        nickname = nickname.strip()
        if nickname == "":
            nickname = 
        try:
            await self.bot.change_nickname(ctx.message.server.me, nickname)
        except discord.Forbidden:
            await self.bot.say("I cannot do that, I lack the "
                "\"Change Nickname\" permission.")
		

