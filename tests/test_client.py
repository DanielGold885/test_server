import pytest
from client.api_client import UserApiClient

BASE_URL = "http://127.0.0.1:8000"

@pytest.fixture(scope="module")
def client():
    return UserApiClient(BASE_URL)

def test_health_check(client):
    response = client.health_check()
    assert response == {"status": "ok"}

def test_create_and_get_user(client):
    user = {
        "id": "111222333",
        "name": "Test User",
        "phone": "+972501112222",
        "address": "Tel Aviv"
    }
    response = client.create_user(user)
    assert response["id"] == user["id"]

    fetched = client.get_user(user["id"])
    assert fetched["name"] == user["name"]

def test_duplicate_user(client):
    user = {
        "id": "999999999",
        "name": "Duplicate User",
        "phone": "+972509999999",
        "address": "Haifa"
    }
    client.create_user(user)
    with pytest.raises(ValueError, match="Bad Request"):
        client.create_user(user)

def test_get_nonexistent_user(client):
    with pytest.raises(ValueError, match="Resource not found"):
        client.get_user("000000000")

def test_list_users(client):
    ids = client.list_users()
    assert isinstance(ids, list)
    assert all(isinstance(uid, str) for uid in ids)
