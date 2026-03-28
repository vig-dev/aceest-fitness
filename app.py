from flask import Flask, jsonify, request

app = Flask(__name__)

# Existing gym info
gym_info = {
    "name": "ACEest Fitness & Gym",
    "location": "Mumbai",
    "status": "Active"
}

# NEW: In-memory member storage
members = [
    {"id": 1, "name": "John", "plan": "Gold"},
    {"id": 2, "name": "Sara", "plan": "Silver"}
]


@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to ACEest Fitness API",
        "version": "v2"
    })


@app.route("/health")
def health():
    return jsonify({"status": "UP"})


@app.route("/gym")
def get_gym_info():
    return jsonify(gym_info)


# 🔹 NEW: GET all members
@app.route("/members", methods=["GET"])
def get_members():
    return jsonify(members)


# 🔹 NEW: ADD member
@app.route("/members", methods=["POST"])
def add_member():
    data = request.get_json()

    # Basic validation
    if not data or "name" not in data or "plan" not in data:
        return jsonify({"error": "Invalid input"}), 400

    new_member = {
        "id": len(members) + 1,
        "name": data["name"],
        "plan": data["plan"]
    }

    members.append(new_member)

    return jsonify(new_member), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)