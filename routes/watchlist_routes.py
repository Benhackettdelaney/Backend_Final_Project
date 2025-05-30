from flask import Blueprint, request, jsonify
from models.movie import Movie
from models.user import User
from models.watchlist import Watchlist
from extensions import db
from flask_jwt_extended import jwt_required, get_jwt_identity

# This creates the blueprint for the watchlist route
watchlist_bp = Blueprint('watchlist_bp', __name__)

# This is the create route for the watchlists, all users can create watchlists
@watchlist_bp.route('/create', methods=['POST'])
@jwt_required() # Need to be authenticated
def create_watchlist():
    user_id = get_jwt_identity() # This gets the logged in users id
    if not request.is_json:
        return jsonify({'error': 'Content-Type must be application/json'}), 400
    
    data = request.json
    if not data or 'title' not in data:
        return jsonify({'error': 'Missing title'}), 400
    
    # This checks if the user exists
    if not User.query.get(int(user_id)):
        return jsonify({'error': 'Invalid user_id'}), 400

    try:
        # This prevents duplicate watchlists titles from being the same
        if Watchlist.query.filter_by(user_id=user_id, title=data['title']).first():
            return jsonify({'error': 'A watchlist with this title already exists'}), 409
        
        movie_ids = []
        # When creating a watchlist, the movie id is optional to add, it puts a movie into the watchlist can be left unfilled
        if 'movie_id' in data and data['movie_id']:
            movie_id = data['movie_id']
            movie = Movie.query.get(movie_id)  
            if not movie:
                return jsonify({'error': 'Invalid movie ID'}), 400  
            movie_ids.append(movie_id)
        
        is_public = data.get('is_public', False)

        # This creates the watchlist object
        watchlist = Watchlist(
            user_id=user_id,
            title=data['title'],
            movie_ids=movie_ids,
            is_public=is_public
        )
        db.session.add(watchlist)
        db.session.commit()
        return jsonify({'message': 'Watchlist created successfully', 'id': watchlist.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Failed to create watchlist: {str(e)}'}), 500

# This GETs all the watchlists
@watchlist_bp.route('', methods=['GET'])
@jwt_required()
def get_user_watchlist():
    user_id = get_jwt_identity()
    if not User.query.get(int(user_id)):
        return jsonify({'error': 'Invalid user_id'}), 400
    
    watchlists = Watchlist.query.filter_by(user_id=user_id).all()
    return jsonify([{
        "id": item.id,
        "user_id": item.user_id,
        "title": item.title,
        "movie_ids": item.movie_ids,
        "is_public": item.is_public
    } for item in watchlists]), 200

# This GETs all the watchlists by their ids
@watchlist_bp.route('/<int:id>', methods=['GET'])
@jwt_required()
def get_watchlist_item(id):
    user_id = get_jwt_identity()
    if not User.query.get(int(user_id)):
        return jsonify({'error': 'Invalid user_id'}), 400
    
    try:
        # This gets all the watchlists that have the same id as the current user
        watchlist = Watchlist.query.filter_by(id=id, user_id=user_id).first()
        if not watchlist:
            return jsonify({'error': 'Watchlist not found or not yours'}), 404
        
        return jsonify({
            "id": watchlist.id,
            "user_id": watchlist.user_id,
            "title": watchlist.title,
            "movie_ids": watchlist.movie_ids,
            "is_public": watchlist.is_public
        }), 200
    except Exception as e:
        return jsonify({'error': f'Failed to fetch watchlist item: {str(e)}'}), 500

# This update allows the user to edit the watchlist title
@watchlist_bp.route('/update/<int:id>', methods=['PUT'])
@jwt_required()
def update_watchlist_entry(id):
    user_id = get_jwt_identity()
    if not request.is_json:
        return jsonify({'error': 'Content-Type must be application/json'}), 400
    
    data = request.json
    # This checks if the field has been changed 
    if not data or ('title' not in data and 'movie_id' not in data and 'movie_ids' not in data and 'remove_movie_id' not in data and 'is_public' not in data):
        return jsonify({'error': 'Missing title, movie_id(s), remove_movie_id, or is_public'}), 400
    
    if not User.query.get(int(user_id)):
        return jsonify({'error': 'Invalid user_id'}), 400
    
    try:
        watchlist = Watchlist.query.filter_by(id=id, user_id=user_id).first()
        if not watchlist:
            return jsonify({'error': 'Watchlist not found or not yours'}), 404
        
        # This code updates the title
        if 'title' in data:
            watchlist.title = data['title']

        # add a single movie
        if 'movie_id' in data:
            movie_id = data['movie_id']
            Movie.query.get_or_404(movie_id)
            if movie_id in watchlist.movie_ids:
                return jsonify({'error': 'Movie is already in watchlist'}), 409
            watchlist.movie_ids = watchlist.movie_ids + [movie_id]

        # add multiple movies
        if 'movie_ids' in data:
            movie_ids = data['movie_ids']
            for movie_id in movie_ids:
                Movie.query.get_or_404(movie_id)
                if movie_id not in watchlist.movie_ids:
                    watchlist.movie_ids = watchlist.movie_ids + [movie_id]

        # Removes a movie
        if 'remove_movie_id' in data:
            remove_movie_id = data['remove_movie_id']
            if remove_movie_id not in watchlist.movie_ids:
                return jsonify({'error': 'Movie not found in watchlist'}), 404
            watchlist.movie_ids = [id for id in watchlist.movie_ids if id != remove_movie_id]

        # This updates the watchlist to either public or private
        if 'is_public' in data:
            watchlist.is_public = data['is_public']
        
        db.session.commit()
        return jsonify({'message': 'Watchlist updated successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Failed to update watchlist: {str(e)}'}), 500

# This allows users to delete watchlists
@watchlist_bp.route('/delete/<int:id>', methods=['DELETE'])
@jwt_required()
def remove_from_watchlist(id):
    user_id = get_jwt_identity()
    if not User.query.get(int(user_id)):
        return jsonify({'error': 'Invalid user_id'}), 400
    
    try:
        watchlist = Watchlist.query.filter_by(id=id, user_id=user_id).first()
        if not watchlist:
            return jsonify({'error': 'Watchlist not found or not yours'}), 404
        
        db.session.delete(watchlist)
        db.session.commit()
        return jsonify({'message': 'Watchlist deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Failed to remove watchlist: {str(e)}'}), 500

# This gets all the watchlists that are set to public
@watchlist_bp.route('/public', methods=['GET'])
def get_public_watchlists():
    try:
        public_watchlists = Watchlist.query.filter_by(is_public=True).all()
        return jsonify([{
            "id": item.id,
            "user_id": item.user_id,
            "title": item.title,
            "movie_ids": item.movie_ids,
            "is_public": item.is_public,
            "username": item.user.username # Gets the watchlist creators name
        } for item in public_watchlists]), 200
    except Exception as e:
        return jsonify({'error': f'Failed to fetch public watchlists: {str(e)}'}), 500

# This gets the details of a specific public watchlist with the id 
@watchlist_bp.route('/public/<int:id>', methods=['GET'])
def get_public_watchlist(id):
    try:
        watchlist = Watchlist.query.filter_by(id=id, is_public=True).first()
        if not watchlist:
            return jsonify({'error': 'Public watchlist not found'}), 404
        
        movie_details = []
        # Gets movie details
        for movie_id in watchlist.movie_ids:
            movie = Movie.query.get(movie_id)
            if movie:
                movie_details.append({
                    "id": movie.id,
                    "title": movie.movie_title,
                    "genres": movie.movie_genres
                })

        return jsonify({
            "id": watchlist.id,
            "user_id": watchlist.user_id,
            "title": watchlist.title,
            "movie_ids": watchlist.movie_ids,
            "movies": movie_details,
            "is_public": watchlist.is_public,
            "username": watchlist.user.username
        }), 200
    except Exception as e:
        return jsonify({'error': f'Failed to fetch public watchlist: {str(e)}'}), 500