from faker import Faker
from extensions import db
from app import app
from models.user import User

fake = Faker()

def seed_user():
    with app.app_context():
        testUser1 = User(
            email="user1@user.com",
            password="password",
            user_gender=0,
            user_occupation_label=5,
            raw_user_age=25, 
        )

        testUser2 = User(
            email="user2@user.com",
            password="password",
            user_gender=1,
            user_occupation_label=10,  
            raw_user_age=30,  
        )

        db.session.add(testUser1)
        db.session.add(testUser2)

        db.session.commit()

        print(f"2 hardcoded users seeded successfully")

if __name__ == "__main__":
    print(f"Starting User Seeding..")
    seed_user()
    print(f"User Seeding Complete..")
