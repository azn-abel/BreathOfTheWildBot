import json

map_data = json.load(open('map.json',))


def get_region(region_id):
    region = map_data['regions'][region_id]
    return region


def get_shrine(region_id, shrine_id):
    shrine = map_data['regions'][region_id]['shrines'][shrine_id]
    return shrine
