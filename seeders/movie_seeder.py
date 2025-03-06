# seeders/movie_seeder.py
import sys
import os
import tensorflow_datasets as tfds
from extensions import db
from app import app
from models.movie import Movie

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# MovieLens 100k genre mapping (verified against official docs)
genre_map = {
    0: "Unknown", 1: "Action", 2: "Adventure", 3: "Animation", 4: "Children",
    5: "Comedy", 6: "Crime", 7: "Documentary", 8: "Drama", 9: "Fantasy",
    10: "Film-Noir", 11: "Horror", 12: "Musical", 13: "Mystery", 14: "Romance",
    15: "Sci-Fi", 16: "Thriller", 17: "War", 18: "Western"
}

def seed_movie():
    with app.app_context():
        dataset = tfds.load("movielens/100k-movies", split="train")
        print("Seeding movies from MovieLens 100k (all movies)...")
        
        batch_size = 100
        counter = 0
        
        db.session.query(Movie).delete()
        db.session.commit()

        for movie in dataset:
            movie_id = movie["movie_id"].numpy().decode('utf-8')
            movie_title = movie["movie_title"].numpy().decode('utf-8')
            genre_ids = movie["movie_genres"].numpy().tolist()
            # Filter out invalid genre IDs and map to names
            valid_genre_ids = [gid for gid in genre_ids if gid in genre_map]
            movie_genres = ", ".join(genre_map[gid] for gid in valid_genre_ids) or "Unknown"
            print(f"Seeding: ID={movie_id}, Title={movie_title}, Genres={movie_genres}")

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