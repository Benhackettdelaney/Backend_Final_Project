# routes/rating.py
from flask import Blueprint, request, jsonify
from models.rating import Rating
from models.movie import Movie
from models.user import User
from extensions import db
from flask_jwt_extended import jwt_required, get_jwt_identity

rating_bp = Blueprint('rating_bp', __name__)

@rating_bp.route('', methods=['POST'])
@jwt_required()
def add_rating():
    user_id = get_jwt_identity()
    json_data = request.get_json()
    if json_data is None or 'movie_id' not in json_data or 'rating' not in json_data:
        return jsonify({'error': 'movie_id and rating are required'}), 400

    movie_id = json_data['movie_id']
    rating = json_data['rating']

    try:
        rating = float(rating)
        if not (1.0 <= rating <= 5.0):
            return jsonify({'error': 'Rating must be between 1.0 and 5.0'}), 400
    except ValueError:
        return jsonify({'error': 'rating must be a number'}), 400

    user = User.query.get(int(user_id))
    movie = Movie.query.get(movie_id)
    if not user:
        return jsonify({'error': f'User with ID {user_id} not found'}), 404
    if not movie:
        return jsonify({'error': f'Movie with ID {movie_id} not found'}), 404

    try:
        existing_rating = Rating.query.filter_by(user_id=user_id, movie_id=movie_id).first()
        if existing_rating:
            existing_rating.rating = rating
            action = "updated"
        else:
            new_rating = Rating(user_id=user_id, movie_id=movie_id, rating=rating)
            db.session.add(new_rating)
            action = "added"

        db.session.commit()
        return jsonify({
            'message': f'Successfully {action} rating for {movie.movie_title} with {rating}',
            'id': existing_rating.id if existing_rating else new_rating.id
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Failed to add rating: {str(e)}'}), 500

@rating_bp.route('', methods=['GET'])
@jwt_required()
def get_user_ratings():
    user_id = get_jwt_identity()
    user = User.query.get(int(user_id))
    if not user:
        return jsonify({'error': f'User with ID {user_id} not found'}), 404

    try:
        ratings = Rating.query.filter_by(user_id=user_id).all()
        rated_movies_list = [
            {
                "id": rating.id,
                "title": rating_movie.movie_title,
                "rating": float(rating.rating),
                "genres": rating_movie.movie_genres,
                "movie_id": rating.movie_id,
                'created_at': rating.created_at.isoformat()
            }
            for rating in ratings
            if (rating_movie := Movie.query.get(rating.movie_id)) 
        ]
        return jsonify({'rated_movies': rated_movies_list}), 200
    except Exception as e:
        return jsonify({'error': f'Failed to fetch ratings: {str(e)}'}), 500