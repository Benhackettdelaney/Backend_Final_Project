from extensions import db
from models.actor import Actor
from models.actor_movie import movie_actors  # Importing the associated table

# Defining movie class 
class Movie(db.Model):
    id = db.Column(db.String(10), primary_key=True) # Unique id for the movie
    movie_title = db.Column(db.String(100), nullable=False) # Movie title
    movie_genres = db.Column(db.String(100), nullable=False) # Movie genres
    description = db.Column(db.String(500), nullable=True) # Movie description
    image_url = db.Column(db.String(200), nullable=True)  # image for the movie
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    # Defining many-to-many relationship with actors
    actors = db.relationship('Actor', secondary=movie_actors, back_populates='movies', lazy='dynamic')

    def __repr__(self):
        return f"Movie(id='{self.id}', title='{self.movie_title}', genres='{self.movie_genres}')"