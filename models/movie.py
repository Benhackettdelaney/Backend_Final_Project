from extensions import db

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_title = db.Column(db.String(100), nullable=False)
    movie_genres = db.Column(db.String(100), nullable=False)
    movie_ratings = db.Column(db.Float(), nullable=False)

    def __repr__(self):
        return f"Movie('{self.movie_title}', '{self.movie_genres}', '{self.movie_ratings}')"