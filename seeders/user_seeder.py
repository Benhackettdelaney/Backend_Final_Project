import sys
import os
import tensorflow_datasets as tfds
from extensions import db
from app import app
from models.user import User
from models.movie import Movie
from models.movie_user import ratings_table  

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

def seed_user():
    with app.app_context():
        ratings_dataset = tfds.load("movielens/100k-ratings", split="train")
    
        for rating in ratings_dataset.take(2): 
            user_id = rating["user_id"].numpy().decode('utf-8')
            user_gender = rating["user_gender"].numpy()
            user_age = rating["raw_user_age"].numpy()
            user_occupation_label = rating["user_occupation_label"].numpy()
            movie_id = rating["movie_id"].numpy().decode('utf-8')  
            user_rating = rating["rating"].numpy()

            
            movie = Movie.query.filter_by(id=movie_id).first()

            if movie:  
                new_user = User(
                    email=f"user@user.com",  
                    password="password", 
                    user_gender=user_gender,
                    user_occupation_label=user_occupation_label,
                    raw_user_age=user_age
                )

                db.session.add(new_user)
                db.session.commit()  

           
                db.session.execute(
                    ratings_table.insert().values(
                        user_id=new_user.id,
                        movie_id=movie.id, 
                        user_rating=user_rating
                    )
                )
                db.session.commit()

        print(f"Users seeded successfully with ratings.")

if __name__ == "__main__":
    print("Starting User Seeding...")
    seed_user()
    print("User Seeding Complete.")
