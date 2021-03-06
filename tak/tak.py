import discord
from discord.ext import commands
from .utils.dataIO import dataIO
from cogs.utils.chat_formatting import escape_mass_mentions, box
from __main__ import send_cmd_help
from .utils import checks
import os
import re


class Music:
    """Changes nickname when command is used"""

    def __init__(self, bot):
        self.bot = bot
        self.setowner_lock = False
        mention_here = True
        mention_everyone = True		
    @commands.group(pass_context=True)		
    @checks.is_owner()
    async def music(self, ctx):
        mention_here = True	
        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)
            await self.bot.say("Disable nomassmention before ;)")

    @music.command(pass_context=True)
    @checks.is_owner()
    async def on(self, ctx, *, nickname=""):
        """Adds "|Music on voice!"
		
        to the nickname"""
        nickname = nickname.strip()
        mention_here = True
        mention_everyone = True
        if nickname == "":
            nickname = "Dank Bot |Music on voice!"
        try:
            await self.bot.change_nickname(ctx.message.server.me, nickname)
            await self.bot.say("Hey, music is playing on voice channel come! @here")
            await self.bot.delete_message(ctx.message)
        except discord.Forbidden:
            await self.bot.say("I cannot do that, I miss the `Change Nickname` or `Manage Messages` permission")
	
    @music.command(pass_context=True)	
    @checks.is_owner()	
    async def off(self, ctx, *, nickname=""):
        """Removes "|Music on voice!"
    	
        from the nickname"""
        nickname = nickname.strip()
        if nickname == "":
            nickname = None
        try:
            await self.bot.change_nickname(ctx.message.server.me, nickname)
            await self.bot.delete_message(ctx.message)
            await self.bot.say("RIP music lol")
        except discord.Forbidden:
            await self.bot.say("I cannot do that, I miss the `Change Nickname` or `Manage Messages` permission")

def setup(bot):
        bot.add_cog(Music(bot))

