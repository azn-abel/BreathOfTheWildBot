from bot import *
from data import *


@client.group(invoke_without_command=False)
async def show(ctx):
    pass


@show.command(aliases=['region'])
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
    embed.set_footer(text="Use \"z.travel shrine <region-id> <location-id>\" to travel to a location!")
    embed.set_image(url="https://i.redd.it/w09wxsvckad31.jpg")

    await ctx.send(embed=embed)


@client.command()
async def travel(ctx, region_id: int, shrine_id: int):
    try:
        region = get_region(region_id)
        shrine = get_shrine(region_id, shrine_id)
    except:
        await ctx.reply("Invalid region or shrine ID.")
        return

    embed = discord.Embed(
        title=f"{shrine['name']} Shrine"
    )
    embed.add_field(name='Location:', value=f"{region['tower']} Region", inline=False)
    embed.add_field(name='Question:', value=shrine['puzzle_question'], inline=False)
    embed.add_field(name='Answer:', value=shrine['puzzle_answer'], inline=False)
    embed.set_footer(text=f"Shrine ID: {region_id}-{shrine_id}")
    embed.set_image(url="https://cdn.vox-cdn.com/thumbor/R73CXU-Og3tdWbfRYTg6zpqTCY4=/0x0:1920x1080/1200x800/filters:focal(807x387:1113x693)/cdn.vox-cdn.com/uploads/chorus_image/image/64062748/challenge_dungeon_temple_things.0.jpg")

    await ctx.send(embed=embed)

