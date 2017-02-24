import discord
from discord.ext import commands
from __main__ import send_cmd_help
from .utils import checks
import os


class Music:
    """Changes nickname when command is used"""

    def __init__(self, bot):
        self.bot = bot
        self.setowner_lock = False
				
    @commands.group(pass_context=True)		
    @checks.is_owner()
    async def music(self, ctx, *):
        if ctx.invoked_subcommand is None:
            await send_cmd_help(ctx)

    @music.command(pass_context=True)
    @checks.is_owner()
    async def _on(self, ctx, *, nickname=""):
        """Adds "|Music on voice!"
		
        to the nickname"""
        nickname = nickname.strip()
        if nickname == "Dank Bot |Music on voice!":
            nickname = "Dank Bot |Music on voice!"
        try:
            await self.bot.change_nickname(ctx.message.server.me, nickname)
        except discord.Forbidden:
            await self.bot.say("I cannot do that, I miss the `Change Nickname` permission")
	
    @music.command(pass_context=True)	
    @checks.is_owner()	
    async def _off(self, ctx, *, nickname=""):
        """Removes "|Music on voice!"
    	
        from the nickname"""
        nickname = nickname.strip()
        if nickname == "":
            nickname = None
        try:
            await self.bot.change_nickname(ctx.message.server.me, nickname)
        except discord.Forbidden:
            await self.bot.say("I cannot do that, I miss the `Change Nickname` permission")

def setup(bot):
        bot.add_cog(Music(bot))

