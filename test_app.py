import pytest

from app import app

from test_inputs import (
    CREATE_USER_VALID_INPUT,
    CREATE_USER_MISSING_NAME,
    CREATE_USER_MISSING_EMAIL,
    CREATE_USER_MISSING_PLAN,
)


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
        json=CREATE_USER_VALID_INPUT
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
        json=CREATE_USER_MISSING_NAME
    )

    assert response.status_code == 400


def test_create_user_requires_email(client):
    response = client.post(
        "/api/create-user",
        json=CREATE_USER_MISSING_EMAIL
    )

    assert response.status_code == 400


def test_create_user_requires_plan(client):
    response = client.post(
        "/api/create-user",
        json=CREATE_USER_MISSING_PLAN
    )

    assert response.status_code == 400