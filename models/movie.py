from extensions import db
from models.actor import Actor
from models.actor_movie import movie_actors  

class Movie(db.Model):
    id = db.Column(db.String(10), primary_key=True)
    movie_title = db.Column(db.String(100), nullable=False)
    movie_genres = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
    actors = db.relationship('Actor', secondary=movie_actors, back_populates='movies', lazy='dynamic')

    def __repr__(self):
        return f"Movie(id='{self.id}', title='{self.movie_title}', genres='{self.movie_genres}')"