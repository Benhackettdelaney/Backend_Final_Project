# models/movie.py
from extensions import db, ratings_table, watchlist_table

class Movie(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    movie_title = db.Column(db.String(100), nullable=False)
    movie_genres = db.Column(db.String(100), nullable=False)

    # Many-to-many relationship with User for ratings
    ratings = db.relationship(
        'User',
        secondary=ratings_table,
        back_populates='ratings'  # Link to User's ratings
    )

    # Many-to-many relationship with User for watchlist
    watchlist = db.relationship(
        'User',
        secondary=watchlist_table,
        back_populates='watchlist',  # Link to User's watchlist
        cascade='all, delete'  # Delete watchlist entries when Movie is deleted
    )

    def __repr__(self):
        return f"Movie('{self.movie_title}', '{self.movie_genres}')"