# routes/ranking_routes.py
from flask import Blueprint, request, jsonify
import tensorflow as tf
import numpy as np

ranking_bp = Blueprint('ranking_bp', __name__)

# Load the ranking model (do this once at startup)
try:
    ranking_model = tf.saved_model.load("ml_models/ranking_model")
except Exception as e:
    print(f"Error loading ranking model: {e}")
    ranking_model = None

@ranking_bp.route('', methods=['GET'])
def get_ranking():
    # Debug: Log request details
    print(f"Request method: {request.method}")
    print(f"Request headers: {request.headers}")
    print(f"Query params: {request.args}")

    # Get user_id from query parameters
    user_id = request.args.get('user_id')
    if not user_id:
        return jsonify({'error': 'user_id is required'}), 400

    try:
        user_id = int(user_id)  # Ensure user_id is an integer
    except ValueError:
        return jsonify({'error': 'user_id must be an integer'}), 400

    # Check if model is loaded
    if ranking_model is None:
        return jsonify({'error': 'Ranking model not available'}), 500

    # Define movie titles (hardcoded for now; could be dynamic)
    movie_titles = ["Speed (1994)", "Rent-a-Kid (1995)"]
    num_movie_titles = len(movie_titles)

    # Prepare input for the model
    # Assuming user_id needs to be repeated for each movie title
    user_ids = np.repeat(np.array([user_id], dtype=np.int32), num_movie_titles)
    input_data = {
        "user_id": user_ids,
        "movie_title": movie_titles  # Model expects a list of strings
    }

    # Get ranking predictions
    try:
        # Call the model and get predictions
        predictions = ranking_model(input_data)
        
        # Convert TensorFlow tensor to NumPy array and then to list
        result = predictions.numpy().tolist()
        
        # Ensure the output matches the expected format: [[float], [float], ...]
        if not isinstance(result, list) or not all(isinstance(x, list) and len(x) == 1 for x in result):
            return jsonify({'error': 'Unexpected model output format'}), 500

        # Return the predictions
        return jsonify({'rankings': result}), 200
    except Exception as e:
        return jsonify({'error': f'Ranking model error: {str(e)}'}), 500