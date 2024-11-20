import discord
import asyncio

from discord import Embed
from discord.ext import commands
from discord import app_commands
from discord import Interaction
from config.settings import VERSION

__version__ = VERSION


#-------------------------------------------------------------------------------------------------#
#-------------------------------------------Information-------------------------------------------#
#-------------------------------------------------------------------------------------------------#


class Information(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="information", description="give information about the bot")
    async def information(self,interaction: Interaction):
        if interaction.channel.type == discord.ChannelType.private:
            await interaction.response.send_message(f"""# Here is some information about the bot:
                                                        - Main Developer: <@727492625032020000> visit https://github.com/ShadowKing6908
                                                        - Bot name: Akali
                                                        - Ping: {int(self.bot.latency*1000)} ms
                                                        - Version: {(__version__)} \n""")
            try:
                while True:
                    await asyncio.sleep(10)
                    await interaction.edit_original_response(content=f"""# Here is some information about the bot:
                                                                        - Main Developer: <@727492625032020000> visit https://github.com/ShadowKing6908
                                                                        - Bot name: Akali
                                                                        - Ping: {int(self.bot.latency*1000)} ms
                                                                        - Version: {(__version__)} \n""")
            except KeyboardInterrupt:
                await interaction.edit_original_response(content=f"""# Here is some information about the bot:
                                                                    - Main Developer: <@727492625032020000> visit https://github.com/ShadowKing6908
                                                                    - Bot name: Akali
                                                                    - Ping: bot is currently offline 
                                                                    - Version: {(__version__)} \n""")   
                while True:
                    await asyncio.sleep(10)
                    await interaction.edit_original_response(content=f"""# Here is some information about the bot:
                                                                        - Main Developer: <@727492625032020000> visit https://github.com/ShadowKing6908
                                                                        - Bot name: Akali
                                                                        - Ping: {int(self.bot.latency*1000)} ms
                                                                        - Version: {(__version__)} \n""")
        else:
            await interaction.response.send_message(f"""# Here is some information about the bot:
                                                        - Main Developer: <@727492625032020000> visit https://github.com/ShadowKing6908
                                                        - Bot name: Akali
                                                        - Ping: {int(self.bot.latency*1000)} ms
                                                        - Version: {(__version__)} \n""", ephemeral=True)

    @app_commands.command(name="readme", description="prints the README.md file")
    async def readme(self, interaction: Interaction):
        await interaction.response.send_message(file=discord.File(r'README.md'))

    @app_commands.command(name="ping", description="prints the ping of the bot")
    async def ping(self, interaction: Interaction):
        await interaction.response.send_message(f'Pong! {int(self.bot.latency*1000)} ms')

async def setup(bot):
    await bot.add_cog(Information(bot))