import sys
import os
from flask import Flask

# This makes sure the parent dictory is in the import path, this was used because when trying to seed the files couldn't be found
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from extensions import db
from models.actor import Actor
from faker import Faker

# This creates fake data
fake = Faker()

def seed_actors():
    # This creates the Flask app and configures the database
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///databasemovie.db'  
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    with app.app_context():
        print("Seeding actors with fake data...")

        # This clear existing actors from the database
        try:
            db.session.query(Actor).delete()
            db.session.commit()
            print("Cleared existing actors.")
        except Exception as e:
            print(f"Error clearing actors: {e}")
            db.session.rollback()
            return

        num_actors = 30  # The amount of actors that are seeded to the database
        counter = 0
        batch_size = 100

        for _ in range(num_actors):
            
            # This generate fake data for each of the actors
            name = fake.name()
            description = fake.paragraph(nb_sentences=2)
            previous_work = ", ".join(fake.words(nb=3, ext_word_list=["Movie A", "Movie B", "Movie C", "Film X", "Show Y"]))
            birthday = fake.date_of_birth(minimum_age=18, maximum_age=80)
            nationality = fake.country()


            # This checks if the actors already exist to avoid dupication 
            existing_actor = Actor.query.filter_by(name=name).first()
            if not existing_actor:

                # This creates and add a new actor to the session 
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