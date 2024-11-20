import asyncio
import discord

from discord import app_commands
from discord.ext import commands
from discord import Interaction

#-------------------------------------------------------------------------------------------------#
#------------------------------------------Bot-Handeling------------------------------------------#
#-------------------------------------------------------------------------------------------------#

class PowerOptions(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="shutdown", description="Shutdown the bot")
    async def shutdown(self, interaction: Interaction):
        if str(interaction.user) == 'shadowmaster6587':
            await interaction.response.send_message("Shutting down...", ephemeral=True)
            asyncio.sleep(10)
            await self.bot.close()

async def setup(bot):
    await bot.add_cog(PowerOptions(bot))