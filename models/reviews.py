from extensions import db

# Defining review class
class Review(db.Model):
    __tablename__ = 'reviews'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) # Primary key and autoincrements for the reviews
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) # Foreign Key relating to the user model
    movie_id = db.Column(db.String(10), db.ForeignKey('movie.id'), nullable=False) # Foreign Key relating to the movies model
    content = db.Column(db.String(500), nullable=False)  # Content of the reviews
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    # Defining the relationship with the User and Movie models
    user = db.relationship('User', backref='reviews')
    movie = db.relationship('Movie', backref='reviews')

    def __repr__(self):
        return f"Review(id={self.id}, user_id={self.user_id}, movie_id='{self.movie_id}', content='{self.content[:20]}...')"