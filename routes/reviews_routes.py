from flask import Blueprint, request, jsonify
from models.reviews import Review  
from models.user import User
from models.movie import Movie
from extensions import db
from flask_jwt_extended import jwt_required, get_jwt_identity

# This creates the blueprint for the review route
review_bp = Blueprint('review_bp', __name__)

# This allows users to create reviews
@review_bp.route('/create', methods=['POST'])
@jwt_required()
def create_review():
    user_id = get_jwt_identity() # Gets the id of the logged in user
    data = request.get_json() # Gets JSON data from the request

    # This checks if the movie id and content are filled
    if not data or 'movie_id' not in data or 'content' not in data:
        return jsonify({'error': 'Missing movie_id or content'}), 400
    
    # Finds the movie by its id
    movie = Movie.query.get(data['movie_id'])
    if not movie:
        return jsonify({'error': 'Movie not found'}), 404

    try:
        # this create a new review object 
        new_review = Review(
            user_id=user_id,
            movie_id=data['movie_id'],
            content=data['content']
            
        )
        db.session.add(new_review)
        db.session.commit()

        # returns the review infomation in the response
        return jsonify({
            'message': 'Review created successfully',
            'id': new_review.id,
            'user_id': new_review.user_id,
            'username': new_review.user.username,
            'movie_id': new_review.movie_id,
            'movie_title': new_review.movie.movie_title,
            'content': new_review.content,
            'created_at': new_review.created_at.isoformat()
        }), 201
    except Exception as e:
        db.session.rollback() # Reverts if errors occur
        return jsonify({'error': f'Failed to create review: {str(e)}'}), 500


# This GETs all the reviews for a specific movie
@review_bp.route('/movie/<movie_id>', methods=['GET'])
@jwt_required()  
def get_movie_reviews(movie_id):

    # Checks if the movie exists
    if not Movie.query.get(movie_id):
        return jsonify({'error': 'Movie not found'}), 404
    
    try:
        # Get all the reviews for this movie
        reviews = Review.query.filter_by(movie_id=movie_id).all()

        # Dictionary for for each review
        review_list = [{
            'id': review.id,
            'user_id': review.user_id,
            'username': review.user.username,
            'movie_id': review.movie_id,
            'movie_title': review.movie.movie_title,
            'content': review.content,
            'created_at': review.created_at.isoformat()
        } for review in reviews]
        return jsonify({'reviews': review_list}), 200
    except Exception as e:
        return jsonify({'error': f'Failed to fetch reviews: {str(e)}'}), 500

# This update allows users to edit their reviews
@review_bp.route('/update/<int:id>', methods=['PUT'])  
@jwt_required()
def update_review(id):
    user_id = get_jwt_identity()
    data = request.get_json()

    # Makes sure fields are filled
    if not data or 'content' not in data:
        return jsonify({'error': 'Missing content'}), 400
    
    review = Review.query.get_or_404(id)

    # This only allows users to update reviews with the same id
    if review.user_id != int(user_id):  
        return jsonify({'error': 'You can only edit your own reviews'}), 403

    try:
        review.content = data['content'] # updates the review content
        db.session.commit()
        return jsonify({
            'message': 'Review updated successfully',
            'id': review.id,
            'content': review.content
        }), 200
    except Exception as e:
        db.session.rollback() # Reverts changes if errors occur
        return jsonify({'error': f'Failed to update review: {str(e)}'}), 500

# The delete for the reviews
@review_bp.route('/delete/<int:id>', methods=['DELETE'])  
@jwt_required()
def delete_review(id):
    user_id = get_jwt_identity()
    review = Review.query.get_or_404(id)

    # This only allows users to delete reviews with the same id 
    if review.user_id != int(user_id):  
        return jsonify({'error': 'You can only delete your own reviews'}), 403

    try:
        db.session.delete(review)
        db.session.commit()
        return jsonify({'message': 'Review deleted successfully', 'id': id}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Failed to delete review: {str(e)}'}), 500