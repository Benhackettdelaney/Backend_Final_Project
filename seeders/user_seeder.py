# seeders/user_seeder.py
import sys
import os
import tensorflow_datasets as tfds
from extensions import db, ratings_table
from app import app
from models.user import User
from models.movie import Movie

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def seed_user():
    with app.app_context():
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

        ratings_dataset = tfds.load("movielens/100k-ratings", split="train")
        user_map = {}
        batch_size = 1000
        counter = 0
        new_users = []
        max_users = 20  # Limit to 20 users (including admin)

        if not existing_admin:
            user_map["admin"] = admin_user.id

        print("Seeding users and ratings from MovieLens 100k (limited to 20 users)...")
        for rating in ratings_dataset:
            user_id = rating["user_id"].numpy().decode('utf-8')
            movie_id = rating["movie_id"].numpy().decode('utf-8')
            user_rating_value = float(rating["user_rating"].numpy())
            user_gender = int(rating["user_gender"].numpy())
            user_age = int(rating["raw_user_age"].numpy())
            user_occupation_label = int(rating["user_occupation_label"].numpy())

            if user_id not in user_map and len(user_map) < max_users:
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
                    new_users.append(new_user)
                    user_map[user_id] = None
                else:
                    user_map[user_id] = existing_user.id

            if user_id in user_map:
                movie = Movie.query.filter_by(id=movie_id).first()
                if movie and user_map[user_id] is not None:
                    existing_rating = db.session.query(ratings_table).filter_by(
                        user_id=user_map[user_id], movie_id=movie.id
                    ).first()
                    if not existing_rating:
                        db.session.execute(
                            ratings_table.insert().values(
                                user_id=user_map[user_id],
                                movie_id=movie.id,
                                rating=user_rating_value
                            )
                        )

            counter += 1
            if counter % batch_size == 0:
                if new_users:
                    db.session.commit()
                    for user in new_users:
                        user_map[user.email.split('@')[0][4:]] = user.id
                    new_users.clear()
                db.session.commit()
                print(f"Committed {counter} ratings...")
                if len(user_map) >= max_users:
                    break

        if new_users:
            db.session.commit()
            for user in new_users:
                user_map[user.email.split('@')[0][4:]] = user.id
        db.session.commit()

        total_ratings = db.session.query(ratings_table).count()
        print(f"Seeded {len(user_map)} users and {total_ratings} ratings successfully.")

if __name__ == "__main__":
    print("Starting User Seeding...")
    seed_user()
    print("User Seeding Complete.")