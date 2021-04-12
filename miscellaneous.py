from bot import *


@client.command()
async def ping(ctx):
    await ctx.reply("pong!")
