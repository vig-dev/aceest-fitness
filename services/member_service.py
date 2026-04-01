members = [
    {"id": 1, "name": "John", "plan_id": 1},
    {"id": 2, "name": "Sara", "plan_id": 2}
]


def get_all_members():
    return members


def get_member_by_id(member_id):
    for member in members:
        if member["id"] == member_id:
            return member
    return None


def add_member(data):
    if not data or "name" not in data or "plan_id" not in data:
        return {"error": "Invalid input"}, 400

    new_member = {
        "id": len(members) + 1,
        "name": data["name"],
        "plan_id": data["plan_id"]
    }

    members.append(new_member)
    return new_member, 201


def update_member(member_id, data):
    member = get_member_by_id(member_id)
    if not member:
        return {"error": "Member not found"}, 404

    member["name"] = data.get("name", member["name"])
    member["plan_id"] = data.get("plan_id", member["plan_id"])

    return member, 200


def delete_member(member_id):
    global members
    member = get_member_by_id(member_id)

    if not member:
        return {"error": "Member not found"}, 404

    members = [m for m in members if m["id"] != member_id]
    return {"message": "Member deleted"}, 200