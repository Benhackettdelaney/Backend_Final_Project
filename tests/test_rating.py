import pytest
import json
from tests.config import app, client, init_database, user_token

@pytest.mark.usefixtures("init_database")
def test_add_rating_success(client, user_token):
    headers = {"Authorization": f"Bearer {user_token}"}
    data = {"movie_id": "tt0000001", "rating": 4.0}
    response = client.post("/ratings", json=data, headers=headers)
    response_data = json.loads(response.data)

    assert response.status_code == 200
    assert "message" in response_data

@pytest.mark.usefixtures("init_database")
def test_add_rating_invalid_rating(client, user_token):
    headers = {"Authorization": f"Bearer {user_token}"}
    data = {"movie_id": "tt0000001", "rating": 6.0}
    response = client.post("/ratings", json=data, headers=headers)
    data = json.loads(response.data)

    assert response.status_code == 400
    assert "error" in data

@pytest.mark.usefixtures("init_database")
def test_get_user_ratings_success(client, user_token):
    headers = {"Authorization": f"Bearer {user_token}"}
    response = client.get("/ratings", headers=headers)
    data = json.loads(response.data)

    assert response.status_code == 200
    assert "rated_movies" in data
    assert len(data["rated_movies"]) == 1

@pytest.mark.usefixtures("init_database")
def test_update_rating_success(client, user_token):
    headers = {"Authorization": f"Bearer {user_token}"}
    data = {"rating": 3.5}
    response = client.put("/ratings/1", json=data, headers=headers)
    response_data = json.loads(response.data)

    assert response.status_code == 200
    assert response_data["rating"] == 3.5

@pytest.mark.usefixtures("init_database")
def test_delete_rating_success(client, user_token):
    headers = {"Authorization": f"Bearer {user_token}"}
    response = client.delete("/ratings/1", headers=headers)
    response_data = json.loads(response.data)

    assert response.status_code == 200
    assert "message" in response_data