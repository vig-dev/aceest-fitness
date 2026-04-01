plans = [
    {"id": 1, "name": "Gold", "price": 3000, "duration": "3 months"},
    {"id": 2, "name": "Silver", "price": 2000, "duration": "2 months"}
]


def get_all_plans():
    return plans


def get_plan_by_id(plan_id):
    for plan in plans:
        if plan["id"] == plan_id:
            return plan
    return None


def add_plan(data):
    if not data or "name" not in data or "price" not in data:
        return {"error": "Invalid input"}, 400

    new_plan = {
        "id": len(plans) + 1,
        "name": data["name"],
        "price": data["price"],
        "duration": data.get("duration", "1 month")
    }

    plans.append(new_plan)
    return new_plan, 201