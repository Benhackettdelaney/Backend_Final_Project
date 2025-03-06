# seeders/movie_seeder.py
import sys
import os
import tensorflow_datasets as tfds
from extensions import db
from app import app
from models.movie import Movie

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def seed_movie():
    with app.app_context():
        dataset = tfds.load("movielens/100k-movies", split="train").take(30)  # Limit to 30 movies
        print("Seeding movies from MovieLens 100k (limited to 30 movies)...")
        
        batch_size = 100
        counter = 0
        
        for movie in dataset:
            movie_id = movie["movie_id"].numpy().decode('utf-8')
            movie_title = movie["movie_title"].numpy().decode('utf-8')
            movie_genres = "Unknown"

            existing_movie = Movie.query.filter_by(id=movie_id).first()
            if not existing_movie:
                new_movie = Movie(
                    id=movie_id,
                    movie_title=movie_title,
                    movie_genres=movie_genres
                )
                db.session.add(new_movie)
            
            counter += 1
            if counter % batch_size == 0:
                db.session.commit()
                print(f"Committed {counter} movies...")

        db.session.commit()
        print(f"Seeded {Movie.query.count()} movies successfully.")

if __name__ == "__main__":
    print("Starting Movie Seeding...")
    seed_movie()
