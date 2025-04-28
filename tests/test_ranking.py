import pytest
import json
import numpy as np
from unittest.mock import patch, MagicMock
from tests.config import app, client, init_database, user_token, mock_ranking_model

@pytest.mark.usefixtures("init_database")
def test_get_top_ranked_movies_success(mock_ranking_model, client, user_token):
    mock_ranking_model.return_value = MagicMock(numpy=lambda: np.array([0.9]))
    headers = {"Authorization": f"Bearer {user_token}"}
    data = {"user_id": "1"}
    response = client.get("/ranking", json=data, headers=headers)
    response_data = json.loads(response.data)

    assert response.status_code == 200
    assert "top_ranked_movies" in response_data
    assert len(response_data["top_ranked_movies"]) == 1
    assert response_data["top_ranked_movies"][0]["id"] == "tt0000001"

@pytest.mark.usefixtures("init_database")
def test_get_top_ranked_movies_missing_user_id(client, user_token):
    headers = {"Authorization": f"Bearer {user_token}"}
    response = client.get("/ranking", headers=headers)
    data = json.loads(response.data)

    assert response.status_code == 400
    assert "error" in data