# routes/ranking_routes.py
from flask import Blueprint, request, jsonify
import tensorflow as tf
import numpy as np
from extensions import db
from models.movie import Movie

ranking_bp = Blueprint('ranking_bp', __name__)

# Load the ranking model 
try:
    ranking_model = tf.saved_model.load("ml_models/ranking_model")
    print("Ranking model loaded successfully")
    if hasattr(ranking_model, 'signatures'):
        print("Model signatures:", ranking_model.signatures)
except Exception as e:
    print(f"Error loading ranking model: {e}")
    ranking_model = None

# Initialize movie_titles and num_movies as globals, to be loaded later
movie_titles = []
num_movies = 0

def load_movie_titles():
    """Load movie titles from the database within an app context."""
    global movie_titles, num_movies
    if not movie_titles:  # Only load if not already populated
        try:
            movie_titles = [movie.movie_title for movie in Movie.query.all()]
            num_movies = len(movie_titles)
            print(f"Loaded {num_movies} movie titles from database")
            print(f"First few titles: {movie_titles[:5]}")
        except Exception as e:
            print(f"Error loading movies from database: {e}")
            movie_titles = []
            num_movies = 0

@ranking_bp.route('', methods=['POST'])
def rank_movies():
    """Get the top 5 highest-rated movie titles with genres for a given user_id."""
    load_movie_titles()

    print(f"Request method: {request.method}")
    print(f"Request headers: {request.headers}")
    print(f"Request body: {request.get_data(as_text=True)}")

    json_data = request.get_json()
    if json_data is None or 'user_id' not in json_data:
        return jsonify({'error': 'user_id is required'}), 400
    
    user_id = json_data['user_id']
    try:
        user_id = str(int(user_id))  # Convert to string (e.g., "42")
    except ValueError:
        return jsonify({'error': 'user_id must be an integer'}), 400

    if ranking_model is None:
        return jsonify({'error': 'Ranking model not available'}), 500
    if not movie_titles:
        return jsonify({'error': 'Movie titles not available'}), 500

    user_ids = tf.constant([user_id] * num_movies, dtype=tf.string)
    movie_titles_tensor = tf.constant(movie_titles, dtype=tf.string)
    input_data = {
        "user_id": user_ids,
        "movie_title": movie_titles_tensor
    }
    print(f"Input user_ids shape: {user_ids.shape}")
    print(f"Input movie_titles shape: {movie_titles_tensor.shape}")
    print(f"Input data sample: user_id={user_ids[0].numpy().decode('utf-8')}, movie_title={movie_titles_tensor[0].numpy().decode('utf-8')}")

    try:
        predictions = ranking_model(input_data)
        ratings = predictions.numpy().flatten()
        print(f"Predictions shape: {predictions.shape}")
        print(f"First few ratings: {ratings[:5].tolist()}")

        movies = Movie.query.all()
        movie_ratings = [(movie, rating) for movie, rating in zip(movies, ratings)]
        sorted_movie_ratings = sorted(movie_ratings, key=lambda x: x[1], reverse=True)
        top_5 = sorted_movie_ratings[:5]

        result = [
            {
                "title": movie.movie_title,
                "rating": float(rating),
                "genres": movie.movie_genres
            }
            for movie, rating in top_5
        ]
        print(f"Top 5 movies: {result}")
        return jsonify(result), 200
    except Exception as e:
        print(f"Prediction error: {str(e)}")
        return jsonify({'error': f'Ranking model error: {str(e)}'}), 500

@ranking_bp.route('', methods=['GET'])
def get_top_ranked_movies():
    """Return the top 5 highest-rated movie titles with genres for a given user_id (GET)."""
    load_movie_titles()

    print(f"Request method: {request.method}")
    print(f"Request headers: {request.headers}")
    print(f"Request body: {request.get_data(as_text=True)}")

    json_data = request.get_json(silent=True)  # Look for user_id in body
    if json_data and 'user_id' in json_data:
        user_id = json_data['user_id']
    else:
        user_id = request.args.get('user_id')  # Fallback to query parameter
        if not user_id:
            return jsonify({'error': 'user_id is required in body or query'}), 400

    try:
        user_id = str(int(user_id))  # Convert to string for model
    except ValueError:
        return jsonify({'error': 'user_id must be an integer'}), 400

    if ranking_model is None:
        return jsonify({'error': 'Ranking model not available'}), 500
    if not movie_titles:
        return jsonify({'error': 'Movie titles not available'}), 500

    user_ids = tf.constant([user_id] * num_movies, dtype=tf.string)
    movie_titles_tensor = tf.constant(movie_titles, dtype=tf.string)
    input_data = {
        "user_id": user_ids,
        "movie_title": movie_titles_tensor
    }
    print(f"Input user_ids shape: {user_ids.shape}")
    print(f"Input movie_titles shape: {movie_titles_tensor.shape}")
    print(f"Input data sample: user_id={user_ids[0].numpy().decode('utf-8')}, movie_title={movie_titles_tensor[0].numpy().decode('utf-8')}")

    try:
        predictions = ranking_model(input_data)
        ratings = predictions.numpy().flatten()
        print(f"Predictions shape: {predictions.shape}")
        print(f"First few ratings: {ratings[:5].tolist()}")

        movies = Movie.query.all()
        movie_ratings = [(movie, rating) for movie, rating in zip(movies, ratings)]
        sorted_movie_ratings = sorted(movie_ratings, key=lambda x: x[1], reverse=True)
        top_5 = sorted_movie_ratings[:5]

        result = [
            {
                "title": movie.movie_title,
                "rating": float(rating),
                "genres": movie.movie_genres
            }
            for movie, rating in top_5
        ]
        print(f"Top 5 movies for user {user_id}: {result}")
        return jsonify({
            'top_ranked_movies': result
        }), 200
    except Exception as e:
        print(f"Prediction error: {str(e)}")
        return jsonify({'error': f'Ranking model error: {str(e)}'}), 500