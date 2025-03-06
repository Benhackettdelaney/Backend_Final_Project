from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required
from werkzeug.security import check_password_hash
from extensions import db
from models.user import User
from flask_bcrypt import Bcrypt

auth_bp = Blueprint('auth', __name__)
bcrypt = Bcrypt()

@auth_bp.route("/register", methods=["POST"])
def register():
    """Register a new user."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400

    email = data.get("email")
    password = data.get("password")
    user_gender = data.get("user_gender")
    user_occupation_label = data.get("user_occupation_label")
    raw_user_age = data.get("raw_user_age")

    if not all([email, password, user_gender, user_occupation_label, raw_user_age]):
        return jsonify({"error": "All fields (email, password, user_gender, user_occupation_label, raw_user_age) are required"}), 400

    if len(password) < 8:
        return jsonify({"error": "Password must be at least 8 characters"}), 400

    try:
        user_gender = int(user_gender)
        user_occupation_label = int(user_occupation_label)
        raw_user_age = int(raw_user_age)
    except ValueError:
        return jsonify({"error": "user_gender, user_occupation_label, and raw_user_age must be integers"}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({"error": "Email already registered"}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")

    new_user = User(
        email=email,
        password=hashed_password,
        user_gender=user_gender,
        user_occupation_label=user_occupation_label,
        raw_user_age=raw_user_age,
        user_rating=0.0,  
        role="user"  
    )

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "Registration successful", "user_id": new_user.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Failed to register: {str(e)}"}), 500

@auth_bp.route("/login", methods=["POST"])
def login():
    """Log in a user and return a JWT token."""
    data = request.get_json()
    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    user = User.query.filter_by(email=email).first()
    if user and bcrypt.check_password_hash(user.password, password):
        access_token = create_access_token(identity=user.id, fresh=True)
        return jsonify({
            "message": "Login successful",
            "access_token": access_token,
            "user_id": user.id
        }), 200

    return jsonify({"error": "Invalid email or password"}), 401

@auth_bp.route("/logout", methods=["POST"])
@jwt_required()
def logout():
    """Log out a user (client-side token invalidation)."""
    return jsonify({"message": "Successfully logged out"}), 200