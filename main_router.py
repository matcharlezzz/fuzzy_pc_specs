from flask import Flask, jsonify
from flask import request
from membership import PCSpecsMembership
import inference_engine as ig
import defuzzifier as dfz
import recommender as rcm
import json
import pprint

app = Flask(__name__)

@app.route("/query", methods=['POST'])
def receive_query():
    error = None
    if request.method == 'POST':
        data = json.loads(request.data.decode('utf-8'))
        print(f'data are: {data}')

        pc = PCSpecsMembership()

        val1 = pc.budget(float(data["budget"]))
        val2 = pc.workload(float(data["workload"]))
        val3 = pc.storage(float(data["storage"]))

        print(f"val1: {val1}, val2: {val2}, val3: {val3}")

        all_inputs = ig.input_combiner(val1, val2, val3)
        aggregate = dfz.aggregate(ig.ruleset, ig.output_sets, all_inputs, False)

        defuzz_out = dfz.defuzzy(aggregate, ig.output_xmid)
        defuzz_outV2 = dfz.defuzzyV2(aggregate)

        defuzz_list = [defuzz_out, defuzz_outV2]

        closest_defuzz = min(defuzz_list, key=lambda x: abs(x - (int(data["budget"]) / 10000)))

        print(f'\nFinal PC Score: {closest_defuzz}')

        recos = rcm.recommendation(closest_defuzz)

        data = json.dumps(recos, indent=4)
        response = jsonify(recos)
        print(response.data)
        return response

