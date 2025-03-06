# models/watchlist.py
from extensions import db

class Watchlist(db.Model):
    __tablename__ = 'watchlist'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    movie_id = db.Column(db.String(10), db.ForeignKey('movie.id'), nullable=False)  # Changed to String
    title = db.Column(db.String(100), nullable=False)

    user = db.relationship('User', backref='watchlist_entries')
    movie = db.relationship('Movie', backref='watchlist_entries')

    def __repr__(self):
        return f"Watchlist(user_id={self.user_id}, movie_id='{self.movie_id}', title='{self.title}')"