# routes/watchlist_routes.py
from flask import Blueprint, request, jsonify
from models.movie import Movie
from models.user import User
from extensions import db, watchlist_table

watchlist_bp = Blueprint('watchlist_bp', __name__)

@watchlist_bp.route('/add', methods=['POST'])  
def add_to_watchlist():
    data = request.json
    user_id = data['user_id']
    movie_id = data['movie_id']
    title = data['title']  

    user = User.query.get_or_404(user_id)
    movie = Movie.query.get_or_404(movie_id)

    db.session.execute(
        watchlist_table.insert().values(user_id=user.id, movie_id=movie.id, title=title)
    )
    db.session.commit()

    return jsonify({'message': 'Movie added to watchlist successfully'}), 201

@watchlist_bp.route('/<int:user_id>', methods=['GET'])  
def get_user_watchlist(user_id):
    user = User.query.get_or_404(user_id)
    watchlist_items = db.session.query(Movie).join(watchlist_table).filter(watchlist_table.c.user_id == user.id).all()

    return jsonify([{
        "id": movie.id,
        "movie_title": movie.movie_title,
        "movie_genres": movie.movie_genres
    } for movie in watchlist_items]), 200

@watchlist_bp.route('/remove', methods=['POST'])
def remove_from_watchlist():
    data = request.json
    user_id = data['user_id']
    movie_id = data['movie_id']

    user = User.query.get_or_404(user_id)
    Movie.query.get_or_404(movie_id)  # Validate movie exists

    db.session.query(watchlist_table).filter_by(user_id=user_id, movie_id=movie_id).delete()
    db.session.commit()

    return jsonify({'message': 'Movie removed from watchlist successfully'}), 200