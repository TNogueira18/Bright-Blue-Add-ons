from flask import Flask, jsonify, request

app = Flask(__name__)

# Simulated sensor data
sensors_data = {
    "production": 75.5,
    "ph": 7.2,
    "rp": 700,
    "temperature": 26.5,
    "salt": 3.1
}

@app.route("/api", methods=["GET"])
def get_data():
    return jsonify(sensors_data)

@app.route("/api/ph", methods=["POST"])
def set_ph():
    data = request.get_json()
    if "ph" in data:
        sensors_data["ph"] = data["ph"]
        return jsonify({"message": "pH updated"}), 200
    return jsonify({"error": "Invalid data"}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
