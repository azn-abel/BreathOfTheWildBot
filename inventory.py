from bot import *
from database import *


@client.group(aliases=['inventory'], invoke_without_command=True)
async def inv(ctx, *args):
    user_id = ctx.author.id
    dictCur.execute("SELECT * FROM inventory WHERE user_id = %s", (str(user_id),))
    # if they don't have thing
    if dictCur.fetchall() == []:
        dictCur.execute("INSERT INTO inventory (user_id, equipped, weapons, armor, food, key_items, elixirs) VALUES (%s, %s, %s, %s, %s, %s, %s)", (str(user_id), Json({}), [], [], Json({}), Json({}), Json({})))
        conn.commit()
        dictCur.execute("SELECT * FROM inventory WHERE user_id = %s", (str(user_id),))
        print(s)
        print(f"Created row for {ctx.author.name}")
    dictCur.execute("SELECT * FROM inventory WHERE user_id = %s", (str(user_id),))
    s = dictCur.fetchone()
    await ctx.send(s)
@inv.command()
async def equipped(ctx):
    user_id = ctx.author.id
    dictCur.execute("SELECT * FROM inventory WHERE user_id = %s", (str(user_id),))
    s = dictCur.fetchone()
    if s['equipped'] != {}:
        output_text = ""
        for item in s['equipped']:
            output_text += f"{item['name']} "
        await ctx.send(output_text)
    else:
        await ctx.send("You don't have anything equipped")
@inv.command(aliases=['weapon'])
async def weapons(ctx):
    user_id = ctx.author.id
    dictCur.execute("SELECT * FROM inventory WHERE user_id = %s", (str(user_id),))
    s = dictCur.fetchone()
    if s['weapons'] != []:
        output_text = ""
        for item in s['weapons']:
            output_text += item
        await ctx.send(output_text)
    else:
        await ctx.send("You don't have any weapons :(")
@inv.command()
async def armor(ctx):
    user_id = ctx.author.id
    dictCur.execute("SELECT * FROM inventory WHERE user_id = %s", (str(user_id),))
    s = dictCur.fetchone()
    if s['armor'] != []:
        output_text = ""
        for item in s['armor']:
            output_text += item
        await ctx.send(output_text)
    else:
        await ctx.send("You don't have any armor pieces :(")


@client.command()
async def get(ctx, *args):
    user_id = ctx.author.id
    updateDatabase(user_id, args[0], args[1])


def updateDatabase(user_id: int, column: str, item: str):
    user_id = str(user_id)
    dictCur.execute("SELECT * FROM inventory WHERE user_id = %s", (user_id,))
    s = dictCur.fetchone()
    if column == 'weapons' or column == 'armor':
        itemArr = s[column]
        itemArr.append(item)
        if column == 'weapons':
            dictCur.execute("UPDATE inventory SET weapons = %s WHERE user_id = %s", (itemArr, user_id))
        else:
            dictCur.execute("UPDATE inventory SET armor = %s WHERE user_id = %s", (itemArr, user_id))
        conn.commit()
    elif column == 'equipped' or column == 'food' or column == 'key_items' or column == 'elixirs':
        itemDict = s[column]
        if item in itemDict.keys():
            itemDict[item] += 1
        else:
            itemDict[item] = 1
        if column == 'equipped':
            dictCur.execute("UPDATE inventory SET equipped = %s WHERE user_id = %s", (Json(itemDict), user_id))
        elif column == 'food':
            dictCur.execute("UPDATE inventory SET food = %s WHERE user_id = %s", (Json(itemDict), user_id))
        elif column == 'key_items':
            dictCur.execute("UPDATE inventory SET key_items = %s WHERE user_id = %s", (Json(itemDict), user_id))
        else:
            dictCur.execute("UPDATE inventory SET elixirs = %s WHERE user_id = %s", (Json(itemDict), user_id))
        conn.commit()