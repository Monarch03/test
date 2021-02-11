import discord
from discord.ext import commands
import random

class Moderation(commands.Cog):
    
    def __init__(self,client):
        self.client=client

    @commands.command()
    async def say(self, ctx, *, message):
        await ctx.message.delete()
        await ctx.send(message)

    @commands.command(aliases = ['pfp', 'av'])
    async def avatar(self, ctx, *, member: discord.Member = None):
        """ Get someones or your own avatar 
        """
        member = member or ctx.author
        gif_or_png = f'[PNG]({member.avatar_url_as(format="png")})' if not member.is_avatar_animated() else f'[GIF]({member.avatar_url_as(format="gif")})'
        av = discord.Embed(
            title = f"{member.name}'s Avatar",
            color = 0x40aeff,
            description = f'{gif_or_png} | '
                          f'[JPG]({member.avatar_url_as(format="jpg")}) | '
                          f'[WEBP]({member.avatar_url_as(format="webp")})'
        )
        av.set_image(url=member.avatar_url)

        await ctx.send(embed=av)

def setup(client):
    client.add_cog(Moderation(client))