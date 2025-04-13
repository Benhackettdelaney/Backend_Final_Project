# seeders/seed_all.py
import sys
import os
from flask import Flask

# Add project root to sys.path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from extensions import db

print("Starting seed_all.py...")

try:
    from seeders.movie_seeder import seed_movies
    from seeders.user_seeder import seed_user
    from seeders.actor_seeder import seed_actors
    print("Imports successful.")
except ImportError as e:
    print(f"Import error: {e}")
    sys.exit(1)

def seed_all():
    print("Entering seed_all function...")
    # Create a Flask app for seeding
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databasemovie.db'  # Matches config.py
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize the database
    db.init_app(app)

    try:
        with app.app_context():
            print("Dropping all tables...")
            db.drop_all()
            print("All tables dropped.")
            
            print("Creating all tables...")
            db.create_all()
            print("Database tables created or verified.")
            
            print("Starting Seeding...")
            seed_actors()
            seed_movies()
            seed_user()
            print("Seeding completed successfully.")
    except Exception as e:
        print(f"Error during seeding: {e}")
        sys.exit(1)

if __name__ == "__main__":
    print("Executing seed_all...")
    seed_all()