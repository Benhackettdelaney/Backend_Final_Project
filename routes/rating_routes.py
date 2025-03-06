# routes/rating_routes.py
from flask import Blueprint, request, jsonify
from extensions import db, ratings_table
from models.movie import Movie
from models.user import User

rating_bp = Blueprint('rating_bp', __name__)

@rating_bp.route('', methods=['POST'])
def add_rating():
    """Allow a user to rate a movie, storing the rating in ratings_table."""
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
        existing_rating = db.session.query(ratings_table).filter_by(user_id=user_id, movie_id=movie_id).first()
        if existing_rating:
            stmt = db.update(ratings_table).where(
                (ratings_table.c.user_id == user_id) &
                (ratings_table.c.movie_id == movie_id)
            ).values(rating=rating)
            db.session.execute(stmt)
            action = "updated"
        else:
            stmt = db.insert(ratings_table).values(user_id=user_id, movie_id=movie_id, rating=rating)
            db.session.execute(stmt)
            action = "added"

        db.session.commit()
        print(f"Rating {action}: User {user_id}, Movie {movie_id}, Rating {rating}")
        return jsonify({
            'message': f'Successfully {action} rating for {movie.movie_title} with {rating}'
        }), 200
    except Exception as e:
        db.session.rollback()
        print(f"Error adding rating: {str(e)}")
        return jsonify({'error': f'Failed to add rating: {str(e)}'}), 500

@rating_bp.route('', methods=['GET'])
def get_user_ratings():
    """Return all movies rated by a user for display in the front-end."""
    print(f"Request method: {request.method}")
    print(f"Request headers: {request.headers}")
    print(f"Request body: {request.get_data(as_text=True)}")

    # Get user_id from JSON body instead of query parameters
    json_data = request.get_json(silent=True)  # silent=True to avoid 400 if no body
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
        rated_movies = (
            db.session.query(Movie, ratings_table.c.rating)
            .join(ratings_table, Movie.id == ratings_table.c.movie_id)
            .filter(ratings_table.c.user_id == user_id)
            .all()
        )

        rated_movies_list = [
            {
                "title": movie.movie_title,
                "rating": float(rating),
                "genres": movie.movie_genres,
                "movie_id": movie.id
            }
            for movie, rating in rated_movies
        ]

        print(f"User {user_id} rated movies: {rated_movies_list}")
        return jsonify({
            'rated_movies': rated_movies_list
        }), 200
    except Exception as e:
        print(f"Error fetching ratings: {str(e)}")
        return jsonify({'error': f'Failed to fetch ratings: {str(e)}'}), 500