# models/actors.py
from extensions import db
from models.actor_movie import movie_actors 

class Actor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    previous_work = db.Column(db.String(200), nullable=True)  
    birthday = db.Column(db.DateTime, nullable=True)  
    nationality = db.Column(db.String(100), nullable=True)  
    movies = db.relationship('Movie', secondary=movie_actors, back_populates='actors', lazy='dynamic')

    def __repr__(self):
        return f"Actor('{self.name}')"