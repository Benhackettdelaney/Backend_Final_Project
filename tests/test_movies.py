import pytest
import json
from unittest.mock import patch
from tests.config import app, client, init_database, user_token, admin_token

@pytest.mark.usefixtures("init_database")
def test_get_movies_success(client, user_token):
    headers = {"Authorization": f"Bearer {user_token}"}
    response = client.get("/movies", headers=headers)
    data = json.loads(response.data)

    assert response.status_code == 200
    assert isinstance(data, list)
    assert len(data) == 1
    assert data[0]["id"] == "tt0000001"
    assert data[0]["movie_title"] == "Test Movie"
    assert data[0]["movie_genres"] == "Action"
    assert data[0]["actors"][0]["id"] == 1

@pytest.mark.usefixtures("init_database")
def test_get_movies_unauthorized(client):
    response = client.get("/movies")
    data = json.loads(response.data)

    assert response.status_code == 401
    assert "msg" in data

@pytest.mark.usefixtures("init_database")
def test_get_single_movie_success(client, user_token):
    headers = {"Authorization": f"Bearer {user_token}"}
    response = client.get("/movies/tt0000001", headers=headers)
    data = json.loads(response.data)

    assert response.status_code == 200
    assert data["id"] == "tt0000001"
    assert data["movie_title"] == "Test Movie"
    assert data["actors"][0]["id"] == 1

@pytest.mark.usefixtures("init_database")
def test_get_single_movie_not_found(client, user_token):
    headers = {"Authorization": f"Bearer {user_token}"}
    response = client.get("/movies/tt9999999", headers=headers)

    assert response.status_code == 404

@pytest.mark.usefixtures("init_database")
def test_create_movie_success(client, admin_token):
    headers = {"Authorization": f"Bearer {admin_token}"}
    data = {
        "id": "tt0000002",
        "movie_title": "New Movie",
        "movie_genres": "Comedy",
        "description": "A funny movie",
        "actor_id": 2,
        "image": "bloodborne1.jpg"
    }
    with patch("os.path.isfile", return_value=True):
        response = client.post("/movies/create", json=data, headers=headers)
        data = json.loads(response.data)

    assert response.status_code == 201
    assert data["movie_title"] == "New Movie"
    assert data["message"] == "Movie created successfully"
    assert data["actors"][0]["id"] == 2

@pytest.mark.usefixtures("init_database")
def test_create_movie_unauthorized(client, user_token):
    headers = {"Authorization": f"Bearer {user_token}"}
    data = {
        "id": "tt0000002",
        "movie_title": "New Movie",
        "movie_genres": "Comedy",
        "actor_id": 2,
        "image": "bloodborne1.jpg"
    }
    response = client.post("/movies/create", json=data, headers=headers)
    data = json.loads(response.data)

    assert response.status_code == 403
    assert data["error"] == "Admin access required"

@pytest.mark.usefixtures("init_database")
def test_update_movie_success(client, admin_token):
    headers = {"Authorization": f"Bearer {admin_token}"}
    data = {
        "movie_title": "Updated Movie",
        "movie_genres": "Drama",
        "description": "An updated movie",
        "image": "bloodborne1.jpg"
    }
    with patch("os.path.isfile", return_value=True):
        response = client.put("/movies/update/tt0000001", json=data, headers=headers)
        data = json.loads(response.data)

    assert response.status_code == 200
    assert data["movie_title"] == "Updated Movie"
    assert data["message"] == "Movie updated successfully"

@pytest.mark.usefixtures("init_database")
def test_delete_movie_success(client, admin_token):
    headers = {"Authorization": f"Bearer {admin_token}"}
    response = client.delete("/movies/delete/tt0000001", headers=headers)
    data = json.loads(response.data)

    assert response.status_code == 200
    assert "message" in data
    assert "Movie and associated ratings, reviews, and watchlist entries deleted successfully" in data["message"]

@pytest.mark.usefixtures("init_database")
def test_add_actor_success(client, admin_token):
    headers = {"Authorization": f"Bearer {admin_token}"}
    data = {"actor_id": 2}
    response = client.post("/movies/tt0000001/actors", json=data, headers=headers)
    data = json.loads(response.data)

    assert response.status_code == 200
    assert "message" in data
    assert "Second Actor added to movie Test Movie" in data["message"]

@pytest.mark.usefixtures("init_database")
def test_remove_actor_success(client, admin_token):
    headers = {"Authorization": f"Bearer {admin_token}"}
    response = client.delete("/movies/tt0000001/actors/1", headers=headers)
    data = json.loads(response.data)

    assert response.status_code == 200
    assert "message" in data
    assert "Test Actor deleted from database" in data["message"]