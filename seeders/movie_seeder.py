# seeders/movie_seeder.py
import sys
import os
import tensorflow_datasets as tfds
from extensions import db
from app import app
from models.movie import Movie
from models.actor import Actor  
from faker import Faker
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

fake = Faker()

genre_map = {
    0: "Unknown", 1: "Action", 2: "Adventure", 3: "Animation", 4: "Children",
    5: "Comedy", 6: "Crime", 7: "Documentary", 8: "Drama", 9: "Fantasy",
    10: "Film-Noir", 11: "Horror", 12: "Musical", 13: "Mystery", 14: "Romance",
    15: "Sci-Fi", 16: "Thriller", 17: "War", 18: "Western"
}

def seed_movies():
    with app.app_context():
        dataset = list(tfds.load("movielens/100k-movies", split="train"))
        print("Seeding movies from MovieLens 100k (all movies with 4 actors each)...")
        
        batch_size = 100
        counter = 0
        
        all_actors = Actor.query.all()
        if len(all_actors) < 4:
            print("Error: Need at least 4 actors in the database. Run actor_seeder.py first.")
            return

        try:
            db.session.query(Movie).delete()
            db.session.commit()
            print("Cleared existing movies.")
        except Exception as e:
            print(f"Error deleting existing movies: {e}")
            db.session.rollback()
            return

        for movie in dataset:
            movie_id = movie["movie_id"].numpy().decode('utf-8')
            movie_title = movie["movie_title"].numpy().decode('utf-8')
            genre_ids = movie["movie_genres"].numpy().tolist()
            valid_genre_ids = [gid for gid in genre_ids if gid in genre_map]
            movie_genres = ", ".join(genre_map[gid] for gid in valid_genre_ids) or "Unknown"
            description = fake.paragraph(nb_sentences=2)
            
            existing_movie = Movie.query.filter_by(id=movie_id).first()
            if not existing_movie:
                selected_actors = random.sample(all_actors, 4)
                new_movie = Movie(
                    id=movie_id,
                    movie_title=movie_title,
                    movie_genres=movie_genres,
                    description=description
                )
                new_movie.actors.extend(selected_actors)  
                db.session.add(new_movie)
            
            counter += 1
            if counter % batch_size == 0:
                try:
                    db.session.commit()
                    print(f"Committed {counter} movies...")
                except Exception as e:
                    print(f"Error committing batch at {counter} movies: {e}")
                    db.session.rollback()
                    return

        try:
            db.session.commit()
            total_movies = Movie.query.count()
            total_actors = Actor.query.count()
            print(f"Seeded {total_movies} movies with actors from a pool of {total_actors} actors successfully.")
            sample_movie = Movie.query.first()
            if sample_movie:
                print(f"Sample Movie: ID={sample_movie.id}, Title={sample_movie.movie_title}, Genres={sample_movie.movie_genres}, "
                      f"Description={sample_movie.description}, Actors={[actor.name for actor in sample_movie.actors.all()]}")
        except Exception as e:
            print(f"Final movie commit failed: {e}")
            db.session.rollback()

if __name__ == "__main__":
    print("Starting Movie Seeding...")
    seed_movies()