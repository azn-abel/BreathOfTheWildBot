from bot import *
from data import *
import re

pattern = re.compile('[\W_]+')

@client.group(invoke_without_command=False)
async def show(ctx):
    pass


@show.command(aliases=['region', 'reg'])
async def regions(ctx):
    output_string_1, output_string_2 = two_col_output(map_data['regions'], 'tower')

    embed = discord.Embed(
        title="Showing All Regions"
    )
    embed.add_field(name='Region - ID:', value=output_string_1, inline=True)
    embed.add_field(name='** **', value=output_string_2, inline=True)
    embed.set_footer(text="Use \"z.show shrines <region-id>\" to see shrines in that region!")
    embed.set_image(url="https://cdn.vox-cdn.com/thumbor/y_jWcps4hKDVit_gONR0bvOIpuE=/0x0:1280x720/1200x800/filters:focal(538x258:742x462)/cdn.vox-cdn.com/uploads/chorus_image/image/54792785/Zelda_E3_11am_SCRN062.0.0.jpg")

    await ctx.send(embed=embed)


@show.command(aliases=['shrine'])
async def shrines(ctx, region_id: int):
    region = get_region(region_id)
    region_name = region['tower']

    output_string_1, output_string_2 = two_col_output(region['shrines'], 'name')

    embed = discord.Embed(
        title=f"Showing Shrines in the {region_name} Region ({region_id})"
    )
    embed.add_field(name='Shrine - ID:', value=output_string_1, inline=True)
    embed.add_field(name='** **', value=output_string_2, inline=True)
    embed.set_footer(text="Use \"z.travel shrine <region-id> <shrine-id>\" to travel to a shrine!")
    embed.set_image(url="https://i.redd.it/w09wxsvckad31.jpg")

    await ctx.send(embed=embed)


@show.command(aliases=['loc', 'location'])
async def locations(ctx, region_id: int):
    region = get_region(region_id)
    region_name = region['tower']

    output_string_1, output_string_2 = two_col_output(region['locations'], 'name')

    embed = discord.Embed(
        title=f"Showing Locations in the {region_name} Region ({region_id})"
    )
    embed.add_field(name='Location - ID:', value=output_string_1, inline=True)
    embed.add_field(name='** **', value=output_string_2, inline=True)
    embed.set_footer(text="Use \"z.travel loc <region-id> <location-id>\" to travel to a location!")
    embed.set_image(url="https://i.redd.it/w09wxsvckad31.jpg")

    await ctx.send(embed=embed)


@show.command(aliases=["shop"])
async def shops(ctx, region_id: int):
    region = get_region(region_id)
    region_name = region['tower']

    output_string = ""

    for x in range(0, len(region['shops'])):
        output_string += f"{region['shops'][x]['name']} - {x}"

    embed = discord.Embed(
        title=f"Showing Shops in the {region_name} Region ({region_id})"
    )
    embed.add_field(name='Shop - ID:', value=output_string)
    embed.set_footer(text="Use \"z.travel shop <region-id> <location-id>\" to travel to a shop!")
    embed.set_image(url='https://www.zeldadungeon.net/wiki/images/thumb/1/11/Kochi_Dye_Shop_-_HWAoC.png/280px-Kochi_Dye_Shop_-_HWAoC.png')

    await ctx.send(embed=embed)


@client.group(invoke_without_command=False)
async def travel(ctx):
    pass


@travel.command()
async def shrine(ctx, region_id: int, shrine_id: int):
    try:
        region = get_region(region_id)
        shrine = get_shrine(region_id, shrine_id)
    except:
        await ctx.reply("Invalid region or shrine ID.")
        return

    embed = discord.Embed(
        title=f"{shrine['name']} Shrine"
    )
    embed.add_field(name='Region:', value=f"{region['tower']}", inline=False)
    embed.add_field(name='Question:', value=shrine['puzzle_question'], inline=False)
    embed.add_field(name='Answer:', value=shrine['puzzle_answer'], inline=False)
    embed.set_footer(text=f"Shrine ID: {region_id}-{shrine_id}")
    embed.set_image(url="https://cdn.vox-cdn.com/thumbor/R73CXU-Og3tdWbfRYTg6zpqTCY4=/0x0:1920x1080/1200x800/filters:focal(807x387:1113x693)/cdn.vox-cdn.com/uploads/chorus_image/image/64062748/challenge_dungeon_temple_things.0.jpg")

    await ctx.send(embed=embed)


@travel.command(aliases=['loc'])
async def location(ctx, region_id: int, location_id: int):
    try:
        region = get_region(region_id)
        location = get_location(region_id, location_id)
    except:
        await ctx.reply("Invalid region or location ID.")
        return

    embed = discord.Embed(
        title=f"{location['name']}"
    )
    embed.add_field(name='Region:', value=f"{region['tower']}", inline=False)
    embed.add_field(name='Use `z.hunt` or `z.forage` to obtain resources from this area!', value="** **", inline=False)
    embed.set_footer(text=f"Location ID: {region_id}-{location_id}")

    image = get_image(f"images/locations/{pattern.sub('', location['name']).lower()}")
    embed.set_image(url='attachment://image.png')

    await ctx.send(file=image, embed=embed)


@travel.command(aliases=['shop'])
async def shops(ctx, region_id: int, shop_id: int):
    try:
        region = get_region(region_id)
        shop = get_shop(region_id, shop_id)
    except:
        await ctx.reply("Invalid region or location ID.")
        return

    embed = discord.Embed(
        title=f"{shop['name']}"
    )
    embed.add_field(name='Region:', value=f"{region['tower']}", inline=False)
    embed.add_field(name='Stock:', value=f"{shop_stock_display(shop)}", inline=False)
    embed.add_field(name='Use `z.buy <region-id>-<shop-id> <item-index> <amount>` to buy something!', value="** **", inline=False)
    embed.set_footer(text=f"Shop ID: {region_id}-{shop_id}")

    image = get_image(f"images/shops/{pattern.sub('', shop['name']).lower()}")
    embed.set_image(url='attachment://image.png')

    await ctx.send(file=image, embed=embed)
