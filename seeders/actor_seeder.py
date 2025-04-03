# seeders/actor_seeder.py
import sys
import os
from extensions import db
from app import app
from models.actor import Actor
from faker import Faker

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

fake = Faker()

def seed_actors():
    with app.app_context():
        print("Seeding actors with fake data...")

        try:
            db.session.query(Actor).delete()
            db.session.commit()
            print("Cleared existing actors.")
        except Exception as e:
            print(f"Error clearing actors: {e}")
            db.session.rollback()
            return

        num_actors = 30  
        counter = 0
        batch_size = 100

        for _ in range(num_actors):
            name = fake.name()
            description = fake.paragraph(nb_sentences=2)
            previous_work = ", ".join(fake.words(nb=3, ext_word_list=["Movie A", "Movie B", "Movie C", "Film X", "Show Y"]))
            birthday = fake.date_of_birth(minimum_age=18, maximum_age=80)
            nationality = fake.country()

            existing_actor = Actor.query.filter_by(name=name).first()
            if not existing_actor:
                new_actor = Actor(
                    name=name,
                    description=description,
                    previous_work=previous_work,
                    birthday=birthday,
                    nationality=nationality
                )
                db.session.add(new_actor)
                counter += 1

            if counter % batch_size == 0:
                try:
                    db.session.commit()
                    print(f"Committed {counter} actors...")
                except Exception as e:
                    print(f"Error committing batch at {counter} actors: {e}")
                    db.session.rollback()
                    return

        try:
            db.session.commit()
            total_actors = Actor.query.count()
            print(f"Seeded {total_actors} actors successfully.")
            sample_actor = Actor.query.first()
            if sample_actor:
                print(f"Sample Actor: ID={sample_actor.id}, Name={sample_actor.name}, Description={sample_actor.description}, "
                      f"Previous Work={sample_actor.previous_work}, Birthday={sample_actor.birthday}, Nationality={sample_actor.nationality}")
        except Exception as e:
            print(f"Final actor commit failed: {e}")
            db.session.rollback()

if __name__ == "__main__":
    print("Starting Actor Seeding...")
    seed_actors()