# This file was going to used for querying the retrieval and ranking, as the model didn't work as expected it was left unused

#import numpy as np
#from models.movie import Movie
#from extensions import db, ratings_table

#def movie_to_features(movie, user_id=None):
   # """
    #Convert a movie's details into a feature vector.
    
   # Args:
    #    movie (Movie): The Movie object.
    #    user_id (int, optional): If provided, include the user's rating.
    
   # Returns:
   #     np.array: Feature vector with genre vector and rating.
  #  """
   # genre_vector = genre_to_vector(movie.movie_genres)
    #rating = db.session.query(ratings_table.c.rating).filter_by(
   #     movie_id=movie.id, user_id=user_id
   # ).scalar() or 0.0 if user_id else 0.0  
    
    #return np.array(genre_vector + [rating])

#def genre_to_vector(genres):
   # """
  #  Convert a comma-separated genre string into a binary vector.
    
   # Args:
   #     genres (str): Comma-separated string of genres (e.g., "Action,Comedy").
    
   # Returns:
  #      list: Binary vector representing genre presence.
   # """
   # all_genres = ["Action", "Comedy", "Drama", "Children", "Adventure", "Crime", "Unknown"]
   # genre_vector = [0] * len(all_genres)
    
    #if genres:
   #     genre_list = [g.strip() for g in genres.split(',')]
   #     for genre in genre_list:
   #         if genre in all_genres:
    #            genre_vector[all_genres.index(genre)] = 1
    
    #return genre_vector

#def prepare_ranking_input(movie_ids, ratings=None, user_id=None):
  #  """
   # Prepare input data for a ranking model.
    
   # Args:
   #     movie_ids (list): List of movie IDs.
   #     ratings (list, optional): List of ratings (if provided, overrides DB fetch).
   #     user_id (int, optional): If provided, fetch ratings from DB for this user.
    
   # Returns:
   #     np.array: Array of feature vectors.
  #  """
   # features = []
   # ratings = ratings or [None] * len(movie_ids)  # Default to None if not provided
   # 
  #  if len(movie_ids) != len(ratings):
   #     raise ValueError("movie_ids and ratings must have the same length if ratings provided")

   # for movie_id, rating in zip(movie_ids, ratings):
   #     movie = Movie.query.get(movie_id)
   #     if not movie:
   #         continue
   #     
   #     movie_features = movie_to_features(movie, user_id=user_id)
   #     final_rating = rating if rating is not None else movie_features[-1]
   #     features.append(list(movie_features[:-1]) + [final_rating])
    
    #return np.array(features) if features else np.array([])