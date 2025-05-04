from extensions import db
from models.actor_movie import movie_actors # Importing associated table

# Defining the actor class
class Actor(db.Model):
    id = db.Column(db.Integer, primary_key=True) #  Unique id for each actor
    name = db.Column(db.String(100), nullable=False) # Actor name
    description = db.Column(db.String(500), nullable=True) # Description
    previous_work = db.Column(db.String(200), nullable=True)  # Previous Work
    birthday = db.Column(db.DateTime, nullable=True)  # Birthday
    nationality = db.Column(db.String(100), nullable=True)  # Nationality

    # Defining a many-to-many relationship with movies 
    movies = db.relationship('Movie', secondary=movie_actors, back_populates='actors', lazy='dynamic')

    def __repr__(self):
        return f"Actor('{self.name}')"