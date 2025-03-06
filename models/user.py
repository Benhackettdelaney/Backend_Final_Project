from extensions import db, ratings_table, watchlist_table

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    user_gender = db.Column(db.Integer, nullable=False)
    user_occupation_label = db.Column(db.Integer, nullable=False)
    raw_user_age = db.Column(db.Integer, nullable=False)
    user_rating = db.Column(db.Float, nullable=False)
    role = db.Column(db.String, nullable=False, default="user")

    ratings = db.relationship(
        'Movie',
        secondary=ratings_table,
        back_populates='ratings'
    )

    watchlist = db.relationship(
        'Movie',
        secondary=watchlist_table,
        back_populates='watchlist'
    )

    def is_admin(self):
        return self.role == "admin"

    def is_user(self):
        return self.role == "user"

    def __repr__(self):
        return f"User('{self.email}', '{self.password}')"

