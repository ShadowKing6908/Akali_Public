import discord
from discord import Interaction, ui, Embed, Color
from discord.ext import commands
from discord import app_commands


#-------------------------------------------------------------------------------------------------#
#--------------------------------------------DM-Secion--------------------------------------------#
#-------------------------------------------------------------------------------------------------#


class DMsExtension(commands.Cog):
    def __init__(self, bot):
        self.bot = bot


    @app_commands.command(name="shadow", description="this is a command, only for a specific person")
    async def shadow(self, interaction: Interaction, member: discord.Member):
        if str(interaction.user) == 'shadowmaster6587':
            channel = await member.create_dm()
            embed = Embed(title = "Chat with me in your DMs!", color = Color.blue())
            await channel.send(embed = embed, view = DMsLauncher())
        else:
            await interaction.response.send_message("did you not read the description? ur obviously are not it :P", ephemeral=True)

    @app_commands.command(name="cleardms", description="Clear the bot's messages in your DMs")
    async def cleardms(self, interaction: Interaction):
        try:
            # Create a DM channel with the user
            channel = await interaction.user.create_dm()
            
            # Defer the response to give the bot time to process
            await interaction.response.defer(ephemeral=True)
            
            # Iterate over the messages in the DM channel
            async for message in channel.history(limit=None):
                # Check if the message is from the bot
                if message.author == self.bot.user:
                    await message.delete()
            
            # Send a confirmation message
            await interaction.followup.send("All bot messages in your DMs have been deleted.", ephemeral=True)
        except Exception as e:
            # Handle any exceptions and inform the user
            await interaction.followup.send(f"An error occurred: {str(e)}", ephemeral=True)

    @app_commands.command(name="cleardmsamount", description="Clear a specific amount of messages in your DMs")
    async def cleardmsamount(self, interaction: Interaction, amount: int):
        try:
            # Create a DM channel with the user
            channel = await interaction.user.create_dm()
            
            # Defer the response to give the bot time to process
            await interaction.response.defer(ephemeral=True)
            
            # Iterate over the messages in the DM channel
            async for message in channel.history(limit=amount):
                # Check if the message is from the bot
                if message.author == self.bot.user:
                    await message.delete()
            
            # Send a confirmation message
            await interaction.followup.send(f"All bot messages in your DMs have been deleted.", ephemeral=True)
        except Exception as e:
            # Handle any exceptions and inform the user
            await interaction.followup.send(f"An error occurred: {str(e)}", ephemeral=True)

class DMsLauncher(ui.View):

    def __init__(self) -> None:
        super().__init__(timeout = None)
        
    @discord.ui.button(label = "DM Bot Launch", style = discord.ButtonStyle.blurple, custom_id = "dms_button")
    async def dms(self, interaction: discord.Interaction, button: discord.ui.Button):
            embed = discord.Embed(description=f"Hallo {interaction.user}! Nice that you choose to chat with me!")
            embed.set_author(name=f"{interaction.user}", icon_url=f"{interaction.user.display_avatar}")
            embed.set_footer(text="I'll be right here for you!")
            await interaction.response.send_message(embed=embed, ephemeral=True)

async def setup(bot):
    await bot.add_cog(DMsExtension(bot))

