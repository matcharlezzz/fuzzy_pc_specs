import json


def pack_dict(dictionary):

    json_object = json.dumps(dictionary, indent=4)

    with open('db/sends.json', 'w') as outfile:
        outfile.write(json_object)

    return True
