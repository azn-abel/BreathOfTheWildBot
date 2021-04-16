import json
import discord

map_data = json.load(open('map.json',))
gear_data = json.load(open('gear.json',))

def get_region(region_id):
    return map_data['regions'][region_id]


def get_shrine(region_id, shrine_id):
    return map_data['regions'][region_id]['shrines'][shrine_id]


def get_location(region_id, location_id):
    return map_data['regions'][region_id]['locations'][location_id]


def get_image(path):
    try:
        return discord.File(f"{path}.png", filename="image.png")
    except:
        return discord.File(f"{path}.jpg", filename="image.png")


def two_col_output(lst, key):
    output_string_1 = ""
    output_string_2 = ""
    counter = 0
    for item in lst:
        if counter < len(lst) / 2:
            output_string_1 += f"{item[key]} - {counter}\n"
        else:
            output_string_2 += f"{item[key]} - {counter}\n"
        counter += 1
    return output_string_1, output_string_2


def get_surface(root, item):
    return gear_data[root][item]


def get_deep(root, column, item):
    return gear_data[root][column][item]
