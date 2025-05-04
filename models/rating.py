from extensions import db

# Defining rating class
class Rating(db.Model):
    __tablename__ = 'ratings'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True) # Primary key that autoincrements for ratings
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False) # Foreign key linking to the user model
    movie_id = db.Column(db.String(10), db.ForeignKey('movie.id'), nullable=False) # Foreign key linking to the movie model
    rating = db.Column(db.Float, nullable=False) # The rating value
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    # Sets up the relationships with the User and Movie models
    user = db.relationship('User', backref='rating_entries')
    movie = db.relationship('Movie', backref='rating_entries')

    def __repr__(self):
        return f"Rating(user_id={self.user_id}, movie_id='{self.movie_id}', rating={self.rating})"