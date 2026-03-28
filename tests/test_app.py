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
        "plan": "Platinum"
    })
    assert response.status_code == 201