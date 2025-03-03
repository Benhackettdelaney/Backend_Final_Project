from extensions import db

ratings_table = db.Table('ratings',
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True),
    db.Column('movie_id', db.Integer, db.ForeignKey('movie.id'), primary_key=True),
    db.Column('user_rating', db.Float, nullable=False),
)

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_title = db.Column(db.String(100), nullable=False)
    movie_genres = db.Column(db.String(100), nullable=False)
    
    ratings = db.relationship('User', secondary=ratings_table, backref='movies')

    def __repr__(self):
        return f"Movie('{self.movie_title}', '{self.movie_genres}')"


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    user_gender = db.Column(db.Integer, nullable=False)
    user_occupation_label = db.Column(db.Integer, nullable=False)
    raw_user_age = db.Column(db.Integer, nullable=False)

    ratings = db.relationship('Movie', secondary=ratings_table, backref='users')

    def __repr__(self):
        return f"User('{self.email}', '{self.password}')"
