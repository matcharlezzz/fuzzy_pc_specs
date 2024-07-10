from itertools import islice
import json

f = open('db/backup-1720626377.json')

data = json.load(f)

reco_specs = {}


def recommendation(score: int) -> dict:
    for i in range(len(data)):
        if data[i]['total_price'] <= score * 10000:
            reco_specs[data[i]['total_price'] / 10000] = data[i]

    sorted_reco = dict(sorted(reco_specs.items(), reverse=True))
    top_five = dict(islice(sorted_reco.items(), 5))

    return top_five


f.close()
