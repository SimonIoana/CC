import requests
import flask
from flask import jsonify
import json

app = flask.Flask(__name__)
app.config["DEBUG"] = True


@app.route('/', methods=['GET'])
def home():
    return "<h1>Random numbers</h1><p>This site is a prototype API for random numbers.</p>"
@app.route('/api/v1/resources/numbers', methods=['GET'])
def api_id():
    URL = "https://random-data-api.com/api/bank/random_bank"
    response = requests.get(URL)
    data = response.json()
    print(data)

    URL1 = "https://api.random.org/dashboard"
    response1 = requests.get(URL1)
    data1 = response1.json()
    print(data1)

    URL2 = "https://randomapi.com/"
    response2 = requests.get(URL2)
    data2 = response2.json()
    print(data2)
    return jsonify(data)
    return jsonify(data1)
    return jsonify(data2)
app.run()
