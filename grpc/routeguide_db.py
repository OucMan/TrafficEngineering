import json
import routeguide_pb2

def read_routeguide_db(path):
    feature_list = []
    with open(path) as f:
        for item in json.load(f):
            feature = routeguide_pb2.Feature(
                name = item['name'],
                location = routeguide_pb2.Point(
                    latitude = item['location']['latitude'],
                    longitude = item['location']['longitude']
                )
            )
            feature_list.append(feature)
    return feature_list
