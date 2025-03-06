# seeders/movie_seeder.py
import sys
import os
import tensorflow_datasets as tfds
from extensions import db
from app import app
from models.movie import Movie

# Add the root directory to sys.path (one level up from seeders/)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def seed_movie():
    with app.app_context():
        # Load the MovieLens 100k movies dataset
        dataset = tfds.load("movielens/100k-movies", split="train")
        print("Seeding movies from MovieLens 100k...")
        
        batch_size = 100  # Batch commits for performance
        counter = 0
        
        for movie in dataset:
            movie_id = movie["movie_id"].numpy().decode('utf-8')
            movie_title = movie["movie_title"].numpy().decode('utf-8')
            # No genre data in this TFDS split; use a default
            movie_genres = "Unknown"  # Placeholder since genres aren’t available

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

        # Final commit for remaining movies
        db.session.commit()
        print(f"Seeded {Movie.query.count()} movies successfully.")

if __name__ == "__main__":
    print("Starting Movie Seeding...")
    seed_movie()
    print("Movie Seeding Complete.")