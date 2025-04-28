from extensions import db

class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    movie_id = db.Column(db.String(10), db.ForeignKey('movie.id'), nullable=False)
    content = db.Column(db.String(500), nullable=False)  
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    user = db.relationship('User', backref='reviews')
    movie = db.relationship('Movie', backref='reviews')

    def __repr__(self):
        return f"Review(id={self.id}, user_id={self.user_id}, movie_id='{self.movie_id}', content='{self.content[:20]}...')"