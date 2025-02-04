import json


def pack_dict(dictionary):
    clear_json()

    json_object = json.dumps(dictionary, indent=4)

    with open('db/sends.json', 'w') as outfile:
        outfile.write(json_object)

    return True


def clear_json():

    with open('db/sends.json', 'w') as outfile:
        outfile.truncate()

    return
