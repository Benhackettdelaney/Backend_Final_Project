from flask import Blueprint, request, jsonify
from models.rating import Rating
from models.movie import Movie
from models.user import User
from extensions import db

rating_bp = Blueprint('rating_bp', __name__)

@rating_bp.route('', methods=['POST'])
def add_rating():
    """Allow a user to rate a movie, storing the rating with a unique ID."""
    print(f"Request method: {request.method}")
    print(f"Request headers: {request.headers}")
    print(f"Request body: {request.get_data(as_text=True)}")

    json_data = request.get_json()
    if json_data is None or 'user_id' not in json_data or 'movie_id' not in json_data or 'rating' not in json_data:
        return jsonify({'error': 'user_id, movie_id, and rating are required'}), 400

    user_id = json_data['user_id']
    movie_id = json_data['movie_id']
    rating = json_data['rating']

    try:
        user_id = int(user_id)
        rating = float(rating)
        if not (1.0 <= rating <= 5.0):
            return jsonify({'error': 'Rating must be between 1.0 and 5.0'}), 400
    except ValueError:
        return jsonify({'error': 'user_id must be an integer, rating must be a number'}), 400

    user = User.query.get(user_id)
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
        print(f"Rating {action}: User {user_id}, Movie {movie_id}, Rating {rating}")
        return jsonify({
            'message': f'Successfully {action} rating for {movie.movie_title} with {rating}',
            'id': existing_rating.id if existing_rating else new_rating.id
        }), 200
    except Exception as e:
        db.session.rollback()
        print(f"Error adding rating: {str(e)}")
        return jsonify({'error': f'Failed to add rating: {str(e)}'}), 500

@rating_bp.route('', methods=['GET'])
def get_user_ratings():
    print(f"Request method: {request.method}")
    print(f"Request headers: {request.headers}")
    print(f"Request body: {request.get_data(as_text=True)}")

    json_data = request.get_json(silent=True)
    if json_data and 'user_id' in json_data:
        user_id = json_data['user_id']
    else:
        return jsonify({'error': 'user_id is required in the request body'}), 400

    try:
        user_id = int(user_id)
    except ValueError:
        return jsonify({'error': 'user_id must be an integer'}), 400

    user = User.query.get(user_id)
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
                "movie_id": rating.movie_id
            }
            for rating in ratings
            if (rating_movie := Movie.query.get(rating.movie_id))  # Fetch movie details
        ]

        print(f"User {user_id} rated movies: {rated_movies_list}")
        return jsonify({
            'rated_movies': rated_movies_list
        }), 200
    except Exception as e:
        print(f"Error fetching ratings: {str(e)}")
        return jsonify({'error': f'Failed to fetch ratings: {str(e)}'}), 500