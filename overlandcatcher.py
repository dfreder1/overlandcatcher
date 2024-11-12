from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/json", methods=["POST"])
def json():
    if request.is_json:
        req = request.get_json()
        print(type(req))
        print(req)
        return "JSON recd!", 200
    else:
        return "No JSON recd", 400

