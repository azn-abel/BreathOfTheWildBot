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
    embed = discord.Embed (
        Title = "Showing Equipped Items"
    )
    if s['equipped'] != {}:
        output_text = ""
        for item in s['equipped']:
            output_text += f"{item['name']}\n"
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
    dictCur.execute("SELECT * FROM inventory WHERE user_id = %s", (str(user_id),))
    s = dictCur.fetchone()
    embed = discord.Embed (
        Title = "Showing Weapons"
    )
    if s['weapons'] != []:
        output_text = ""
        for item in s['weapons']:
            output_text += f"{item}\n"
    else:
        output_text = "You don't have any weapons"
    if output_text == "You don't have any weapons":
        embed.add_field(name=output_text, value="** **")
        embed.set_footer(text="Very sad :(")
    else:
        embed.add_field(name="Weapons", value=output_text, inline=True)
        embed.set_footer(text="Footer")
    await ctx.send(embed=embed)
@inv.command()
async def armor(ctx):
    user_id = ctx.author.id
    dictCur.execute("SELECT * FROM inventory WHERE user_id = %s", (str(user_id),))
    s = dictCur.fetchone()
    embed = discord.Embed (
        Title = "Showing Armor"
    )
    if s['armor'] != []:
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
    dictCur.execute("SELECT * FROM inventory WHERE user_id = %s", (str(user_id),))
    s = dictCur.fetchone()
    embed = discord.Embed (
        Title = "Showing Food"
    )
    if s['food'] != {}:
        output_text = ""
        for item in s['food']:
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
    dictCur.execute("SELECT * FROM inventory WHERE user_id = %s", (str(user_id),))
    s = dictCur.fetchone()
    embed = discord.Embed (
        Title = "Showing Elixirs"
    )
    if s['elixirs'] != {}:
        output_text = ""
        for item in s['elixirs']:
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
    print(user_id)
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