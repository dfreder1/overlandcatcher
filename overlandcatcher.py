from flask import Flask, request, jsonify, make_response

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/json", methods=["POST"])
def json():
    if request.is_json:
        req = request.get_json()
        incoming = {
            "locations": [
                {
                    "type": "Feature",
                    "geometry": {
                        "type": "Point",
                        "coordinates": [
                            -122.030581, 
                            37.331800
                        ]
                    },
                    "properties": {
                        "timestamp": "2015-10-01T08:00:00-0700", 
                        "altitude": 0,
                        "speed": 4,
                        "horizontal_accuracy": 30,
                        "vertical_accuracy": -1,
                        "motion": ["driving","stationary"],
                        "pauses": false,
                        "activity": "other_navigation",
                        "desired_accuracy": 100,
                        "deferred": 1000,
                        "significant_change": "disabled",
                        "locations_in_payload": 1,
                        "battery_state": "charging",
                        "battery_level": 0.80,
                        "device_id": "",
                        "wifi": ""
                    }
                }
            ]
        }
        res = make_response(jsonify(incoming),200)
        return res 
    else:
        res = make_response(jsonify({"message": "No JSON recd"}), 418) 
        return res 
                        
