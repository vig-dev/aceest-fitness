from flask import Flask, jsonify, request
from services.member_service import get_all_members, add_member
from services.plan_service import get_all_plans, add_plan, get_plan_by_id
from services.member_service import (
    get_all_members,
    add_member,
    get_member_by_id,
    update_member,
    delete_member
)

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
        "version": "ACEest Fitness App - Version 4 Running"
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


@app.route("/members/<int:member_id>", methods=["GET"])
def get_member(member_id):
    member = get_member_by_id(member_id)
    if not member:
        return jsonify({"error": "Member not found"}), 404
    return jsonify(member)


@app.route("/members", methods=["POST"])
def create_member():
    result, status = add_member(request.get_json())
    return jsonify(result), status


@app.route("/members/<int:member_id>", methods=["PUT"])
def update_member_api(member_id):
    result, status = update_member(member_id, request.get_json())
    return jsonify(result), status


@app.route("/members/<int:member_id>", methods=["DELETE"])
def delete_member_api(member_id):
    result, status = delete_member(member_id)
    return jsonify(result), status


@app.route("/plans", methods=["GET"])
def get_plans():
    return jsonify(get_all_plans())


@app.route("/plans/<int:plan_id>", methods=["GET"])
def get_plan(plan_id):
    plan = get_plan_by_id(plan_id)
    if not plan:
        return jsonify({"error": "Plan not found"}), 404
    return jsonify(plan)


@app.route("/plans", methods=["POST"])
def create_plan():
    result, status = add_plan(request.get_json())
    return jsonify(result), status


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)