import pytest
import json
from tests.config import app, client, init_database, user_token

@pytest.mark.usefixtures("init_database")
def test_create_review_success(client, user_token):
    headers = {"Authorization": f"Bearer {user_token}"}
    data = {"movie_id": "tt0000001", "content": "Amazing movie!"}
    response = client.post("/reviews/create", json=data, headers=headers)
    response_data = json.loads(response.data)

    assert response.status_code == 201
    assert response_data["content"] == "Amazing movie!"
    assert response_data["message"] == "Review created successfully"

@pytest.mark.usefixtures("init_database")
def test_get_movie_reviews_success(client, user_token):
    headers = {"Authorization": f"Bearer {user_token}"}
    response = client.get("/reviews/movie/tt0000001", headers=headers)
    data = json.loads(response.data)

    assert response.status_code == 200
    assert "reviews" in data
    assert len(data["reviews"]) == 1
    assert data["reviews"][0]["content"] == "Great movie!"

@pytest.mark.usefixtures("init_database")
def test_update_review_success(client, user_token):
    headers = {"Authorization": f"Bearer {user_token}"}
    data = {"content": "Updated review"}
    response = client.put("/reviews/update/1", json=data, headers=headers)
    response_data = json.loads(response.data)

    assert response.status_code == 200
    assert response_data["content"] == "Updated review"
    assert response_data["message"] == "Review updated successfully"

@pytest.mark.usefixtures("init_database")
def test_delete_review_success(client, user_token):
    headers = {"Authorization": f"Bearer {user_token}"}
    response = client.delete("/reviews/delete/1", headers=headers)
    response_data = json.loads(response.data)

    assert response.status_code == 200
    assert response_data["message"] == "Review deleted successfully"