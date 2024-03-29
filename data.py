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


def get_shop(region_id, shop_id):
    return map_data['regions'][region_id]['shops'][shop_id]


def shop_stock_display(shop):
    output = ""
    for x in range(0, len(shop['products'])):
        product = shop['products'][x]
        output += f"**{x}:** {product['name']} - {product['price']} Rupees each, {product['stock']} in stock.\n"
    return output


def get_map_data():
    return map_data


def write_map_data(json_data):
    with open("map.json", "w") as write_file:
        json.dump(json_data, write_file)


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


def find_item(item):
    location = item.split('_')[-1]
    if location == 'handheld':
        return [gear_data['weapons']['handheld'][i] for i in gear_data['weapons']['handheld'] if i == item][0]
    elif location == 'bow':
        return [gear_data['weapons']['bows'][i] for i in gear_data['weapons']['bows'] if i == item][0]
    elif location == 'shields':
        return [gear_data['shields'][i] for i in gear_data['shields'] if i == item][0]
    elif location == 'food':
        return [gear_data['consumables']['food'][i] for i in gear_data['consumables']['food'] if i == item][0]
    return None


def EmptyMask(key):
    return [[False for _ in region[key]] for region in map_data['regions']]
