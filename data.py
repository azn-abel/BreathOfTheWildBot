import json

map_data = json.load(open('map.json',))


def get_region(region_id):
    region = map_data['regions'][region_id]
    return region


def get_shrine(region_id, shrine_id):
    shrine = map_data['regions'][region_id]['shrines'][shrine_id]
    return shrine


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
