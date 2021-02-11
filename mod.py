import discord
from discord.ext import commands
import random

class MemberID(commands.Converter):
    async def convert(self, ctx, argument):
        try:
            m = await commands.MemberConverter().convert(ctx, argument)
        except commands.BadArgument:
            try:
                return int(argument, base = 10)
            except ValueError:
                raise commands.BadArgument(f"{argument} is not a valid member or member ID.") from None
        else:
            return m.id

class Moderation(commands.Cog):
    
    def __init__(self,client):
        self.client=client

    @commands.has_guild_permissions(kick_members=True)
    @commands.command()
    async def kick(self, ctx, member: discord.Member, *, reason=None):
        await member.kick(reason=reason)
        await ctx.send(f"{member.mention} was kicked cos dey noty noty")

    @commands.has_guild_permissions(ban_members=True)
    @commands.command()
    async def ban(self, ctx, member: MemberID, *, reason=None):
        member = await self.client.fetch_user(member)
        messages = [f"**{member.name}** was banned cos dey are have sinnned >:(", f"**{member.name}** was banned cos dey noty as freak", f"**{member.name}** was banned cos dey are big dingus"]
        await ctx.guild.ban(discord.Object(member.id), reason=reason)
        await ctx.send(random.choice(messages))

    @commands.command()
    async def unban(self, ctx, member: MemberID, *, reason=None):
        member = await self.client.fetch_user(member)
        messages = [f"**{member.name}** was unbanned cos dey are have mercy :)", f"**{member.name}** was unbanned cos dey lucky as freak"]
        if member == ctx.author.id:
            return await ctx.send('You can\'t unban yourself')

        await ctx.guild.unban(discord.Object(id=member.id), reason=reason)
        await ctx.send(random.choice(messages))

    @commands.command()
    async def clear(self, ctx, amount=5):
        await ctx.channel.purge(limit=amount+1)
        await ctx.send("teh fings got smooshed", delete_after=3)

    @commands.has_guild_permissions(manage_messages=True)
    @commands.command()
    @commands.guild_only()
    async def mute(self, ctx, member: discord.Member, *, reason=None):
        mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

        if not mutedRole:
            mutedRole = await ctx.guild.create_role (name="Muted")

            for channel in ctx.guild.channels:
                await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=True)

        await member.add_roles(mutedRole, reason=reason)
        await ctx.send(f"Muted {member.mention} for reason {reason}")
        await member.send(f"noob you got muted in the server called {ctx.guild.name} for {reason}")

    @commands.has_guild_permissions(manage_messages=True)
    @commands.command()
    @commands.guild_only()
    async def unmute(self, ctx, member: discord.Member, *, reason=None):
        mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

        if not mutedRole:
            return await ctx.send("dis server got no mooted role in existence. set one up idiot")

        await member.remove_roles(mutedRole, reason=reason)
        await ctx.send(f"Unmuted {member.mention} for reason {reason}")
        await member.send(f"haha noob you got moooooted in {ctx.guild.name} for {reason}. be not noty noty next time.")

def setup(client):
    client.add_cog(Moderation(client))