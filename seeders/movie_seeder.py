import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from extensions import db
from models.movie import Movie
import random
from app import app
from faker import Faker

fake = Faker()

NUM_MOVIES = 5

def seed_movie():
    with app.app_context():
        for _ in range(NUM_MOVIES):
            movie = Movie(
                movie_title=fake.sentence(nb_words=1),
                movie_genres=random.choice(["Action", "Comedy", "Drama", "Horror", "Sci-Fi"]),
                movie_ratings=round(random.uniform(1.0, 5.0), 1),
            )
            db.session.add(movie)
            db.session.commit()

        print(f"{NUM_MOVIES} fake movies seeded successfully")

if __name__ == "__main__":
    print("Starting Movie Seeding..")
    seed_movie()
    print("Movie Seeding Complete..")
