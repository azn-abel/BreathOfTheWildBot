from bot import *
from data import *
from database import *


@client.command(aliases=['get'])
@commands.has_role("botDev")
async def give(ctx, *args):
    # variables
    user_id = ctx.author.id
    nullCheckArr = ['handheld', 'bows', 'arrows', 'shields', 'armor', 'food', 'elixirs', 'key_items']
    # check if they are registered
    dictCur.execute("SELECT * FROM inventory WHERE user_id = %s", (str(user_id),))
    if dictCur.fetchall() == []:
        await ctx.send("Please register using 'z.register'")
        return
    # give money
    if args[0] == 'rupees':
        dictCur.execute("SELECT rupees FROM inventory WHERE user_id = %s", (str(user_id),))
        s = dictCur.fetchone()
        rupees = s['rupees'] + int(args[1])
        dictCur.execute("UPDATE inventory SET rupees = %s WHERE user_id = %s", (rupees, str(user_id)))
        conn.commit()
        await ctx.send(f"Gave you {args[1]} rupees.. baka")
        return
    # nullcheck
    if len(args) < 2: return
    if args[1] not in nullCheckArr:
        await ctx.send(f"There is no slot named '{args[1]}'.")
        return
    updateDatabase(user_id, args[0], args[1])
    await ctx.send(f"You gave yourself a {args[0]}. You cheater. I'm dissapointed in you.")


@client.command()
@commands.has_role("botDev")
async def set(ctx, *args):
    # variables
    user_id = ctx.author.id
    # check if they are registered
    dictCur.execute("SELECT * FROM inventory WHERE user_id = %s", (str(user_id),))
    if dictCur.fetchall() == []:
        await ctx.send("Please register using 'z.register'")
        return
    if args[0] == 'rupees':
        dictCur.execute("UPDATE inventory SET rupees = %s WHERE user_id = %s", (int(args[1]), str(user_id)))
        conn.commit()
        await ctx.send(f"Set your rupees to: {args[1]}")
        return


# I worked too hard on something that won't actually be in the game...
def updateDatabase(user_id: int, item: str, slot: str):
    # variables
    user_id = str(user_id)
    itemFound = False
    itemData = {}
    sqlSet = None
    # get the dictionary
    dictCur.execute("SELECT * FROM inventory WHERE user_id = %s", (user_id,))
    s = dictCur.fetchone()
    itemDict = {}
    rootColumn = ""
    # set the dictionary and rootColumn
    itemDict = find_item(item)
    rootColumn = item.split('_')[-1]
    if rootColumn == "bow": rootColumn = "bows"
    if rootColumn == "food" or rootColumn == "elixirs":
        sqlSet = "consumables"
        if itemDict:
            try:
                print(s['consumables'][rootColumn])
                print(item)
                s['consumables'][rootColumn][item]['durability'] += 1
            except:
                s['consumables'][rootColumn][item] = {'name': itemDict['name'], 'durability': 1}
    elif rootColumn == "handheld" or rootColumn == "bows":
        sqlSet = "weapons"
        if itemDict:
            s['weapons'][rootColumn].append({'name': itemDict['name'], 'damage': itemDict['damage'], 'durability': itemDict['durability']})
    elif rootcolumn == "shields" or rootColumn == "armor":
        print(rootColumn)
        # sqlSet = rootColumn
        # if itemDict:
        #     s[sqlSet]
    # put the itemDict into the big dictionary
    dictCur.execute("UPDATE inventory SET " + sqlSet + " = %s WHERE user_id = %s", (Json(s[sqlSet]), user_id))
    conn.commit()
