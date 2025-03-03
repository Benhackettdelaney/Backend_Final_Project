from flask import Flask, jsonify, request
from models import Movie  
import numpy as np

app = Flask(__name__)


@app.route('/recommendations', methods=['GET'])
def get_recommendations():
    
    genre = request.args.get('genre')
    user_id = request.args.get('user_id')  
    
    movies = Movie.query.filter_by(movie_genres=genre).all()
    
    movie_features = [movie_to_features(movie) for movie in movies]

    predictions = basic_retrieval_model.predict(np.array(movie_features))  

    recommended_movies = []
    for i in range(len(predictions)):
        movie = movies[i]
        recommended_movies.append({
            'movie_id': movie.id,
            'movie_title': movie.movie_title,
            'movie_genres': movie.movie_genres,
            'rating': predictions[i]  
        })

    return jsonify(recommended_movies)
