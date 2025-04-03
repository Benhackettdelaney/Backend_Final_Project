# seeders/seed_all.py
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

print("Starting seed_all.py...")  

try:
    from movie_seeder import seed_movies
    from user_seeder import seed_user
    from actor_seeder import seed_actors  
    from app import app
    from extensions import db
    print("Imports successful.")  
except ImportError as e:
    print(f"Import error: {e}")
    sys.exit(1)

def seed_all():
    print("Entering seed_all function...") 
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