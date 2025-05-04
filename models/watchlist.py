from extensions import db

# Defining watchlist class
class Watchlist(db.Model):
    __tablename__ = 'watchlist'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) # Primary key that autoincrements for the waychlists
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) # Foreign key for the user model
    title = db.Column(db.String(100), nullable=False) # Title of the watchlists
    movie_ids = db.Column(db.JSON, nullable=False, default=lambda: []) # Foreign key for the movie model
    is_public = db.Column(db.Boolean, nullable=False, default=False)  # Users can set their watchlist to public or private
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp()) 

    # Defining relationship with User model
    user = db.relationship('User', back_populates='watchlists')

    def __repr__(self):
        return f"Watchlist(user_id={self.user_id}, title='{self.title}', movie_ids={self.movie_ids}, is_public={self.is_public})"