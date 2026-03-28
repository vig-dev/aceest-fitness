from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to ACEest Fitness API",
        "version": "v1"
    })

@app.route("/health")
def health():
    return jsonify({
        "status": "UP"
    })

@app.route("/gym")
def gym_info():
    return jsonify({
        "name": "ACEest Fitness & Gym",
        "status": "active"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)