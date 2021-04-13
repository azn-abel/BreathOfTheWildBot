import json

map_data = json.load(open('map.json',))

def get_question(region_id, shrine_id):
    question = map_data['regions'][region_id]['shrines'][shrine_id]['puzzle_questions']