# tests/test_watchlist.py
import pytest
import json
from tests.config import app, client, init_database, user_token

@pytest.mark.usefixtures("init_database")
def test_create_watchlist_success(client, user_token):
    headers = {"Authorization": f"Bearer {user_token}"}
    data = {"title": "New Watchlist", "movie_id": "tt0000001", "is_public": True}
    response = client.post("/watchlists/create", json=data, headers=headers)
    response_data = json.loads(response.data)

    assert response.status_code == 201
    assert response_data["message"] == "Watchlist created successfully"

@pytest.mark.usefixtures("init_database")
def test_get_user_watchlist_success(client, user_token):
    headers = {"Authorization": f"Bearer {user_token}"}
    response = client.get("/watchlists", headers=headers)
    data = json.loads(response.data)

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["title"] == "Test Watchlist"
    assert data[0]["movie_ids"] == ["tt0000001"]

@pytest.mark.usefixtures("init_database")
def test_get_watchlist_item_success(client, user_token):
    headers = {"Authorization": f"Bearer {user_token}"}
    response = client.get("/watchlists/1", headers=headers)
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data["title"] == "Test Watchlist"
    assert data["movie_ids"] == ["tt0000001"]

@pytest.mark.usefixtures("init_database")
def test_update_watchlist_success(client, user_token):
    headers = {"Authorization": f"Bearer {user_token}"}
    data = {"title": "Updated Watchlist", "is_public": False}
    response = client.put("/watchlists/update/1", json=data, headers=headers)
    response_data = json.loads(response.data)

    assert response.status_code == 200
    assert response_data["message"] == "Watchlist updated successfully"

@pytest.mark.usefixtures("init_database")
def test_delete_watchlist_success(client, user_token):
    headers = {"Authorization": f"Bearer {user_token}"}
    response = client.delete("/watchlists/delete/1", headers=headers)
    response_data = json.loads(response.data)

    assert response.status_code == 200
    assert response_data["message"] == "Watchlist deleted successfully"

@pytest.mark.usefixtures("init_database")
def test_get_public_watchlists_success(client):
    response = client.get("/watchlists/public")
    data = json.loads(response.data)

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["title"] == "Test Watchlist"

@pytest.mark.usefixtures("init_database")
def test_get_public_watchlist_success(client):
    response = client.get("/watchlists/public/1")
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data["title"] == "Test Watchlist"
    assert data["movies"][0]["id"] == "tt0000001"