# routes/review.py
from flask import Blueprint, request, jsonify
from models.reviews import Review
from models.user import User
from models.movie import Movie
from extensions import db
from flask_jwt_extended import jwt_required, get_jwt_identity

review_bp = Blueprint('review_bp', __name__)

@review_bp.route('/create', methods=['POST'])
@jwt_required()
def create_review():
    user_id = get_jwt_identity()
    data = request.get_json()
    if not data or 'movie_id' not in data or 'content' not in data:
        return jsonify({'error': 'Missing movie_id or content'}), 400
    
    movie = Movie.query.get(data['movie_id'])
    if not movie:
        return jsonify({'error': 'Movie not found'}), 404

    try:
        new_review = Review(
            user_id=user_id,
            movie_id=data['movie_id'],
            content=data['content']
        )
        db.session.add(new_review)
        db.session.commit()
        return jsonify({'message': 'Review created successfully', 'id': new_review.id}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Failed to create review: {str(e)}'}), 500

@review_bp.route('', methods=['GET'])
def get_all_reviews():
    reviews = Review.query.all()
    return jsonify([{
        'id': review.id,
        'user_id': review.user_id,
        'username': review.user.username,
        'movie_id': review.movie_id,
        'movie_title': review.movie.movie_title,
        'content': review.content,
        'created_at': review.created_at.isoformat()
    } for review in reviews]), 200

@review_bp.route('/user', methods=['GET'])
@jwt_required()
def get_user_reviews():
    user_id = get_jwt_identity()
    reviews = Review.query.filter_by(user_id=user_id).all()
    return jsonify([{
        'id': review.id,
        'movie_id': review.movie_id,
        'movie_title': review.movie.movie_title,
        'content': review.content,
        'created_at': review.created_at.isoformat()
    } for review in reviews]), 200

@review_bp.route('/update/<id>', methods=['PUT'])
@jwt_required()
def update_review(id):
    user_id = get_jwt_identity()
    review = Review.query.get_or_404(id)
    if review.user_id != int(user_id) and not User.query.get(user_id).is_admin():
        return jsonify({'error': 'Unauthorized'}), 403
    
    data = request.get_json()
    if not data or 'content' not in data:
        return jsonify({'error': 'Missing content'}), 400
    
    try:
        review.content = data['content']
        db.session.commit()
        return jsonify({'message': 'Review updated successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Failed to update review: {str(e)}'}), 500

@review_bp.route('/delete/<id>', methods=['DELETE'])
@jwt_required()
def delete_review(id):
    user_id = get_jwt_identity()
    review = Review.query.get_or_404(id)
    if review.user_id != int(user_id) and not User.query.get(user_id).is_admin():
        return jsonify({'error': 'Unauthorized'}), 403
    
    try:
        db.session.delete(review)
        db.session.commit()
        return jsonify({'message': 'Review deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Failed to delete review: {str(e)}'}), 500