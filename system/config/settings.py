import discord
import os

from dotenv import load_dotenv

load_dotenv()
            
TOKEN = os.getenv("TOKEN_AKALI")
PUB_KEY = os.getenv("PUB_KEY_AKALI")
APP_ID = os.getenv("APPLICATION_ID_AKALi")
VERSION = os.getenv("VERSION_AKALI")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY_AKALI")
README_MD = (discord.File('README.md', filename='README.md'))