import discord

from discord import Color
from discord import Embed
from discord.ext import commands
from discord import app_commands
from discord import Interaction


#-------------------------------------------------------------------------------------------------#
#----------------------------------------------Builds---------------------------------------------#
#-------------------------------------------------------------------------------------------------#


class Build(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="shadowbuild", description="Get one of Shadow's own builds")
    async def shadowbuild(interaction: Interaction, lane: str, role: str):
        builds = {
            "top": {
                "ap": {
                    "items": [
                        {"name": "Sorcerer's Shoes", "icon": "https://static.wikia.nocookie.net/leagueoflegends/images/b/bb/Sorcerer%27s_Shoes_item_HD.png/revision/latest/scale-to-width-down/64?cb=20240915180245"},
                        {"name": "Stormsurger", "icon": "https://example.com/stormsurger.png"},
                        {"name": "Lichbane", "icon": "https://example.com/lichbane.png"},
                        {"name": "Zhonya's Hourglass", "icon": "https://example.com/zhonyas_hourglass.png"},
                        {"name": "Mejai's Soulstealer", "icon": "https://example.com/mejais_soulstealer.png"},
                        {"name": "Rabadon's Deathcap", "icon": "https://example.com/rabadons_deathcap.png"}
                    ],
                    "runes_pri": [
                        {"name": "Electrocute", "icon": "https://example.com/electrocute.png"},
                        {"name": "Sudden Impact", "icon": "https://example.com/sudden_impact.png"},
                        {"name": "Eyeball Collection", "icon": "https://example.com/eyeball_collection.png"},
                        {"name": "Ultimate Hunter", "icon": "https://example.com/ultimate_hunter.png"}
                    ],
                    "runes_sec": [
                        {"name": "Second Wind", "icon": "https://example.com/second_wind.png"},
                        {"name": "Overgrow", "icon": "https://example.com/overgrow.png"}
                    ],
                    "runes_ext": [
                        {"name": "Adaptive Force", "icon": "https://example.com/adaptive_force.png"},
                        {"name": "Adaptive Force", "icon": "https://example.com/adaptive_force.png"},
                        {"name": "Health", "icon": "https://example.com/health.png"}
                    ]
                }
            }
        }

        build = builds.get(lane, {}).get(role, None)
        if not build:
            await interaction.response.send_message("Build not found for the specified lane and role.", ephemeral=True)
            return
        
        embed = Embed(title=f"Shadow's {lane.capitalize()} {role.upper()} Build", color=Color.dark_teal())
        
        for item in build["items"]:
            embed.add_field(name=item["name"], value="\u200b", inline=True)
            embed.set_thumbnail(url=item["icon"])
        
        embed.add_field(name="Primary Runes", value="\u200b", inline=False)
        for rune in build["runes_pri"]:
            embed.add_field(name=rune["name"], value="\u200b", inline=True)
            embed.set_thumbnail(url=rune["icon"])
        
        embed.add_field(name="Secondary Runes", value="\u200b", inline=False)
        for rune in build["runes_sec"]:
            embed.add_field(name=rune["name"], value="\u200b", inline=True)
            embed.set_thumbnail(url=rune["icon"])
        
        embed.add_field(name="Extended Runes", value="\u200b", inline=False)
        for rune in build["runes_ext"]:
            embed.add_field(name=rune["name"], value="\u200b", inline=True)
            embed.set_thumbnail(url=rune["icon"])

async def setup(bot):
    await bot.add_cog(Build(bot))