members = [
    {"id": 1, "name": "John", "plan": "Gold"},
    {"id": 2, "name": "Sara", "plan": "Silver"}
]


def get_all_members():
    return members


def add_member(data):
    if not data or "name" not in data or "plan" not in data:
        return {"error": "Invalid input"}, 400

    new_member = {
        "id": len(members) + 1,
        "name": data["name"],
        "plan": data["plan"]
    }

    members.append(new_member)

    return new_member, 201