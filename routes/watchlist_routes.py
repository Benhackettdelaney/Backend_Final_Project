# routes/watchlist_routes.py
from flask import Blueprint, request, jsonify
from models.movie import Movie
from models.user import User
from extensions import db, watchlist_table

watchlist_bp = Blueprint('watchlist_bp', __name__)

@watchlist_bp.route('/create', methods=['POST'])
def add_to_watchlist():
    """Add a movie to a user's watchlist."""
    print(f"Request headers: {request.headers}")
    print(f"Request data: {request.data}")
    if not request.is_json:
        return jsonify({'error': 'Content-Type must be application/json'}), 400
    
    data = request.json
    print(f"Parsed JSON: {data}")
    if not data or 'user_id' not in data or 'movie_id' not in data or 'title' not in data:
        return jsonify({'error': 'Missing user_id, movie_id, or title'}), 400
    
    try:
        # Validate user and movie exist
        User.query.get_or_404(data['user_id'])
        Movie.query.get_or_404(data['movie_id'])
        
        # Check if entry already exists
        existing_entry = db.session.query(watchlist_table).filter_by(
            user_id=data['user_id'], movie_id=data['movie_id']
        ).first()
        if existing_entry:
            return jsonify({'error': 'Movie already in watchlist for this user'}), 409
        
        db.session.execute(
            watchlist_table.insert().values(
                user_id=data['user_id'],
                movie_id=data['movie_id'],
                title=data['title']
            )
        )
        db.session.commit()
        return jsonify({'message': 'Movie added to watchlist successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Failed to add to watchlist: {str(e)}'}), 500

@watchlist_bp.route('', methods=['GET'])
def get_all_watchlists():
    """Get all watchlist entries."""
    watchlist_items = db.session.query(watchlist_table).all()
    return jsonify([{
        "user_id": item.user_id,
        "movie_id": item.movie_id,
        "title": item.title
    } for item in watchlist_items]), 200

@watchlist_bp.route('/<int:user_id>', methods=['GET'])
def get_user_watchlist(user_id):
    """Get a specific user's watchlist."""
    User.query.get_or_404(user_id)  # Validate user exists
    watchlist_items = db.session.query(watchlist_table).filter_by(user_id=user_id).all()
    return jsonify([{
        "user_id": item.user_id,
        "movie_id": item.movie_id,
        "title": item.title
    } for item in watchlist_items]), 200

@watchlist_bp.route('/update/<int:id>', methods=['PUT'])
def update_watchlist_entry(id):
    """Update a watchlist entry's title by its pseudo-ID (index)."""
    if not request.is_json:
        return jsonify({'error': 'Content-Type must be application/json'}), 400
    
    data = request.json
    if not data or 'title' not in data:
        return jsonify({'error': 'Missing title'}), 400
    
    try:
        # Find the watchlist entry by pseudo-ID (index)
        watchlist_item = db.session.query(watchlist_table).offset(id - 1).limit(1).first()
        if not watchlist_item:
            return jsonify({'error': 'Watchlist entry not found'}), 404
        
        # Update the title
        db.session.execute(
            watchlist_table.update()
            .where(watchlist_table.c.user_id == watchlist_item.user_id)
            .where(watchlist_table.c.movie_id == watchlist_item.movie_id)
            .values(title=data['title'])
        )
        db.session.commit()
        return jsonify({'message': 'Watchlist entry updated successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Failed to update watchlist: {str(e)}'}), 500

@watchlist_bp.route('/delete/<int:id>', methods=['DELETE'])
def remove_from_watchlist(id):
    try:
        watchlist_item = db.session.query(watchlist_table).offset(id - 1).limit(1).first()
        if not watchlist_item:
            return jsonify({'error': 'Watchlist entry not found'}), 404
        
        db.session.execute(
            watchlist_table.delete()
            .where(watchlist_table.c.user_id == watchlist_item.user_id)
            .where(watchlist_table.c.movie_id == watchlist_item.movie_id)
        )
        db.session.commit()
        return jsonify({'message': 'Watchlist entry deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Failed to remove from watchlist: {str(e)}'}), 500