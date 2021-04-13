from bot import *
from data import *


@client.group(invoke_without_command=False)
async def show(ctx):
    pass


@show.command(aliases=['region'])
async def regions(ctx):
    output_string = ""

    counter = 0
    for region in map_data['regions']:
        output_string += f"{region['tower']} - {counter}\n"
        counter += 1

    embed = discord.Embed(
        title="Showing All Regions"
    )
    embed.add_field(name='Region - ID:', value=output_string)
    embed.set_footer(text="Use \"z.show shrines <region-id>\" to see shrines in that region!")

    await ctx.send(embed=embed)


@show.command(aliases=['shrine'])
async def shrines(ctx, region_id: int):
    region = get_region(region_id)
    region_name = region['tower']
    output_string = ""

    counter = 0
    for shrine in region['shrines']:
        output_string += f"{shrine['name']} - {counter}\n"
        counter += 1

    embed = discord.Embed(
        title=f"Showing Shrines in the {region_name} Region"
    )
    embed.add_field(name='Shrine - ID:', value=output_string)
    embed.set_footer(text="Use \"z.travel shrine <region-id> <shrine-id>\" to travel to a shrine!")

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

    await ctx.send(embed=embed)

