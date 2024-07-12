from flask import Flask, jsonify
from flask import request
from membership import PCSpecsMembership
import main as fuzzy
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

        response = jsonify(fuzzy.ezpc(val1, val2, val3))

        return response
        

