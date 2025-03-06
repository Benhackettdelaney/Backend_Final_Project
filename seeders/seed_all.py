
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from movie_seeder import seed_movie
from user_seeder import seed_user

def seed_all():
    print("Starting Seeding..")
    seed_movie()
    seed_user()
    print("Seeding Complete")

if __name__ == "__main__":
    seed_all()