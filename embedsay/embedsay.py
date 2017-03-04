import discord
from discord.ext import commands

class Embedsay:
    """Says stuff!"""

    def __init__(self, bot):
        self.bot = bot
        self.data = dataIO.load_json(JSON)

    @commands.command()
    async def embedsay(self):
        """Says stuff!"""

        text = " ".join(text)
        if author.id in self.data:
                    avatar = author.avatar_url if author.avatar else author.default_avatar_url
                    if self.data[author.id][text]:
                        em = discord.Embed(description=self.data[author.id][text], color=discord.Color.blue())
                        em.set_author(name='{} says'.format(author.display_name), icon_url=avatar)
                    else:
                        em = discord.Embed(color=discord.Color.blue())
                        em.set_author(name='{} says'.format(author.display_name), icon_url=avatar)
                    await self.bot.send_message(message.channel, embed=em)

def setup(bot):
    bot.add_cog(Embedsay(bot))