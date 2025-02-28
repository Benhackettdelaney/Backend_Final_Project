from flask import Blueprint, request, jsonify
from models.movie import Movie
from extensions import db

movie_bp = Blueprint('movie_bp', __name__)

@movie_bp.route('/movies', methods=['POST']) 
def create_movie():
    data = request.json
    new_movie = Movie(movie_title=data['movie_title'], movie_ratings=data['movie_ratings'], movie_genres=data['movie_genres'])
    db.session.add(new_movie)
    db.session.commit()
    return jsonify({'message': 'Movie created successfully'}), 201

@movie_bp.route('/movies', methods=['GET'])
def get_movies():
    movies = Movie.query.all()
    return jsonify([{"id": movies.id, "movie_title": movies.title, "movie_ratings": movies.ratings, "movie_genres": movies.genres} for movies in movies]), 200

@movie_bp.route('/movies/<int:id>', methods=['PUT'])
def update_movie(id):
    data = request.json
    movie = Movie.query.get_or_404(id)
    movie.movie_title = data['movie_title']
    movie.movie_ratings = data['movie_ratings']
    movie.movie_genres = data['movie_genres']
    db.session.commit()
    return jsonify({'message': 'Movie updated successfully'}), 200

@movie_bp.route('/movies/<int:id>', methods=['DELETE'])
def delete_movie(id):
    movie = Movie.query.get_or_404(id)  
    db.session.delete(movie)
    db.session.commit()
    return jsonify({'message': 'Movie deleted successfully'}), 200