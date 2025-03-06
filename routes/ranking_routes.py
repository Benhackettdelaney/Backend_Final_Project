# routes/ranking_routes.py
from flask import Blueprint, request, jsonify
import tensorflow as tf
import tensorflow_datasets as tfds
import numpy as np

ranking_bp = Blueprint('ranking_bp', __name__)

# Load the ranking model (do this once at startup)
try:
    ranking_model = tf.saved_model.load("ml_models/ranking_model")
    print("Ranking model loaded successfully")
    if hasattr(ranking_model, 'signatures'):
        print("Model signatures:", ranking_model.signatures)
except Exception as e:
    print(f"Error loading ranking model: {e}")
    ranking_model = None

# Load MovieLens 100k movie titles (do this once at startup)
try:
    movie_dataset = tfds.load("movielens/100k-movies", split="train")
    movie_titles = [movie["movie_title"].numpy().decode('utf-8') for movie in movie_dataset]
    num_movie_titles = len(movie_titles)
    print(f"Loaded {num_movie_titles} movie titles from MovieLens 100k")
    print(f"First few titles: {movie_titles[:5]}")
except Exception as e:
    print(f"Error loading MovieLens dataset: {e}")
    movie_titles = []
    num_movie_titles = 0

@ranking_bp.route('', methods=['POST'])
def rank_movies():
    """Get the top 5 highest-rated movie titles with their ratings for a given user_id."""
    # Debug: Log request details
    print(f"Request method: {request.method}")
    print(f"Request headers: {request.headers}")
    print(f"Request body: {request.get_data(as_text=True)}")

    # Get JSON data from request body
    json_data = request.get_json()
    if json_data is None or 'user_id' not in json_data:
        return jsonify({'error': 'user_id is required'}), 400
    
    user_id = json_data['user_id']
    try:
        user_id = str(int(user_id))  # Convert to int then back to string (e.g., "42")
    except ValueError:
        return jsonify({'error': 'user_id must be an integer'}), 400

    # Check if model and movie titles are loaded
    if ranking_model is None:
        return jsonify({'error': 'Ranking model not available'}), 500
    if not movie_titles:
        return jsonify({'error': 'Movie titles not available'}), 500

    # Prepare input for the model
    user_ids = tf.constant([user_id] * num_movie_titles, dtype=tf.string)  
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

        movie_ratings = list(zip(movie_titles, ratings))
        sorted_movie_ratings = sorted(movie_ratings, key=lambda x: x[1], reverse=True)
        
        # Take top 5
        top_5 = sorted_movie_ratings[:5]
        
        # Format as list of dictionaries
        result = [{"title": title, "rating": float(rating)} for title, rating in top_5]
        
        # Debug top 5
        print(f"Top 5 movies: {result}")
        
        # Return the top 5
        return jsonify(result), 200
    except Exception as e:
        print(f"Prediction error: {str(e)}")
        return jsonify({'error': f'Ranking model error: {str(e)}'}), 500