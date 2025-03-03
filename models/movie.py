from extensions import db
import movie_user

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_title = db.Column(db.String(100), nullable=False)
    movie_genres = db.Column(db.String(100), nullable=False)

  
    ratings = db.relationship('User', secondary=movie_user, backref='movies')

    def __repr__(self):
        return f"Movie('{self.movie_title}', '{self.movie_genres}')"
