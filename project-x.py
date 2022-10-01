from flask import Flask
import flask
app = Flask(__name__)
import json
@app.route("/")
def hello():
    return "Hello, World!"

@app.route('/users', methods=["GET"])
def users():
    print("users endpoint reached...")
    with open("users.json", "r") as f:
        data = json.load(f)
        data.append({"username":"user4", "pets": ["hamster"]})
        return flask.jsonify(data)
if __name__ == '__main__':
    app.run('localhost', 6969)

test_inputID = '1241 4324 3453 5325'
test_inputExpiryFrom = '05/21'
test_inputExpiryThru = '09/24'
test_inputName = 'Patrick Gatal'