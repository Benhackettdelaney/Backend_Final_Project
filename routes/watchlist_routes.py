from flask import Blueprint, request, jsonify
from models.movie import Movie
from models.user import User
from models.watchlist import Watchlist
from extensions import db

watchlist_bp = Blueprint('watchlist_bp', __name__)

@watchlist_bp.route('/create', methods=['POST'])
def create_watchlist():
    """Create a new watchlist for the user."""
    if not request.is_json:
        return jsonify({'error': 'Content-Type must be application/json'}), 400
    
    data = request.json
    print(f"Parsed JSON: {data}")
    if not data or 'title' not in data or 'user_id' not in data:
        return jsonify({'error': 'Missing title or user_id'}), 400
    
    user_id = data['user_id']
    if not User.query.get(int(user_id)):
        return jsonify({'error': 'Invalid user_id'}), 400
    
    try:
        if Watchlist.query.filter_by(user_id=user_id, title=data['title']).first():
            return jsonify({'error': 'A watchlist with this title already exists'}), 409
        
        watchlist = Watchlist(
            user_id=user_id,
            title=data['title'],
            movie_ids=[]
        )
        db.session.add(watchlist)
        db.session.commit()
        return jsonify({'message': 'Watchlist created successfully', 'id': watchlist.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Failed to create watchlist: {str(e)}'}), 500

@watchlist_bp.route('', methods=['GET'])
def get_user_watchlist():
    """Get all watchlists for the specified user."""
    user_id = request.args.get('user_id')
    if not user_id or not User.query.get(int(user_id)):
        return jsonify({'error': 'Invalid or missing user_id'}), 400
    
    watchlists = Watchlist.query.filter_by(user_id=user_id).all()
    return jsonify([{
        "id": item.id,
        "user_id": item.user_id,
        "title": item.title,
        "movie_ids": item.movie_ids
    } for item in watchlists]), 200

@watchlist_bp.route('/<int:id>', methods=['GET'])
def get_watchlist_item(id):
    """Get a single watchlist by ID for the specified user."""
    user_id = request.args.get('user_id')
    if not user_id or not User.query.get(int(user_id)):
        return jsonify({'error': 'Invalid or missing user_id'}), 400
    
    try:
        watchlist = Watchlist.query.filter_by(id=id, user_id=user_id).first()
        if not watchlist:
            return jsonify({'error': 'Watchlist not found or not yours'}), 404
        
        return jsonify({
            "id": watchlist.id,
            "user_id": watchlist.user_id,
            "title": watchlist.title,
            "movie_ids": watchlist.movie_ids
        }), 200
    except Exception as e:
        return jsonify({'error': f'Failed to fetch watchlist item: {str(e)}'}), 500

@watchlist_bp.route('/update/<int:id>', methods=['PUT'])
def update_watchlist_entry(id):
    """Update a watchlist’s title or append movie_ids to movie_ids."""
    if not request.is_json:
        return jsonify({'error': 'Content-Type must be application/json'}), 400
    
    data = request.json
    print(f"Parsed JSON: {data}")
    if not data or ('title' not in data and 'movie_id' not in data and 'movie_ids' not in data) or 'user_id' not in data:
        return jsonify({'error': 'Missing title, movie_id(s), or user_id'}), 400
    
    user_id = data['user_id']
    if not User.query.get(int(user_id)):
        return jsonify({'error': 'Invalid user_id'}), 400
    
    try:
        watchlist = Watchlist.query.filter_by(id=id, user_id=user_id).first()
        if not watchlist:
            return jsonify({'error': 'Watchlist not found or not yours'}), 404
        
        print(f"Before update - Watchlist: id={watchlist.id}, movie_ids={watchlist.movie_ids}")
        if 'title' in data:
            watchlist.title = data['title']
            print(f"Updated title to: {watchlist.title}")
        if 'movie_id' in data:  # Single movie ID
            movie_id = data['movie_id']
            print(f"Appending single movie_id: {movie_id}")
            Movie.query.get_or_404(movie_id)
            if movie_id in watchlist.movie_ids:
                return jsonify({'error': 'Movie already in this watchlist'}), 409
            watchlist.movie_ids = watchlist.movie_ids + [movie_id]
            print(f"After append (single) - Watchlist movie_ids: {watchlist.movie_ids}")
        if 'movie_ids' in data:  # Multiple movie IDs
            movie_ids = data['movie_ids']
            print(f"Appending multiple movie_ids: {movie_ids}")
            for movie_id in movie_ids:
                Movie.query.get_or_404(movie_id)
                if movie_id not in watchlist.movie_ids:
                    watchlist.movie_ids = watchlist.movie_ids + [movie_id]
            print(f"After append (multiple) - Watchlist movie_ids: {watchlist.movie_ids}")
        
        db.session.add(watchlist)
        db.session.commit()
        print(f"After commit - Watchlist movie_ids: {watchlist.movie_ids}")
        return jsonify({'message': 'Watchlist updated successfully'}), 200
    except Exception as e:
        db.session.rollback()
        print(f"Error during update: {str(e)}")
        return jsonify({'error': f'Failed to update watchlist: {str(e)}'}), 500

@watchlist_bp.route('/delete/<int:id>', methods=['DELETE'])
def remove_from_watchlist(id):
    """Delete a watchlist by ID for the specified user."""
    user_id = request.args.get('user_id')
    if not user_id or not User.query.get(int(user_id)):
        return jsonify({'error': 'Invalid or missing user_id'}), 400
    
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