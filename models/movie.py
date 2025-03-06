# models/movie.py
from extensions import db, ratings_table, watchlist_table

class Movie(db.Model):
    id = db.Column(db.String(10), primary_key=True)  
    movie_title = db.Column(db.String(100), nullable=False)
    movie_genres = db.Column(db.String(100), nullable=False)

    ratings = db.relationship(
        'User',
        secondary=ratings_table,
        back_populates='ratings'  
    )

    watchlist = db.relationship(
        'User',
        secondary=watchlist_table,
        back_populates='watchlist', 
        cascade='all, delete'  
    )

    def __repr__(self):
        return f"Movie('{self.movie_title}', '{self.movie_genres}')"