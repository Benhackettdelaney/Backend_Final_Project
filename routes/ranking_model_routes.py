@app.route('/rank_movies', methods=['POST'])
def rank_movies():

    user_ratings = request.json.get('user_ratings') 
    
    movie_ids = [rating['movie_id'] for rating in user_ratings]
    ratings = [rating['rating'] for rating in user_ratings]

    ranking_input = prepare_ranking_input(movie_ids, ratings)  

    ranking_predictions = ranking_model.predict(ranking_input)

    ranked_movies = []
    for i, movie_id in enumerate(movie_ids):
        movie = Movie.query.get(movie_id)
        ranked_movies.append({
            'movie_id': movie.id,
            'movie_title': movie.movie_title,
            'movie_genres': movie.movie_genres,
            'predicted_rank': ranking_predictions[i]
        })

    ranked_movies.sort(key=lambda x: x['predicted_rank'], reverse=True)

    return jsonify(ranked_movies)
