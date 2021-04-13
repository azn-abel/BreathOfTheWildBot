import discord
from discord.ext import commands
import os

if os.getenv("HOME") != '/app':
    from environment import *

TOKEN = os.getenv('DISCORD_BOT_TOKEN')
intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
client = commands.Bot(command_prefix=['z.', 'Z.'], intents=intents)
