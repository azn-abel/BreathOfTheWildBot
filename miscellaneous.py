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
    equippedDict = {'head': {'name': '', 'durability': 0}, 'body': {'name': '', 'durability': 0}, 'legs': {'name': '', 'durability': 0}, 'weapon': {'name': '', 'durability': 0}, 'shield': {'name': '', 'durability': 0}, 'bow': {'name': '', 'durability': 0}, 'arrows': {'name': '', 'durability': 0}}
    weaponDict = {'handheld': [{'name': '', 'damage': 0, 'durability': 0}], 'bows': [{'name': '', 'damage': 0, 'durability': 0}], 'arrows': {'name': '', 'durability': 0}}
    shieldDict = [{'name': '', 'durability': 0}]
    armorDict = [{'name': '', 'durability': 0}]
    consumableDict = {'food': [{'name': '', 'durability': 0}], 'elixirs': [{'name': '', 'durability': 0}]}
    key_itemsDict = [{'name': '', 'durability': 0}] # idk what we need to save here so this is a placeholder
    dictCur.execute("INSERT INTO inventory (user_id, equipped, weapons, shields, armor, consumables, key_items) VALUES (%s, %s, %s, %s, %s, %s, %s)", (user_id, Json(equippedDict), Json(weaponDict), Json(shieldDict), Json(armorDict), Json(consumableDict), Json(key_itemsDict)))
    conn.commit()
    await ctx.send("You are now registered!")