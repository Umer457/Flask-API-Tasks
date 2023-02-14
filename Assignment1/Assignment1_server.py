from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Test Server Created for Assignment 1"

@app.route("/sum", methods=['POST'])
def sum():
            data = request.get_json()
            a = data.get("a")
            b = data.get("b")
            result = {"Addition": a + b}
            return jsonify(result)
@app.route("/multiply", methods=['POST'])
def multiply():
        data = request.get_json()
        a = data.get("a")
        b = data.get("b")
        result = {"product": a * b}
        return jsonify(result)
@app.route("/subtraction", methods=['POST'])
def subtract():
        data = request.get_json()
        a = data.get("a")
        b = data.get("b")
        result = {"subtraction": a - b}
        return jsonify(result)
if __name__ == "__main__":
    app.run(debug=True)