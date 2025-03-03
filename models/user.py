from extensions import db
import movie_user 

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    user_gender = db.Column(db.Integer, nullable=False)
    user_occupation_label = db.Column(db.Integer, nullable=False)
    raw_user_age = db.Column(db.Integer, nullable=False)
    user_rating = db.Column(db.Float, nullable=False)

 
    ratings = db.relationship('Movie', secondary=movie_user, backref='users')

    def __repr__(self):
        return f"User('{self.email}', '{self.password}')"
