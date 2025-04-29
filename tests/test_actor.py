import pytest
import json
from unittest.mock import patch
from tests.config import app, client, init_database, user_token, admin_token
from extensions import db
from models.actor import Actor

@pytest.mark.usefixtures("init_database")
def test_get_all_actors_success(client, user_token):
    headers = {"Authorization": f"Bearer {user_token}"}
    response = client.get("/actors", headers=headers)
    data = json.loads(response.data)

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) == 2
    assert data[0]["name"] == "Test Actor"
    assert data[0]["birthday"] == "1990-01-01T00:00:00"

@pytest.mark.usefixtures("init_database")
def test_create_actor_success(client, admin_token):
    headers = {"Authorization": f"Bearer {admin_token}"}
    data = {
        "name": "New Actor",
        "description": "New description",
        "previous_work": "New work",
        "birthday": "1985-01-01",
        "nationality": "United States"  
    }
    response = client.post("/actors", json=data, headers=headers)
    data = json.loads(response.data)

    assert response.status_code == 201
    assert data["name"] == "New Actor"
    assert data["message"] == "Actor created successfully"

@pytest.mark.usefixtures("init_database")
def test_create_actor_invalid_birthday(client, admin_token):
    headers = {"Authorization": f"Bearer {admin_token}"}
    data = {
        "name": "Invalid Actor",
        "birthday": "invalid-date"
    }
    response = client.post("/actors", json=data, headers=headers)
    data = json.loads(response.data)

    assert response.status_code == 400
    assert data["error"] == "Birthday must be in YYYY-MM-DD format"  

@pytest.mark.usefixtures("init_database")
def test_get_actor_success(client, user_token):
    headers = {"Authorization": f"Bearer {user_token}"}
    response = client.get("/actors/1", headers=headers)
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data["name"] == "Test Actor"
    assert data["movies"][0]["id"] == "tt0000001"

@pytest.mark.usefixtures("init_database")
def test_get_actor_not_found(client, user_token):
    headers = {"Authorization": f"Bearer {user_token}"}
    response = client.get("/actors/999", headers=headers)

    assert response.status_code == 404

@pytest.mark.usefixtures("init_database")
def test_update_actor_success(client, admin_token):
    headers = {"Authorization": f"Bearer {admin_token}"}
    data = {
        "name": "Updated Actor",
        "description": "Updated description",
        "nationality": "United States"  
    }
    response = client.put("/actors/1", json=data, headers=headers)
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data["name"] == "Updated Actor"
    assert data["message"] == "Actor updated successfully"

@pytest.mark.usefixtures("init_database")
def test_delete_actor_success(client, admin_token):
    headers = {"Authorization": f"Bearer {admin_token}"}
    response = client.delete("/actors/1", headers=headers)
    data = json.loads(response.data)

    assert response.status_code == 200
    assert "message" in data
    assert "Test Actor deleted successfully" in data["message"]

@pytest.mark.usefixtures("init_database")
def test_remove_actor_from_movie_success(client, admin_token):
    headers = {"Authorization": f"Bearer {admin_token}"}
    response = client.delete("/movies/tt0000001/actors/1", headers=headers)
    data = json.loads(response.data)

    assert response.status_code == 200
    assert "message" in data
    assert "Actor Test Actor removed from movie Test Movie" in data["message"]  