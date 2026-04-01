import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app import app

def test_home():
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

def test_health():
    client = app.test_client()
    response = client.get("/health")
    assert response.status_code == 200

def test_get_members():
    client = app.test_client()
    response = client.get("/members")
    assert response.status_code == 200

def test_add_member():
    client = app.test_client()
    response = client.post("/members", json={
        "name": "Alex",
        "plan_id": "Platinum"
    })
    assert response.status_code == 201

def test_get_plans():
    client = app.test_client()
    response = client.get("/plans")
    assert response.status_code == 200


def test_add_plan():
    client = app.test_client()
    response = client.post("/plans", json={
        "name": "Platinum",
        "price": 5000
    })
    assert response.status_code == 201


def test_get_member_by_id():
    client = app.test_client()
    response = client.get("/members/1")
    assert response.status_code == 200


def test_update_member():
    client = app.test_client()
    response = client.put("/members/1", json={
        "name": "Updated Name"
    })
    assert response.status_code == 200


def test_delete_member():
    client = app.test_client()
    response = client.delete("/members/1")
    assert response.status_code == 200