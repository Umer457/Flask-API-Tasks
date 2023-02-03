from flask import Flask, jsonify

app = Flask(__name__)

data = [
    {'name': 'Umer Nadeem', 'email': 'umer.nadeem@gmail.com'},
    {'name': 'Usama Rashid', 'email': 'usamarashid@gmail.com'},
    {'name': 'Duraze Saqib', 'email': 'durazesaqib@gmail.com'},
]
@app.route('/')
def index():
    return "Test Server Created for Assignment 2"
@app.route("/info", methods=["GET"])
def info():
    return jsonify({'Users': data})

if __name__ == "__main__":
    app.run(debug=True)