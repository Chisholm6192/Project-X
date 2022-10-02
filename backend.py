import math
from flask import Flask, request
import flask
import json
from flask_cors import CORS
<<<<<<< Updated upstream
=======

>>>>>>> Stashed changes

app = Flask(__name__)
CORS(app)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route('/users', methods=["GET", "POST"])
def users():
    print("users endpoint reached...")
    if request.method == "GET":
        with open("users.json", "r") as f:
            data = json.load(f)
<<<<<<< Updated upstream
            data.append({
                "Name": "Hello",
                "Amount": ["10"]
            })

            return flask.jsonify(data)
=======
        return flask.jsonify(data)

>>>>>>> Stashed changes
    if request.method == "POST":
        received_data = request.get_json()
        print(f"received data: {received_data}")
        message = received_data['data']
        return_data = {
            "status": "success",
            "message": f"received: {message}"
        }
        return flask.Response(response=json.dumps(return_data), status=201)

if __name__ == "__main__":
    app.run("localhost", 6969)


<<<<<<< Updated upstream
name = str(input("Enter Name: "))
amount = int(input("Enter Amount: "))
result = math.ceil(amount)

=======
#name = str(input("Enter Name: "))
#amount = int(input("Enter Amount: "))
#result = math.ceil(amount) - amount
>>>>>>> Stashed changes
