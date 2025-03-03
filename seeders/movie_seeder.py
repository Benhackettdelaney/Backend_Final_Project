import sys
import os
import tensorflow_datasets as tfds
from extensions import db
from models.movie import Movie
import random
from app import app

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

NUM_MOVIES = 20

def seed_movie():
    with app.app_context():
        dataset = tfds.load("movielens/100k-movies", split="train")

        for i, movie in enumerate(dataset):
            if i >= NUM_MOVIES:
                break
            movie_data = movie["movie_title"].numpy().decode('utf-8')
            movie_genres = random.choice(["Action", "Comedy", "Drama", "Children", "Adventure", "Crime", "Unknown"])
            
            new_movie = Movie(
                movie_title=movie_data,
                movie_genres=movie_genres,
            )
            
        db.session.add(new_movie)
        db.session.commit() 
        print(f"{NUM_MOVIES} movies seeded successfully.")

if __name__ == "__main__":
    print("Starting Movie Seeding...")
    seed_movie()
    print("Movie Seeding Complete.")
