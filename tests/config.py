# tests/config.py
import pytest
import numpy as np
import os
import sys
from app import create_app
from extensions import db
from models.movie import Movie
from models.user import User
from models.actor import Actor
from models.rating import Rating
from models.reviews import Review
from models.watchlist import Watchlist
from flask_jwt_extended import create_access_token
from unittest.mock import MagicMock
from datetime import datetime

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

class TestConfig:
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = 'test-secret-key'
    JWT_TOKEN_LOCATION = ['headers']
    JWT_COOKIE_CSRF_PROTECT = False
    JWT_ACCESS_TOKEN_EXPIRES = 3600

@pytest.fixture
def app():
    app = create_app(TestConfig)
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture
def client(app):
    return app.test_client()

@pytest.fixture
def init_database(app):
    with app.app_context():
        user = User(
            id=1,
            username="testuser",
            email="testuser@example.com",
            password="testpass",
            user_gender=1,
            user_occupation_label=1,
            raw_user_age=30,
            user_rating=4.0,
            role="user"
        )
        admin = User(
            id=2,
            username="adminuser",
            email="adminuser@example.com",
            password="adminpass",
            user_gender=1,
            user_occupation_label=1,
            raw_user_age=40,
            user_rating=4.5,
            role="admin"
        )
        db.session.add_all([user, admin])

        actor = Actor(
            id=1,
            name="Test Actor",
            description="Test description",
            previous_work="Test work",
            birthday=datetime.strptime("1990-01-01", "%Y-%m-%d"),
            nationality="Test nationality"
        )
        actor2 = Actor(
            id=2,
            name="Second Actor",
            description="Another description",
            previous_work="More work",
            birthday=datetime.strptime("1980-01-01", "%Y-%m-%d"),
            nationality="Another nationality"
        )
        db.session.add_all([actor, actor2])

        movie = Movie(
            id="tt0000001",
            movie_title="Test Movie",
            movie_genres="Action",
            description="A test movie",
            image_url="movies/bloodborne1.jpg"
        )
        movie.actors.append(actor)
        db.session.add(movie)

        rating = Rating(
            id=1,
            user_id=1,
            movie_id="tt0000001",
            rating=4.5
        )
        db.session.add(rating)

        review = Review(
            id=1,
            user_id=1,
            movie_id="tt0000001",
            content="Great movie!"
        )
        db.session.add(review)

        watchlist = Watchlist(
            id=1,
            user_id=1,
            title="Test Watchlist",
            movie_ids=["tt0000001"],
            is_public=True
        )
        db.session.add(watchlist)

        db.session.commit()
        yield db

@pytest.fixture
def user_token(app):
    with app.app_context():
        return create_access_token(identity="1")

@pytest.fixture
def admin_token(app):
    with app.app_context():
        return create_access_token(identity="2")

@pytest.fixture
def mock_ranking_model():
    mock_model = MagicMock()
    mock_model.return_value = MagicMock(numpy=lambda: np.array([0.9, 0.8, 0.7, 0.6, 0.5]))
    return mock_model