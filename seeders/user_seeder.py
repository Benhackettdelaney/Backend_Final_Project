# seeders/user_seeder.py
import sys
import os
import tensorflow_datasets as tfds
from extensions import db, ratings_table
from app import app
from models.user import User
from models.movie import Movie

# Add the root directory to sys.path (one level up from seeders/)
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def seed_user():
    with app.app_context():
        # Seed admin user
        admin_email = "admin@moviemuse.com"
        admin_password = "adminpassword"
        
        existing_admin = User.query.filter_by(email=admin_email).first()
        if not existing_admin:
            admin_user = User(
                email=admin_email,
                password=admin_password,
                user_gender=0,
                user_occupation_label=0,
                raw_user_age=30,
                user_rating=0.0,
                role="admin"
            )
            db.session.add(admin_user)
            db.session.commit()
            print("Admin user created.")

        # Load the MovieLens 100k ratings dataset
        ratings_dataset = tfds.load("movielens/100k-ratings", split="train")
        user_map = {}
        batch_size = 1000
        counter = 0
        new_users = []  # Track new users to commit

        print("Seeding users and ratings from MovieLens 100k...")
        for rating in ratings_dataset:
            user_id = rating["user_id"].numpy().decode('utf-8')
            movie_id = rating["movie_id"].numpy().decode('utf-8')
            user_rating = float(rating["user_rating"].numpy())
            user_gender = rating["user_gender"].numpy()
            user_age = rating["raw_user_age"].numpy()
            user_occupation_label = rating["user_occupation_label"].numpy()

            # Check if user already exists in the database or user_map
            if user_id not in user_map:
                email = f"user{user_id}@moviemuse.com"
                existing_user = User.query.filter_by(email=email).first()
                if not existing_user:
                    new_user = User(
                        email=email,
                        password="password",
                        user_gender=user_gender,
                        user_occupation_label=user_occupation_label,
                        raw_user_age=user_age,
                        user_rating=0.0,
                        role="user"
                    )
                    db.session.add(new_user)
                    new_users.append(new_user)  # Add to list for batch commit
                    user_map[user_id] = None  # Placeholder until committed
                else:
                    user_map[user_id] = existing_user.id

            # Associate rating with movie if it exists
            movie = Movie.query.filter_by(id=movie_id).first()
            if movie and user_map[user_id] is not None:  # Only if user_id is set
                existing_rating = db.session.query(ratings_table).filter_by(
                    user_id=user_map[user_id], movie_id=movie.id
                ).first()
                if not existing_rating:
                    db.session.execute(
                        ratings_table.insert().values(
                            user_id=user_map[user_id],
                            movie_id=movie.id,
                            rating=user_rating
                        )
                    )

            counter += 1
            if counter % batch_size == 0:
                # Commit new users first to assign IDs
                if new_users:
                    db.session.commit()
                    for user in new_users:
                        user_map[user.email.split('@')[0][4:]] = user.id  # Update user_map with actual IDs
                    new_users.clear()
                db.session.commit()  # Commit ratings
                print(f"Committed {counter} ratings...")

        # Final commit for remaining records
        if new_users:
            db.session.commit()
            for user in new_users:
                user_map[user.email.split('@')[0][4:]] = user.id
        db.session.commit()
        print(f"Seeded {len(user_map)} users and {counter} ratings successfully.")

if __name__ == "__main__":
    print("Starting User Seeding...")
    seed_user()
    print("User Seeding Complete.")