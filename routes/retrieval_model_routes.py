from flask import Blueprint, jsonify, request
from models.movie import Movie  
from models.user import User
from extensions import db
import numpy as np
from utils import movie_to_features  
from models.movie_user import ratings_table
import tensorflow as tf


retrieval_bp = Blueprint('retrieval_bp', __name__)

# Load your retrieval model
basic_retrieval_model = tf.saved_model.load('retrieval_model')
 
@retrieval_bp.route('/recommendations', methods=['GET'])
def get_recommendations():
    genre = request.args.get('genre')
    user_id = request.args.get('user_id')

    # Get all the movies rated by the user by joining the ratings_table
    user_rated_movies = db.session.query(Movie, ratings_table.c.rating).join(
        ratings_table, ratings_table.c.movie_id == Movie.id
    ).filter(ratings_table.c.user_id == user_id).all()

    # If the user hasn't rated any movies, return an error message
    if not user_rated_movies:
        return jsonify({'message': 'No movies found for the specified user'}), 404

    # Filter the movies by genre
    genre_filtered_movies = [movie for movie, rating in user_rated_movies if genre in movie.movie_genres.split(',')]

    # If no movies match the genre, return an error message
    if not genre_filtered_movies:
        return jsonify({'message': 'No movies found for the specified genre'}), 404

    # Get movie titles for retrieval
    movie_titles = [movie.movie_title for movie in genre_filtered_movies]

    # Get recommendations from the retrieval model
    _, titles = basic_retrieval_model(movie_titles)

    # Prepare the recommended movie list
    recommended_movies = [{"movie_title": title} for title in titles[0][:3]]

    return jsonify(recommended_movies)
