from flask import Flask, request, jsonify, abort, render_template
from pathlib import Path
import json

if not Path("/tmp/valoresAPI.tmp").exists:
    with open("/tmp/valoresAPI.tmp","w") as data_file:
        data = {
            "val_max" : 0,
            "val_min" : 0,
            "val"     : 0
        }
        json.dump(data,data_file)

app = Flask(__name__)

@app.route('/', methods=["GET"])
def index():
    return render_template('index.html')

@app.route('/valores', methods=["GET"])
def verV():
    dataA = {}
    with open("/tmp/valoresAPI.tmp","r") as data_read:
        dataA = json.load(data_read)
    return jsonify(dataA), 200

app.run(host='0.0.0.0', port=8000, debug=True)