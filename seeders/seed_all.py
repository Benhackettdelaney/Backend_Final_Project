
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from movie_seeder import seed_movie
from user_seeder import seed_user
from app import app
from extensions import db

def seed_all():
    with app.app_context():
        db.drop_all()  # Drop existing tables
        print("All tables dropped.")
        db.create_all()  # Create new tables
        print("Database tables created or verified.")
        
        print("Starting Seeding...")
        seed_movie()  # Seed movies first
        seed_user()   # Seed users and ratings after movies

if __name__ == "__main__":
    seed_all()