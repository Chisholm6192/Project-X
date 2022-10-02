from flask import Flask, request
import flask
import json
from flask_cors import CORS
import os
from openpyxl import Workbook, load_workbook

app = Flask(__name__)
CORS(app)

storage = {}
headings = []
wb = Workbook()
ws = wb.active
class creditCards:
    def addEntries(self, store,heading):
        with open('new_file.json', 'w') as f:
            json.dumps(store['Name'])
            json.dumps(headings['Name'])
creditCards()
@app.route('/test', methods=['GET'])
def input_tests():
    if request.method == 'GET':
        with open('users.json', 'r') as f:
            data = json.load(f)
            for k,v in data.items():
                headings.append[k]
                storage[k] = v
            creditCards.addEntries(storage, heading)
            return flask.jsonify(storage)

@app.route('/users', methods=["HEAD"])
def users():
    print("users endpoint reached...")
    if request.method == "HEAD":
        creditCards()
    # if request.method == "POST":
    #     received_data = request.get_json()
    #     print(f"received data: {received_data}")
    #     message = received_data['data']
    #     return_data = {
    #         "status": "success",
    #         "message": f"received: {message}"
    #     }
    #     return flask.Response(response=json.dumps(return_data), status=201)

if __name__ == "__main__":
    app.run("localhost", 6969)