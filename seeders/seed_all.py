from movie_seeder import seed_movie
from user_seeder import seed_user

def seed_all():
    print(f"Starting Seeding..")
    seed_movie() 
    seed_user()  
    print(f"Seeding Complete")

if __name__ == "__main__":
    seed_all()
