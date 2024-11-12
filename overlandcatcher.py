from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/json", methods=["POST"])
def json():
    if request.is_json:
        req = request.get_json()
        response = {
                "message": "JSON recd",
                "name": req.get("name")
        }
        res = make_response(jsonify(response),200)
        return res 
    else:
        res = make_response(jsonify({"message": "No JSON recd"}), 418) 
        return res 

