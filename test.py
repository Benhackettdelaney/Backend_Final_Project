
import tensorflow as tf;
import numpy as np;


ranking_model = tf.saved_model.load("ml_models/ranking_model")

# Get user ratings from request
# user_ratings = request.json.get('user_ratings') 

# Extract movie IDs and ratings from the user ratings data
# movie_ids = [rating['movie_id'] for rating in user_ratings]
# ratings = [rating['rating'] for rating in user_ratings]

# Prepare input for the ranking model
# ranking_input = prepare_ranking_input(movie_ids, ratings)  
ranking_input = {"user_id": np.array(["42"]), "movie_title": ["Speed (1994)"]}  

# Predict rankings using the model
# ranking_predictions = ranking_model.predict(ranking_input)

result = ranking_model(ranking_input).numpy()

print(result);

# Load it back; can also be done in TensorFlow Serving.lig
# loaded = tf.saved_model.load("ml_models/retrieval_model")

# # Pass a user id in, get top predicted movie titles back.
# scores, titles = loaded(["42"])

# print(f"Recommendations: {titles[0][:3]}")