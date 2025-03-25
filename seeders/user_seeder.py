# seeders/user_seeder.py
import sys
import os
import tensorflow_datasets as tfds
from extensions import db
from app import app
from models.user import User
from models.movie import Movie
from models.rating import Rating
from models.reviews import Review
from models.watchlist import Watchlist  # Ensure Watchlist model is imported
from flask_bcrypt import Bcrypt
from faker import Faker
import random

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

bcrypt = Bcrypt()
fake = Faker()

def seed_user():
    with app.app_context():
        # Seed the admin user
        admin_email = "admin@moviemuse.com"
        admin_password = "adminpassword"
        
        existing_admin = User.query.filter_by(email=admin_email).first()
        if not existing_admin:
            hashed_admin_password = bcrypt.generate_password_hash(admin_password).decode('utf-8')
            admin_user = User(
                username="admin",
                email=admin_email,
                password=hashed_admin_password,
                user_gender=0,
                user_occupation_label=0,
                raw_user_age=30,
                user_rating=0.0,
                role="admin"
            )
            db.session.add(admin_user)
            db.session.commit()
            print("Admin user created.")
        else:
            admin_user = existing_admin

        # Load all movies from the database
        all_movies = Movie.query.all()
        if not all_movies:
            print("No movies found in the database. Please seed movies first.")
            return
        movie_ids = [movie.id for movie in all_movies]
        total_movies = len(movie_ids)
        print(f"Found {total_movies} movies in the database.")

        # Seed 10 regular users
        max_users = 10
        user_map = {}
        new_users = []

        if not existing_admin:
            user_map["admin"] = admin_user.id

        print(f"Seeding {max_users} users with 1 review and 1 rating per movie, plus private and public watchlists...")

        # Use MovieLens data for initial user info
        ratings_dataset = list(tfds.load("movielens/100k-ratings", split="train"))
        counter = 0

        for rating in ratings_dataset:
            user_id = rating["user_id"].numpy().decode('utf-8')
            user_gender = int(rating["user_gender"].numpy())
            user_age = int(rating["raw_user_age"].numpy())
            user_occupation_label = int(rating["user_occupation_label"].numpy())

            if user_id not in user_map and len(user_map) < max_users:
                email = f"user{user_id}@moviemuse.com"
                max_attempts = 5
                for attempt in range(max_attempts):
                    username = fake.user_name()
                    if not User.query.filter_by(username=username).first():
                        break
                    if attempt == max_attempts - 1:
                        username = f"{fake.user_name()}{user_id}"
                
                existing_user = User.query.filter_by(email=email).first()
                if not existing_user:
                    hashed_password = bcrypt.generate_password_hash("password123").decode('utf-8')
                    new_user = User(
                        username=username,
                        email=email,
                        password=hashed_password,
                        user_gender=user_gender,
                        user_occupation_label=user_occupation_label,
                        raw_user_age=user_age,
                        user_rating=0.0,
                        role="user"
                    )
                    db.session.add(new_user)
                    new_users.append(new_user)
                    user_map[user_id] = None  # Temporarily None until committed

            counter += 1
            if counter >= max_users:
                break

        # Commit the new users and assign their IDs
        if new_users:
            db.session.commit()
            for new_user in new_users:
                user_map[new_user.email.split('@')[0][4:]] = new_user.id
            print(f"Seeded {len(new_users)} new users.")

        # Prepare user IDs for random assignment
        user_ids = [user_id for user_id_str, user_id in user_map.items() if user_id]  # Exclude None values
        counter = 0
        batch_size = 1000  # Commit in batches

        # Seed 1 review and 1 rating per movie
        for movie_id in movie_ids:
            movie = Movie.query.get(movie_id)
            if movie:
                # Seed 1 review with a random user
                reviewer_id = random.choice(user_ids)
                if not Review.query.filter_by(user_id=reviewer_id, movie_id=movie_id).first():
                    review_content = f"{fake.sentence()} The {fake.word()} was {fake.word()} and the {fake.word()} really {fake.word()} the experience."
                    new_review = Review(
                        user_id=reviewer_id,
                        movie_id=movie_id,
                        content=review_content
                    )
                    db.session.add(new_review)
                    counter += 1

                # Seed 1 rating with a random user
                rater_id = random.choice(user_ids)
                if not Rating.query.filter_by(user_id=rater_id, movie_id=movie_id).first():
                    rating_value = float(fake.random_int(min=1, max=5))
                    new_rating = Rating(
                        user_id=rater_id,
                        movie_id=movie_id,
                        rating=rating_value
                    )
                    db.session.add(new_rating)
                    counter += 1

            # Commit in batches
            if counter % batch_size == 0:
                db.session.commit()
                print(f"Committed {counter} ratings and reviews...")

        # Seed watchlists for each user
        for user_id in user_ids:
            # Seed 1 private watchlist
            if not Watchlist.query.filter_by(user_id=user_id, title="My Private List").first():
                private_movie_ids = random.sample(movie_ids, min(3, len(movie_ids)))  # 3 random movies
                new_private_watchlist = Watchlist(
                    user_id=user_id,
                    title="My Private List",
                    movie_ids=private_movie_ids,
                    is_public=False
                )
                db.session.add(new_private_watchlist)
                counter += 1

            # Seed 1 public watchlist
            if not Watchlist.query.filter_by(user_id=user_id, title="My Public Favorites").first():
                public_movie_ids = random.sample(movie_ids, min(4, len(movie_ids)))  # 4 random movies
                new_public_watchlist = Watchlist(
                    user_id=user_id,
                    title="My Public Favorites",
                    movie_ids=public_movie_ids,
                    is_public=True
                )
                db.session.add(new_public_watchlist)
                counter += 1

        # Final commit for remaining records
        db.session.commit()

        total_ratings = Rating.query.count()
        total_reviews = Review.query.count()
        total_watchlists = Watchlist.query.count()
        print(f"Seeded {len(user_map)} users with {total_ratings} ratings, {total_reviews} reviews, and {total_watchlists} watchlists successfully.")

if __name__ == "__main__":
    print("Starting User Seeding...")
    seed_user()