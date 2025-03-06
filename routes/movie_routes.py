# routes/movie_routes.py
from flask import Blueprint, request, jsonify
from models.movie import Movie
from extensions import db

movie_bp = Blueprint('movie_bp', __name__)

@movie_bp.route('/create', methods=['POST'])
def create_movie():
    print(f"Request headers: {request.headers}")
    print(f"Request data: {request.data}")
    if not request.is_json:
        return jsonify({'error': 'Content-Type must be application/json'}), 400
    
    data = request.json
    print(f"Parsed JSON: {data}")
    if not data or 'movie_title' not in data or 'movie_genres' not in data:
        return jsonify({'error': 'Missing movie_title or movie_genres'}), 400
    
    try:
        new_movie = Movie(
            movie_title=data['movie_title'],
            movie_genres=data['movie_genres']
        )
        db.session.add(new_movie)
        db.session.commit()
        return jsonify({'message': 'Movie created successfully', 'id': new_movie.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Failed to create movie: {str(e)}'}), 500
    
@movie_bp.route('', methods=['GET'])
def get_movies():
    movies = Movie.query.all()
    return jsonify([{
        "id": movie.id,
        "movie_title": movie.movie_title,
        "movie_genres": movie.movie_genres
    } for movie in movies]), 200

@movie_bp.route('/<int:id>', methods=['GET'])
def single_movie(id):
    movie = Movie.query.get_or_404(id)
    return jsonify({
        "id": movie.id,
        "movie_title": movie.movie_title,
        "movie_genres": movie.movie_genres
    }), 200

@movie_bp.route('/update/<int:id>', methods=['PUT'])
def update_movie(id):
    if not request.is_json:
        return jsonify({'error': 'Content-Type must be application/json'}), 400
    
    data = request.json
    if not data or 'movie_title' not in data or 'movie_genres' not in data:
        return jsonify({'error': 'Missing movie_title or movie_genres'}), 400
    
    movie = Movie.query.get_or_404(id)
    try:
        movie.movie_title = data['movie_title']
        movie.movie_genres = data['movie_genres']
        db.session.commit()
        return jsonify({'message': 'Movie updated successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Failed to update movie: {str(e)}'}), 500

@movie_bp.route('/delete/<int:id>', methods=['DELETE'])
def delete_movie(id):
    movie = Movie.query.get_or_404(id)
    try:
        db.session.delete(movie)
        db.session.commit()
        return jsonify({'message': 'Movie and its associated watchlist entries deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Failed to delete movie: {str(e)}'}), 500