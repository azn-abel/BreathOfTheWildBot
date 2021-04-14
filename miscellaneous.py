from bot import *
from database import *


@client.command()
async def ping(ctx):
    await ctx.reply("pong!")


@client.command()
async def register(ctx):
    user_id = str(ctx.author.id)
    dictCur.execute("SELECT * FROM inventory WHERE user_id = %s", (user_id,))
    if dictCur.fetchall() != []:
        await ctx.send("You are already registered...")
        return
    jsonArr = Json({'handheld': [{}], 'bows': [{}], 'arrows': {}})
    dictCur.execute("INSERT INTO inventory (user_id, equipped, weapons, shields, armor, consumables, key_items) VALUES (%s, %s, %s, %s, %s, %s, %s)", (user_id, Json({}), jsonArr, Json({}), Json({}), Json({'food': {}, 'elixirs': {}}), Json({})))
    conn.commit()
    await ctx.send("You are now registered!")
    # dictCur.execute("SELECT * FROM inventory")
    # s = dictCur.fetchall()
    # print(s)