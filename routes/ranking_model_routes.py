# routes/ranking_routes.py
#from flask import Blueprint, request, jsonify
#import tensorflow as tf
#import numpy as np

#ranking_bp = Blueprint('ranking_bp', __name__)

#@ranking_bp.route('', methods=['GET'])  
#def rank_movies():
#    json_data = request.get_json()
##    if json_data is None or 'user_id' not in json_data:
#        return jsonify({'error': 'Invalid input'}), 400
#
#    user_id = json_data['user_id']
 #   movie_titles = ["Speed (1994)", "Rent-a-Kid (1995)"]
 #   num_movie_titles = len(movie_titles)

 #   user_ids = np.repeat(np.array([user_id]), num_movie_titles)
 #   input_data = {
 #       "user_id": user_ids,
#        "movie_title": movie_titles
 #   }

  #  ranking_model = tf.saved_model.load("ml_models/ranking_model")
 #   result = ranking_model(input_data).numpy().tolist()

  #  return jsonify(result), 200