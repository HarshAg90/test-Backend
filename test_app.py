import pytest

from app import app


@pytest.fixture
def client():
    app.config["TESTING"] = True

    with app.test_client() as client:
        yield client


def test_health(client):
    response = client.get("/health")

    assert response.status_code == 200

    data = response.get_json()

    assert data["status"] == "ok"


def test_create_user(client):
    response = client.post(
        "/api/create-user",
        json={
            "name": "Harsh",
            "email": "harsh@example.com",
            "plan": "pro"
        }
    )

    assert response.status_code == 201

    data = response.get_json()

    assert data["message"] == "User created successfully"
    assert data["user"]["name"] == "Harsh"
    assert data["user"]["email"] == "harsh@example.com"
    assert data["user"]["plan"] == "pro"


def test_create_user_requires_name(client):
    response = client.post(
        "/api/create-user",
        json={
            "email": "harsh@example.com",
            "plan": "pro"
        }
    )

    assert response.status_code == 400


def test_create_user_requires_email(client):
    response = client.post(
        "/api/create-user",
        json={
            "name": "Harsh",
            "plan": "pro"
        }
    )

    assert response.status_code == 400


def test_create_user_requires_plan(client):
    response = client.post(
        "/api/create-user",
        json={
            "name": "Harsh",
            "email": "harsh@example.com"
        }
    )

    assert response.status_code == 400