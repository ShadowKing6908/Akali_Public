from discord.ext import commands
from config.akali_main import AkaliBot
from config.settings import TOKEN

__token__ = TOKEN

akali = AkaliBot()

if __name__ == '__main__':
    akali.run((__token__))