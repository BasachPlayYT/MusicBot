import discord
from discord import utils
from discord.ext import commands
import os

Bot = commands.Bot(command_prefix= "!")
Bot.remove_command('help')

@Bot.event
async def on_ready():
	print('Bot is online')

token = os.environ.get('BOT_TOKEN')
Bot.run(str(token))