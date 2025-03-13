from extensions import db

class Watchlist(db.Model):
    __tablename__ = 'watchlist'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    movie_ids = db.Column(db.JSON, nullable=False, default=lambda: [])
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    user = db.relationship('User', back_populates='watchlists')  # Updated, removed duplicate backref

    def __repr__(self):
        return f"Watchlist(user_id={self.user_id}, title='{self.title}', movie_ids={self.movie_ids})"