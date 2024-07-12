from itertools import islice
import json

f = open('db/datasets.json')

data = json.load(f)

reco_specs = {}


def recommendation(score: int) -> dict:
    for i in range(len(data)):
        if data[i]['total_price'] <= score * 10000:
            reco_specs[data[i]['total_price'] / 10000] = {key.strip('()'): value for key, value in data[i].items()}
            reco_specs[data[i]['total_price'] / 10000].pop('total_price')

    sorted_reco = dict(sorted(reco_specs.items(), reverse=True))
    top_five = dict(islice(sorted_reco.items(), 5))

    pretty_top_five = pretty_format(top_five)

    return top_five


def pretty_format(build_list: dict) -> dict:
    prettified_build_list = {}
    build_rank = 1

    for key in build_list:
        # create a new key with its rank
        prettified_build_list[build_rank] = {}
        for components in build_list[key]:
            # remove {name: } and replace the component value into actual name
            prettified_build_list[build_rank][components] = build_list[key][components]['name']

        build_rank += 1

    return prettified_build_list


f.close()
