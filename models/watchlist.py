from extensions import db

class Watchlist(db.Model):
    __tablename__ = 'watchlist'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    movie_ids = db.Column(db.JSON, nullable=False, default=lambda: [])  

    user = db.relationship('User', backref='watchlist_entries')

    def __repr__(self):
        return f"Watchlist(user_id={self.user_id}, title='{self.title}', movie_ids={self.movie_ids})"