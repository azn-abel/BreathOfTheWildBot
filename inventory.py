from bot import *
from database import *


@client.group(aliases=['inventory'], invoke_without_command=True)
async def inv(ctx, *args):
    user_id = ctx.author.id
    dictCur.execute("SELECT * FROM inventory WHERE user_id = %s", (str(user_id),))
    # check if they are registered
    if dictCur.fetchall() == []:
        await ctx.send("Please register using 'z.register'")
        return
    dictCur.execute("SELECT * FROM inventory WHERE user_id = %s", (str(user_id),))
    s = dictCur.fetchone()
    await ctx.send(s)
@inv.command()
async def equipped(ctx):
    user_id = ctx.author.id
    # check if they are registered
    dictCur.execute("SELECT * FROM inventory WHERE user_id = %s", (str(user_id),))
    if dictCur.fetchall() == []:
        await ctx.send("Please register using 'z.register'")
        return
    dictCur.execute("SELECT * FROM inventory WHERE user_id = %s", (str(user_id),))
    s = dictCur.fetchone()
    embed = discord.Embed (
        Title = "Showing Equipped Items"
    )
    if s['equipped'] != {}:
        strArr = ['head', 'body', 'legs', 'weapon', 'shield', 'bow', 'arrows']
        output_text = ""
        # print(s['equipped'])
        for item in strArr:
            item_name = s['equipped'][item]['name']
            if item_name != "":
                output_text += f"**{item[0:1].upper()}{item[1:]}**: {s['equipped'][item]['name']}\n"
            else:
                output_text += f"**{item[0:1].upper()}{item[1:]}**: None\n"
    else:
        output_text = "You don't have anything equipped"
    if output_text == "You don't have anything equipped":
        embed.add_field(name=output_text, value="** **")
        embed.set_footer(text="Very sad :(")
    else:
        embed.add_field(name="Equipped Items", value=output_text, inline=True)
        embed.set_footer(text="Footer")
    await ctx.send(embed=embed)
@inv.command(aliases=['weapon'])
async def weapons(ctx):
    user_id = ctx.author.id
    output_text = ""
    handheld_text = ""
    bows_text = ""
    arrows_text = ""
    # check if they are registered
    dictCur.execute("SELECT * FROM inventory WHERE user_id = %s", (str(user_id),))
    if dictCur.fetchall() == []:
        await ctx.send("Please register using 'z.register'")
        return
    dictCur.execute("SELECT * FROM inventory WHERE user_id = %s", (str(user_id),))
    s = dictCur.fetchone()
    embed = discord.Embed (
        Title = "Showing Weapons"
    )
    if str(s['weapons']) != "{'handheld': [{}], 'bows': [{}], 'arrows': {}}":
        for item in s['weapons']['handheld']:
            handheld_text += f"{item}\n"
        for item in s['weapons']['bows']:
            bows_text += f"{item}\n"
        for item in s['weapons']['arrows']:
            arrows_text += f"{item}\n"
    else:
        output_text = "You don't have any weapons"
    if output_text == "You don't have any weapons":
        embed.add_field(name=output_text, value="** **")
        embed.set_footer(text="Very sad :(")
    else:
        if handheld_text != "":
            embed.add_field(name="Handheld", value=handheld_text, inline=True)
        if bows_text != "":
            embed.add_field(name="Bows", value=bows_text, inline=True)
        if arrows_text != "":
            embed.add_field(name="Arrows", value=arrows_text, inline=True)
        embed.set_footer(text="Footer")
    await ctx.send(embed=embed)
@inv.command()
async def armor(ctx):
    user_id = ctx.author.id
    # check if they are registered
    dictCur.execute("SELECT * FROM inventory WHERE user_id = %s", (str(user_id),))
    if dictCur.fetchall() == []:
        await ctx.send("Please register using 'z.register'")
        return
    dictCur.execute("SELECT * FROM inventory WHERE user_id = %s", (str(user_id),))
    s = dictCur.fetchone()
    embed = discord.Embed (
        Title = "Showing Armor"
    )
    print(s['armor'])
    if s['armor'] != {}:
        output_text = ""
        for item in s['armor']:
            output_text += f"{item}\n"
    else:
        output_text = "You don't have any armor pieces"
    if output_text == "You don't have any armor pieces":
        embed.add_field(name=output_text, value="** **")
        embed.set_footer(text="Very sad :(")
    else:
        embed.add_field(name="Amor", value=output_text, inline=True)
        embed.set_footer(text="Footer")
    await ctx.send(embed=embed)
@inv.command()
async def food(ctx):
    user_id = ctx.author.id
    # check if they are registered
    dictCur.execute("SELECT * FROM inventory WHERE user_id = %s", (str(user_id),))
    if dictCur.fetchall() == []:
        await ctx.send("Please register using 'z.register'")
        return
    dictCur.execute("SELECT * FROM inventory WHERE user_id = %s", (str(user_id),))
    s = dictCur.fetchone()
    embed = discord.Embed (
        Title = "Showing Food"
    )
    if s['consumables']['food'] != {}:
        output_text = ""
        for item in s['consumables']['food']:
            output_text += f"{item}\n"
    else:
        output_text = "You don't have any food"
    if output_text == "You don't have any food":
        embed.add_field(name=output_text, value="** **")
        embed.set_footer(text="Very sad :(")
    else:
        embed.add_field(name="Food", value=output_text, inline=True)
        embed.set_footer(text="Footer")
    await ctx.send(embed=embed)
