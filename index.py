import discord
from discord.ext import commands
import os
from utils import help

client = commands.AutoShardedBot(
  command_prefix=commands.when_mentioned_or("!"),
  case_insensitive=True,
  intents=discord.Intents.all(),
  help_command=help.CustomHelpCommand()
)
for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')
    
  @client.event
  async def on_ready():
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game("!help | bot is WIP"))

client.load_extension("jishaku")
client.run("Nzg1OTEwOTA5NDMxMzE2NTYw.X8-ukg.gLsVteotBVwlkdpBitQZKgzR0xU")