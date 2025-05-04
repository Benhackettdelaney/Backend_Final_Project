from extensions import db

# Defining a many-to-many relationship between actors and movies
movie_actors = db.Table('movie_actors',
    db.Column('movie_id', db.String(10), db.ForeignKey('movie.id'), primary_key=True),
    db.Column('actor_id', db.Integer, db.ForeignKey('actor.id'), primary_key=True)
)