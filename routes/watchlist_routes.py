from flask import Blueprint, request, jsonify, session
from models.movie import Movie
from models.user import User
from models.watchlist import Watchlist
from extensions import db

watchlist_bp = Blueprint('watchlist_bp', __name__)

def check_auth():
    """Check if a user is authenticated and return their user_id."""
    print(f"Session contents in check_auth: {session}")  
    user_id = session.get('user_id')
    if not user_id:
        print("No user_id found in session") 
        return None
    return user_id

@watchlist_bp.route('/create', methods=['POST'])
def add_to_watchlist():
    """Add a movie to the user's watchlist using user_id from request body."""
    if not request.is_json:
        return jsonify({'error': 'Content-Type must be application/json'}), 400
    
    data = request.json
    print(f"Parsed JSON: {data}")
    if not data or 'movie_id' not in data or 'title' not in data or 'user_id' not in data:
        return jsonify({'error': 'Missing movie_id, title, or user_id'}), 400
    
    user_id = data['user_id']
    if not User.query.get(user_id):
        return jsonify({'error': 'Unauthorized: Invalid user_id'}), 401
    
    try:
        Movie.query.get_or_404(data['movie_id'])
        existing_entry = Watchlist.query.filter_by(
            user_id=user_id, movie_id=data['movie_id']
        ).first()
        if existing_entry:
            return jsonify({'error': 'Movie already in your watchlist'}), 409
        
        new_entry = Watchlist(
            user_id=user_id,
            movie_id=data['movie_id'],
            title=data['title']
        )
        db.session.add(new_entry)
        db.session.commit()
        return jsonify({'message': 'Movie added to watchlist successfully', 'id': new_entry.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Failed to add to watchlist: {str(e)}'}), 500

@watchlist_bp.route('', methods=['GET'])
def get_user_watchlist():
    """Get the authenticated user's watchlist."""
    user_id = check_auth()
    if not user_id:
        return jsonify({'error': 'Unauthorized: Please log in'}), 401
    
    watchlist_items = Watchlist.query.filter_by(user_id=user_id).all()
    return jsonify([{
        "id": item.id,
        "user_id": item.user_id,
        "movie_id": item.movie_id,
        "title": item.title
    } for item in watchlist_items]), 200

@watchlist_bp.route('/<int:id>', methods=['GET'])
def get_watchlist_item(id):
    """Get a single watchlist item by ID for the authenticated user."""
    user_id = check_auth()
    if not user_id:
        return jsonify({'error': 'Unauthorized: Please log in'}), 401
    
    try:
        watchlist_item = Watchlist.query.filter_by(id=id, user_id=user_id).first()
        if not watchlist_item:
            return jsonify({'error': 'Watchlist entry not found or not yours'}), 404
        
        return jsonify({
            "id": watchlist_item.id,
            "user_id": watchlist_item.user_id,
            "movie_id": watchlist_item.movie_id,
            "title": watchlist_item.title
        }), 200
    except Exception as e:
        return jsonify({'error': f'Failed to fetch watchlist item: {str(e)}'}), 500

@watchlist_bp.route('/update/<int:id>', methods=['PUT'])
def update_watchlist_entry(id):
    user_id = check_auth()
    if not user_id:
        return jsonify({'error': 'Unauthorized: Please log in'}), 401
    
    if not request.is_json:
        return jsonify({'error': 'Content-Type must be application/json'}), 400
    
    data = request.json
    if not data or 'title' not in data:
        return jsonify({'error': 'Missing title'}), 400
    
    try:
        watchlist_item = Watchlist.query.filter_by(id=id, user_id=user_id).first()
        if not watchlist_item:
            return jsonify({'error': 'Watchlist entry not found or not yours'}), 404
        
        watchlist_item.title = data['title']
        db.session.commit()
        return jsonify({'message': 'Watchlist entry updated successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Failed to update watchlist: {str(e)}'}), 500

@watchlist_bp.route('/delete/<int:id>', methods=['DELETE'])
def remove_from_watchlist(id):
    """Remove a watchlist entry by ID for the authenticated user."""
    user_id = check_auth()
    if not user_id:
        return jsonify({'error': 'Unauthorized: Please log in'}), 401
    
    try:
        watchlist_item = Watchlist.query.filter_by(id=id, user_id=user_id).first()
        if not watchlist_item:
            return jsonify({'error': 'Watchlist entry not found or not yours'}), 404
        
        db.session.delete(watchlist_item)
        db.session.commit()
        return jsonify({'message': 'Watchlist entry deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Failed to remove from watchlist: {str(e)}'}), 500