@inv.command()
async def key_items(ctx):
    user_id = ctx.author.id
    # check if they are registered
    dictCur.execute("SELECT * FROM inventory WHERE user_id = %s", (str(user_id),))
    if dictCur.fetchall() == []:
        await ctx.send("Please register using 'z.register'")
        return
    dictCur.execute("SELECT * FROM inventory WHERE user_id = %s", (str(user_id),))
    s = dictCur.fetchone()
    embed = discord.Embed (
        Title = "Showing Key Items"
    )
    if s['key_items'] != {}:
        output_text = ""
        for item in s['key_items']:
            output_text += f"{item}\n"
    else:
        output_text = "You don't have any key items"
    if output_text == "You don't have any key items":
        embed.add_field(name=output_text, value="** **")
        embed.set_footer(text="Very sad :(")
    else:
        embed.add_field(name="Key Items", value=output_text, inline=True)
        embed.set_footer(text="Footer")
    await ctx.send(embed=embed)
@inv.command()
async def elixirs(ctx):
    user_id = ctx.author.id
    # check if they are registered
    dictCur.execute("SELECT * FROM inventory WHERE user_id = %s", (str(user_id),))
    if dictCur.fetchall() == []:
        await ctx.send("Please register using 'z.register'")
        return
    dictCur.execute("SELECT * FROM inventory WHERE user_id = %s", (str(user_id),))
    s = dictCur.fetchone()
    embed = discord.Embed (
        Title = "Showing Elixirs"
    )
    if s['consumables']['elixirs'] != {}:
        output_text = ""
        for item in s['consumables']['elixirs']:
            output_text += f"{item}\n"
    else:
        output_text = "You don't have any elixirs"
    if output_text == "You don't have any elixirs":
        embed.add_field(name=output_text, value="** **")
        embed.set_footer(text="Very sad :(")
    else:
        embed.add_field(name="Elixirs", value=output_text, inline=True)
        embed.set_image(url="https://static.wikia.nocookie.net/zelda_gamepedia_en/images/9/9d/BotW_Hasty_Elixir_Icon.png/revision/latest/scale-to-width-down/320?cb=20171228104522")
        embed.set_footer(text="Footer")
    await ctx.send(embed=embed)


@client.command(aliases=['give'])
async def get(ctx, *args):
    user_id = ctx.author.id
    # check if they are registered
    dictCur.execute("SELECT * FROM inventory WHERE user_id = %s", (str(user_id),))
    if dictCur.fetchall() == []:
        await ctx.send("Please register using 'z.register'")
        return
    #updateDatabase(user_id, args[0], args[1])
    await ctx.send(f"haha i know you wanted a {args[0]}, it doesn't work yet ;)")


@client.command()
async def equip(ctx, *args):
    # variables
    nullCheckArr = ['head', 'body', 'legs', 'weapon', 'shield', 'bow', 'arrows']
    user_id = str(ctx.author.id)
    itemLocation = ""
    # check if they are registered
    dictCur.execute("SELECT * FROM inventory WHERE user_id = %s", (user_id,))
    if dictCur.fetchall() == []:
        await ctx.send("Please register using 'z.register'")
        return
    # nullchecks
    if not args: return
    if args[1] not in nullCheckArr: 
        await ctx.send(f"There is no slot named '{args[1]}'.")
        return
    # get the data
    dictCur.execute("SELECT * FROM inventory WHERE user_id = %s", (user_id,))
    userDict = dictCur.fetchone()
    # check if you already have the item in the slot
    if args[1] != "arrows":
        if userDict['equipped'][args[1]]['name'] == args[0]:
            await ctx.send(f"You already have a {args[0]} in your {args[1]} slot.")
            return
    else:
        if userDict['equipped'][args[1]] == args[0]:
            await ctx.send(f"You already have a {args[0]} in your {args[1]} slot.")
            return
    # check if you have the item in your inventory
    #print(userDict)
    for weaponDict in userDict['weapons']['handheld']:
        if args[0] == weaponDict['name']:
            itemLocation = "handheld"
    for weaponDict in userDict['weapons']['bows']:
        if args[0] == weaponDict['name']:
            itemLocation = "bows"
    if args[0] in userDict['weapons']['arrows']:
        itemLocation = "arrows"
    if args[0] in userDict['armor']:
        itemLocation = "armor"
    elif args[0] in userDict['key_items']:
        itemLocation = "key_items"
    if itemLocation == "":
        await ctx.send(f"You don't have a '{args[0]}''.")
        return
    print(itemLocation)
    # put the item in the slot
    equipFunc(user_id, args[1], args[0])


# weapons
# bows
# arrows
# shields
# armor
# materials (food)
# food (elixirs)
# key items

# {
#   'head':
#   'body':
#   'legs':
#   'weapon':
#   'shield':
#   'bow':
#   'arrows':
# }


def equipFunc(user_id: str, slot: str, item: str):
    dictCur.execute("SELECT * FROM inventory WHERE user_id = %s", (user_id,))
    s = dictCur.fetchone()
    itemDict = s['equipped']
    itemDict[slot] = {'name': item, 'durability': 1000}
    dictCur.execute("UPDATE inventory SET equipped = %s WHERE user_id = %s", (Json(itemDict), user_id))
    conn.commit()

# I have not made this work yet, and it doesn't get called so don't worry
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