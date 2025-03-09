from extensions import db

class Movie(db.Model):
    id = db.Column(db.String(10), primary_key=True) 
    movie_title = db.Column(db.String(100), nullable=False)
    movie_genres = db.Column(db.String(100), nullable=False)

  
    rated_by = db.relationship('User', secondary='ratings', back_populates='ratings')
    in_watchlists = db.relationship('User', secondary='watchlist', back_populates='watchlist')

    def __repr__(self):
        return f"Movie(id='{self.id}', title='{self.movie_title}', genres='{self.movie_genres}')"
