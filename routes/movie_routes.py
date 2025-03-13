# routes/movie.py
from flask import Blueprint, request, jsonify
from models.movie import Movie
from models.watchlist import Watchlist
from models.rating import Rating
from extensions import db
from flask_jwt_extended import jwt_required, get_jwt_identity
from routes.auth import admin_required  # Keep this, it’s already updated for JWT

movie_bp = Blueprint('movie_bp', __name__)

@movie_bp.route('/create', methods=['POST'])
@admin_required
def create_movie():
    print(f"Request headers: {request.headers}")
    print(f"Request data: {request.data}")
    if not request.is_json:
        return jsonify({'error': 'Content-Type must be application/json'}), 400
    
    data = request.json
    print(f"Parsed JSON: {data}")
    if not data or 'id' not in data or 'movie_title' not in data or 'movie_genres' not in data:
        return jsonify({'error': 'Missing id, movie_title, or movie_genres'}), 400
    
    if Movie.query.get(data['id']):
        return jsonify({'error': f"Movie with ID {data['id']} already exists"}), 409

    try:
        new_movie = Movie(
            id=data['id'],
            movie_title=data['movie_title'],
            movie_genres=data['movie_genres'],
            description=data.get('description')
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
        "movie_genres": movie.movie_genres,
        "description": movie.description,
        "created_at": movie.created_at.isoformat()
    } for movie in movies]), 200

@movie_bp.route('/<id>', methods=['GET'])
def single_movie(id):
    movie = Movie.query.get_or_404(id)
    return jsonify({
        "id": movie.id,
        "movie_title": movie.movie_title,
        "movie_genres": movie.movie_genres,
        "description": movie.description,
        "created_at": movie.created_at.isoformat()
    }), 200

@movie_bp.route('/update/<id>', methods=['PUT'])
@admin_required
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
        movie.description = data.get('description', movie.description)
        db.session.commit()
        return jsonify({'message': 'Movie updated successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Failed to update movie: {str(e)}'}), 500

@movie_bp.route('/delete/<id>', methods=['DELETE'])
@admin_required
def delete_movie(id):
    movie = Movie.query.get_or_404(id)
    try:
        Rating.query.filter_by(movie_id=id).delete()
        Watchlist.query.filter_by(movie_id=id).delete()
        db.session.delete(movie)
        db.session.commit()
        return jsonify({'message': 'Movie and its associated entries deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Failed to delete movie: {str(e)}'}), 500