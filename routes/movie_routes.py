from flask import Blueprint, request, jsonify
from models.movie import Movie
from extensions import db

movie_bp = Blueprint('movie_bp', __name__)

@movie_bp.route('/create', methods=['POST'])  
def create_movie():
    data = request.json
    new_movie = Movie(movie_title=data['movie_title'], movie_ratings=data['movie_ratings'], movie_genres=data['movie_genres'])
    db.session.add(new_movie)
    db.session.commit()
    return jsonify({'message': 'Movie created successfully'}), 201

@movie_bp.route('', methods=['GET'])  
def get_movies():
    movies = Movie.query.all()
    return jsonify([{
        "id": movie.id,
        "movie_title": movie.movie_title,
        "movie_ratings": movie.movie_ratings,
        "movie_genres": movie.movie_genres
    } for movie in movies]), 200

@movie_bp.route('/<int:id>', methods=['GET'])  
def single_movie(id):
    movie = Movie.query.get_or_404(id)
    return jsonify({
        "id": movie.id,
        "movie_title": movie.movie_title,
        "movie_ratings": movie.movie_ratings,
        "movie_genres": movie.movie_genres
    }), 200

@movie_bp.route('/update/<int:id>', methods=['PUT'])
def update_movie(id):
    data = request.json
    movie = Movie.query.get_or_404(id)
    movie.movie_title = data['movie_title']
    movie.movie_ratings = data['movie_ratings']
    movie.movie_genres = data['movie_genres']
    db.session.commit()
    return jsonify({'message': 'Movie updated successfully'}), 200

@movie_bp.route('/delete/<int:id>', methods=['DELETE'])
def delete_movie(id):
    movie = Movie.query.get_or_404(id)
    db.session.delete(movie)
    db.session.commit()
    return jsonify({'message': 'Movie deleted successfully'}), 200
