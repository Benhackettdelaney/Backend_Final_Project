from extensions import db

class Rating(db.Model):
    __tablename__ = 'ratings'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    movie_id = db.Column(db.String(10), db.ForeignKey('movie.id'), nullable=False) 
    rating = db.Column(db.Float, nullable=False)

    user = db.relationship('User', backref='rating_entries')
    movie = db.relationship('Movie', backref='rating_entries')

    def __repr__(self):
        return f"Rating(user_id={self.user_id}, movie_id='{self.movie_id}', rating={self.rating})"
