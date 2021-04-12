import discord
from discord.ext import commands

TOKEN = "ODMxMzAwNjc2NTk5ODA4MDEx.YHTPFg.o8tEpy_iB6xZ8Q382h0DN9RXQmk"
intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True, presences=True)
client = commands.Bot(command_prefix=['p!', 'P!'], intents=intents)
