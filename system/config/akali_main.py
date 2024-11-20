import discord

from discord import app_commands
from discord.ext.commands import Bot
from discord.ext import commands

from config.cog_register import cogs
from config.settings import VERSION, APP_ID

__version__ = VERSION
__application_id__ = APP_ID


#-------------------------------------------------------------------------------------------------#
#--------------------------------------------Bot-main---------------------------------------------#
#-------------------------------------------------------------------------------------------------#


class AkaliBot(Bot):

    def __init__(self):
        intents = discord.Intents.all()
        intents.message_content = True
        super().__init__(command_prefix='!', intents=intents)

    async def on_ready(self):

        for cog in cogs:
            await self.load_extension(cog)

        await self.change_presence(activity=discord.Game("Quick and Deadly"), status=discord.Status.online)
        
        print("Logged in as")
        print(self.user.name)
        print(__version__)
        print(__application_id__)
        print("------")

    #@bot.event   
    #async def on_member_join(member):
    #    channel = discord.utils.get(member.guild.channels, name='welcome')
    #    embed = create_embed(member)
    #    await channel.send(embed=embed)   
    #
    #def create_embed(member):
    #    embed = Embed(title=f'{member.name} joined', description="Someone appeared here...", color=0x444444)
    #    embed.add_field(name='Welcome here', value=f"Hello {member.name}, let's hope you survive long enough...", inline=True)
    #    embed.set_thumbnail(url='https://images.app.goo.gl/4Whhn6QKnhp3P1cR8')
    #    embed.set_image(url=member.display_avatar)
    #    return embed
    #
    #@bot.event
    #async def on_member_remove(member):
    #    channel = discord.utils.get(member.guild.channels, name='bye')
    #    await channel.send(f'{member.name} just disappeared in a smoke...')
