from flask import Blueprint, request, redirect, url_for, flash, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from werkzeug.security import check_password_hash
from models import db, User
from flask_bcrypt import Bcrypt
from models.user import User 
from models.movie_user import ratings_table

bcrypt = Bcrypt()

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        password = request.form["password"]
        user_gender = request.form["gender"]  
        user_occupation_label = request.form["occupation_label"] 
        raw_user_age = request.form["age"]  
        user_rating = 0.0  

        if User.query.filter_by(username=username).first():
            flash("Username already exists", "danger")
            return redirect(url_for("auth.register"))

        if len(password) < 8:
            flash("Password must be at least 8 characters", "danger")
            return redirect(url_for("auth.register"))

        hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
        new_user = User(username=username, email=email, password=hashed_password)

        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful!", "success")
        return redirect(url_for("auth.login"))

    return redirect(url_for("auth.register"))

@auth_bp.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username).first()

        if user and bcrypt.check_password_hash(user.password, password):
            access_token = create_access_token(identity=user.id, fresh=True)
            flash("Login successful!", "success")
            return redirect(url_for("movies.index"))

        flash("Invalid credentials. Please try again.", "danger")
        return redirect(url_for("auth.login"))

    return redirect(url_for("auth.login"))

@auth_bp.route("/logout", methods=["POST"])
@jwt_required()
def logout():
    return jsonify({"message": "Successfully logged out"}), 200
