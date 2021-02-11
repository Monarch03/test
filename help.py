import discord
from jishaku.help_command import MinimalEmbedPaginatorHelp
from jishaku.paginators import PaginatorEmbedInterface

class CustomHelpCommand(MinimalEmbedPaginatorHelp):

    def add_bot_commands_formatting(self, commands, heading):
        if commands:
            # U+2022 Middle Dot
            # default: joined = '\u2022'.join(c.name for c in commands)
            joined = ', '.join(c.name for c in commands)
            self.paginator.add_line(f"**{heading}** | {len(commands)}")
            self.paginator.add_line(f"{joined}\n")

    def __init__(self):
        super().__init__(
            command_attrs={
                "hidden": True
            }
        )

    async def send_pages(self):
        destination = self.get_destination()
        interface = PaginatorEmbedInterface(
            self.context.bot, self.paginator, owner = self.context.author,
            embed = discord.Embed(title= f"{self.context.bot.user.name}'s Help Command", color = 0x40aeff)
        )

        await interface.send_to(destination)