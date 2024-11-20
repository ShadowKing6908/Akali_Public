import discord
import random

from discord.ext import commands
from discord import app_commands
from discord import Interaction

#-------------------------------------------------------------------------------------------------#
#-----------------------------------------Actuall-commands----------------------------------------#
#-------------------------------------------------------------------------------------------------#


class Quotes(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="quotes", description="get a random Akali quote")
    async def quotes(self, interaction: Interaction):
        quote = ["Take one life at a time. Fast. Clean.", "Time to do what's gotta be done.", "The rules hold you back! Leave 'em for someone who needs 'em.", "Let's make this quick.", "We're gonna do this my way: quick, and deadly.", "Stay outta my way!", "Finally. Let's do this.", "I make problems... disappear."]
        await interaction.response.send_message(f"{random.choice(quote)}")

async def setup(bot):
    await bot.add_cog(Quotes(bot))