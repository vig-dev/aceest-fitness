from flask import Flask, jsonify, request
from services.member_service import get_all_members, add_member

app = Flask(__name__)

gym_info = {
    "name": "ACEest Fitness & Gym",
    "location": "Mumbai",
    "status": "Active"
}


@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to ACEest Fitness API",
        "version": "v3"
    })


@app.route("/health")
def health():
    return jsonify({"status": "UP"})


@app.route("/gym")
def get_gym_info():
    return jsonify(gym_info)


@app.route("/members", methods=["GET"])
def get_members():
    return jsonify(get_all_members())


@app.route("/members", methods=["POST"])
def create_member():
    result, status = add_member(request.get_json())
    return jsonify(result), status


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)