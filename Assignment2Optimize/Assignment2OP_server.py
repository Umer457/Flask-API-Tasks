from flask import Flask, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    return "Test Server Created for Assignment 1"

@app.route("/data", methods=['GET'])
def get_data():
    with open("data.json") as json_file:
        data = json.load(json_file)
    return jsonify(data)

if __name__ == "__main__":
    app.run(debug=True)