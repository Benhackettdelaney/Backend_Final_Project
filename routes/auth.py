# routes/auth.py (unchanged)
from flask import Blueprint, request, jsonify
from extensions import db
from models.user import User
from flask_bcrypt import Bcrypt
from functools import wraps  
from flask_jwt_extended import create_access_token, set_access_cookies, unset_jwt_cookies, get_jwt_identity, jwt_required

auth_bp = Blueprint('auth', __name__)
bcrypt = Bcrypt()

def admin_required(f):
    @wraps(f)
    @jwt_required()
    def decorated_function(*args, **kwargs):
        user_id = get_jwt_identity()
        user = User.query.get(int(user_id))
        if not user or not user.is_admin():
            return jsonify({"error": "Admin access required"}), 403
        return f(*args, **kwargs)
    return decorated_function

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400

    required_fields = ["username", "email", "password", "user_gender", "user_occupation_label", "raw_user_age"]
    missing_fields = [field for field in required_fields if field not in data or data[field] is None]
    if missing_fields:
        return jsonify({"error": f"Missing required fields: {', '.join(missing_fields)}"}), 400

    username = data["username"]
    email = data["email"]
    password = data["password"]
    user_gender = data["user_gender"]
    user_occupation_label = data["user_occupation_label"]
    raw_user_age = data["raw_user_age"]

    if len(password) < 8:
        return jsonify({"error": "Password must be at least 8 characters"}), 400

    try:
        user_gender = int(user_gender)
        user_occupation_label = int(user_occupation_label)
        raw_user_age = int(raw_user_age)
    except ValueError:
        return jsonify({"error": "user_gender, user_occupation_label, and raw_user_age must be integers"}), 400

    if User.query.filter_by(email=email).first() or User.query.filter_by(username=username).first():
        return jsonify({"error": "Email or username already registered"}), 400

    hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
    new_user = User(
        username=username,
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
        access_token = create_access_token(identity=str(new_user.id))
        response = jsonify({
            "message": "Registration successful",
            "user_id": str(new_user.id),
            "access_token": access_token
        })
        set_access_cookies(response, access_token)
        return response, 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": f"Failed to register: {str(e)}"}), 500

@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Request body must be JSON"}), 400

    email = data.get("email")
    password = data.get("password")

    if not email or not password:
        return jsonify({"error": "Email and password are required"}), 400

    user = User.query.filter_by(email=email).first()
    if user and bcrypt.check_password_hash(user.password, password):
        access_token = create_access_token(identity=str(user.id))
        print(f"Generated token for user {user.id}: {access_token}")
        response = jsonify({
            "message": "Login successful",
            "user_id": str(user.id),
            "role": user.role,
            "access_token": access_token
        })
        set_access_cookies(response, access_token)
        return response, 200
    return jsonify({"error": "Invalid email or password"}), 401

@auth_bp.route("/logout", methods=["POST"])
def logout():
    response = jsonify({"message": "Successfully logged out"})
    unset_jwt_cookies(response)
    return response, 200

@auth_bp.route("/current-user", methods=["GET"])
@jwt_required()
def current_user():
    user_id = get_jwt_identity()
    user = User.query.get(int(user_id))
    if user:
        return jsonify({
            "user_id": user_id,
            "email": user.email,
            "username": user.username,
            "user_gender": user.user_gender,
            "raw_user_age": user.raw_user_age,
            "user_occupation_label": user.user_occupation_label,
            "user_rating": user.user_rating,
            "role": user.role,
            "created_at": user.created_at.isoformat() 
        }), 200
    return jsonify({"error": "User not found"}), 404