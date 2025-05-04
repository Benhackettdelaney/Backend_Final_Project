from extensions import db

# Defining user class
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True) # Primary key for the user
    username = db.Column(db.String(80), nullable=False)  # Username
    email = db.Column(db.String, unique=True, nullable=False) # Email for the user
    password = db.Column(db.String, nullable=False) # Password for the user
    user_gender = db.Column(db.Integer, nullable=False) # Gender
    user_occupation_label = db.Column(db.Integer, nullable=False) # Occupation
    raw_user_age = db.Column(db.Integer, nullable=False) # Age
    user_rating = db.Column(db.Float, nullable=False) # User rating
    role = db.Column(db.String, nullable=False, default="user") # Role defining the user as an admin or user
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    # Defining the relationship with the Watchlist model
    watchlists = db.relationship('Watchlist', back_populates='user', lazy='dynamic') 

    def is_admin(self):
        return self.role == "admin"

    def is_user(self):
        return self.role == "user"

    def __repr__(self):
        return f"User('{self.email}', '{self.password}')"