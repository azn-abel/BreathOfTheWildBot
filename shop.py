from bot import *
from data import *
from database import *

# z.buy <region-id>-<shop-id> <item-index> <amount>

@client.command()
async def buy(ctx, *args):
    # variables
    user_id = str(ctx.author.id)
    # check if they are registered
    dictCur.execute("SELECT * FROM inventory WHERE user_id = %s", (user_id,))
    if dictCur.fetchall() == []:
        await ctx.send("Please register using 'z.register'")
        return
    # nullchecks
    if len(args) < 2 or len(args) > 4:
        await ctx.send("You don't have the correct arguments :(")
        return
    # more variables
    id = args[0].split("-")
    region_id = int(id[0])
    shop_id = int(id[1])
    item_index = int(args[1])
    amount = int(args[2])
    rupees = None
    sqlSet = None
    # check to see if all of the id's work
    try:
        region = get_region(region_id)
        shop = get_shop(region_id, shop_id)
    except:
        await ctx.send("Invalid region or shop ID.")
        return
    # test / get the item requested
    try:
        shopName = str(shop['name'])
        mapDict = shop['products'][item_index]
        item_name = mapDict['name']
        item_item = mapDict['item']
        item_price = mapDict['price']
        item_stock = mapDict['stock']
    except:
        await ctx.send(f"Invalid item ID: {item_index}")
        return
    # test for enough stock
    if amount <= 0 or amount > item_stock:
        await ctx.send(f"Amount '{amount}' incorrect")
        return
    # test for enough rupees
    dictCur.execute("SELECT * FROM inventory WHERE user_id = %s", (user_id,))
    s = dictCur.fetchone()
    if s['rupees'] < (item_price * amount):
        await ctx.send("You don't have enough rupees for that :(")
        return
    # do the stuff lmao
    rupees = s['rupees'] - (item_price * amount)
    itemDict = find_item(item_item)
    rootColumn = item_item.split('_')[-1]
    if rootColumn == "bow": rootColumn = "bows"
    # put stuff in the dicitonary
    if rootColumn == "handheld" or rootColumn == "bows":
        s['weapons'][rootColumn].append({'name': item_name, 'damage': itemDict['damage'], 'durability': itemDict['durability'], 'item': item_item})
        sqlSet = "weapons"
        # print(s['weapons'])
    
    # now put it in database
    dictCur.execute("UPDATE inventory SET " + sqlSet + " = %s WHERE user_id = %s", (Json(s[sqlSet]), user_id))
    dictCur.execute("UPDATE inventory SET rupees = %s WHERE user_id = %s", (rupees, user_id))
    conn.commit()
    await ctx.send(f"You bought a {item_name} for {item_price * amount} rupees, hope you enjoy!")


@client.command(aliases=['balance'])
async def bal(ctx):
    # variables
    user_id = str(ctx.author.id)
    # check if they are registered
    dictCur.execute("SELECT * FROM inventory WHERE user_id = %s", (user_id,))
    if dictCur.fetchall() == []:
        await ctx.send("Please register using 'z.register'")
        return
    dictCur.execute("SELECT * FROM inventory WHERE user_id = %s", (user_id,))
    rupees = dictCur.fetchone()['rupees']
    if rupees == 0:
        await ctx.send("You don't have any rupees...")
        return
    await ctx.send(f"You have {rupees} rupees!")
