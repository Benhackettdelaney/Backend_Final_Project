from flask import Blueprint, request, jsonify
from models.movie import Movie
from models.watchlist import Watchlist
from models.rating import Rating
from models.reviews import Review  
from models.user import User
from models.actor import Actor  
from extensions import db
from flask_jwt_extended import jwt_required, get_jwt_identity
import os
import logging

logging.basicConfig(level=logging.DEBUG)

movie_bp = Blueprint('movie_bp', __name__)

AVAILABLE_IMAGES = ['bloodborne1.jpg']
IMAGE_FOLDER = 'static/movies'

def admin_required(f):
    @jwt_required()
    def decorated_function(*args, **kwargs):
        user_id = get_jwt_identity()
        user = User.query.get(int(user_id))
        if not user or not user.is_admin():
            return jsonify({"error": "Admin access required"}), 403
        return f(*args, **kwargs)
    return decorated_function

@movie_bp.route('/create', methods=['POST'], endpoint='create_movie')
@admin_required
def create_movie():
    logging.debug(f"Create movie request: {request.json}")
    if not request.is_json:
        return jsonify({'error': 'Content-Type must be application/json'}), 400

    data = request.json
    if not data or 'id' not in data or 'movie_title' not in data or 'movie_genres' not in data or 'actor_id' not in data or 'image' not in data:
        return jsonify({'error': 'Missing id, movie_title, movie_genres, actor_id, or image'}), 400

    if Movie.query.get(data['id']):
        return jsonify({'error': f"Movie with ID {data['id']} already exists"}), 409

    actor = Actor.query.get(data['actor_id'])
    if not actor:
        return jsonify({'error': f"Actor with ID {data['actor_id']} not found"}), 404

    image_filename = data['image']
    if image_filename not in AVAILABLE_IMAGES:
        return jsonify({'error': f"Image must be one of {', '.join(AVAILABLE_IMAGES)}"}), 400
    image_path = os.path.join(IMAGE_FOLDER, image_filename)
    if not os.path.isfile(image_path):
        return jsonify({'error': f"Image {image_filename} not found in {IMAGE_FOLDER}"}), 404
    image_url = f"movies/{image_filename}"

    try:
        new_movie = Movie(
            id=data['id'],
            movie_title=data['movie_title'],
            movie_genres=data['movie_genres'],
            description=data.get('description'),
            image_url=image_url
        )
        if actor in new_movie.actors:
            logging.debug(f"Duplicate actor ID {data['actor_id']} for new movie ID {data['id']}")
            return jsonify({'error': 'Please select a different actor'}), 400
        new_movie.actors.append(actor)
        db.session.add(new_movie)
        db.session.commit()
        response = {
            'message': 'Movie created successfully',
            'id': new_movie.id,
            'movie_title': new_movie.movie_title,
            'movie_genres': new_movie.movie_genres,
            'description': new_movie.description,
            'image_url': f"/static/{new_movie.image_url}",
            'created_at': new_movie.created_at.isoformat(),
            'actors': [{'id': actor.id, 'name': actor.name}]
        }
        logging.debug(f"Create movie response: {response}")
        return jsonify(response), 201
    except Exception as e:
        db.session.rollback()
        logging.error(f"Create movie error: {str(e)}")
        return jsonify({'error': 'Failed to create movie'}), 500

@movie_bp.route('', methods=['GET'], endpoint='get_movies')
@jwt_required()
def get_movies():
    logging.debug("Fetching all movies")
    movies = Movie.query.all()
    response = [{
        "id": movie.id,
        "movie_title": movie.movie_title if movie.movie_title else "Unknown Title",
        "movie_genres": movie.movie_genres if movie.movie_genres else "Unknown",
        "description": movie.description,
        "image_url": f"/static/{movie.image_url}" if movie.image_url else "/static/movies/bloodborne1.jpg",
        "created_at": movie.created_at.isoformat(),
        "ratingsCount": Rating.query.filter_by(movie_id=movie.id).count(),
        "reviewsCount": Review.query.filter_by(movie_id=movie.id).count(),
        "actors": [{'id': actor.id, 'name': actor.name} for actor in movie.actors.all()]
    } for movie in movies]
    logging.debug(f"Get movies response: {response[:2]}") 
    return jsonify(response), 200
        
@movie_bp.route('/<id>', methods=['GET'], endpoint='single_movie')
@jwt_required()
def single_movie(id):
    logging.debug(f"Fetching movie ID: {id}")
    movie = Movie.query.get_or_404(id)
    actors = [{'id': actor.id, 'name': actor.name} for actor in movie.actors.all()]
    response = {
        "id": movie.id,
        "movie_title": movie.movie_title if movie.movie_title else "Unknown Title",
        "movie_genres": movie.movie_genres if movie.movie_genres else "Unknown",
        "description": movie.description,
        "image_url": f"/static/{movie.image_url}" if movie.image_url else "/static/movies/bloodborne1.jpg",
        "created_at": movie.created_at.isoformat(),
        "actors": actors
    }
    logging.debug(f"Single movie response: {response}")
    return jsonify(response), 200

@movie_bp.route('/update/<id>', methods=['PUT'], endpoint='update_movie')
@admin_required
def update_movie(id):
    logging.debug(f"Update movie ID: {id}, data: {request.json}")
    if not request.is_json:
        return jsonify({'error': 'Content-Type must be application/json'}), 400
    
    data = request.json
    if not data or 'movie_title' not in data or 'movie_genres' not in data:
        return jsonify({'error': 'Missing movie_title or movie_genres'}), 400
    
    movie = Movie.query.get_or_404(id)
    try:
        movie.movie_title = data['movie_title']
        movie.movie_genres = data['movie_genres']
        movie.description = data.get('description', movie.description)
        if 'image' in data:
            image_filename = data['image']
            if image_filename not in AVAILABLE_IMAGES:
                return jsonify({'error': f"Image must be one of {', '.join(AVAILABLE_IMAGES)}"}), 400
            image_path = os.path.join(IMAGE_FOLDER, image_filename)
            if not os.path.isfile(image_path):
                return jsonify({'error': f"Image {image_filename} not found in {IMAGE_FOLDER}"}), 404
            movie.image_url = f"movies/{image_filename}"
        if 'actor_id' in data:
            actor = Actor.query.get(data['actor_id'])
            if not actor:
                return jsonify({'error': f"Actor with ID {data['actor_id']} not found"}), 404
            if actor not in movie.actors:  # Only append if actor is not already associated
                movie.actors.append(actor)
        db.session.commit()
        response = {
            'message': 'Movie updated successfully',
            'id': movie.id,
            'movie_title': movie.movie_title,
            'movie_genres': movie.movie_genres,
            'description': movie.description,
            'image_url': f"/static/{movie.image_url}" if movie.image_url else "/static/movies/bloodborne1.jpg",
            'created_at': movie.created_at.isoformat(),
            'actors': [{'id': actor.id, 'name': actor.name} for actor in movie.actors.all()]
        }
        logging.debug(f"Update movie response: {response}")
        return jsonify(response), 200
    except Exception as e:
        db.session.rollback()
        logging.error(f"Update movie error: {str(e)}")
        return jsonify({'error': 'Failed to update movie'}), 500

@movie_bp.route('/delete/<id>', methods=['DELETE'], endpoint='delete_movie')
@admin_required
def delete_movie(id):
    logging.debug(f"Delete movie ID: {id}")
    movie = Movie.query.get_or_404(id)
    try:
        Rating.query.filter_by(movie_id=id).delete()
        Review.query.filter_by(movie_id=id).delete()
        watchlists = Watchlist.query.all()
        for watchlist in watchlists:
            if id in watchlist.movie_ids:
                watchlist.movie_ids = [mid for mid in watchlist.movie_ids if mid != id]
        db.session.delete(movie)
        db.session.commit()
        logging.debug(f"Movie ID {id} deleted")
        return jsonify({'message': 'Movie and associated ratings, reviews, and watchlist entries deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        logging.error(f"Delete movie error: {str(e)}")
        return jsonify({'error': 'Failed to delete movie: {str(e)}'}), 500

@movie_bp.route('/<id>/actors', methods=['POST'], endpoint='add_actor')
@admin_required
def add_actor(id):
    logging.debug(f"Add actor to movie ID: {id}, data: {request.json}")
    if not request.is_json:
        return jsonify({'error': 'Content-Type must be application/json'}), 400
    
    data = request.json
    if not data or 'actor_id' not in data:
        return jsonify({'error': 'Missing actor_id'}), 400

    movie = Movie.query.get_or_404(id)
    actor = Actor.query.get_or_404(data['actor_id'])
    if actor in movie.actors:
        return jsonify({'error': 'Actor is already in movie'}), 400

    movie.actors.append(actor)
    try:
        db.session.commit()
        logging.debug(f"Actor {actor.name} added to movie {movie.movie_title}")
        return jsonify({'message': f'Actor {actor.name} added to movie {movie.movie_title}'}), 200
    except Exception as e:
        db.session.rollback()
        logging.error(f"Add actor error: {str(e)}")
        return jsonify({'error': f'Failed to add actor: {str(e)}'}), 500

@movie_bp.route('/<id>/actors/<actor_id>', methods=['DELETE'], endpoint='remove_actor')
@admin_required
def remove_actor(id, actor_id):
    logging.debug(f"Remove actor ID: {actor_id} from movie ID: {id}")
    movie = Movie.query.get_or_404(id)
    actor = Actor.query.get_or_404(actor_id)
    try:
        db.session.delete(actor)
        db.session.commit()
        logging.debug(f"Actor {actor.name} deleted from movie {movie.movie_title}")
        return jsonify({'message': f'Actor {actor.name} deleted from database'}), 200
    except Exception as e:
        db.session.rollback()
        logging.error(f"Remove actor error: {str(e)}")
        return jsonify({'error': f'Failed to delete actor: {str(e)}'}), 500

@movie_bp.route('/<id>/stats', methods=['GET'])
def movie_stats(id):
    logging.debug(f"Fetch stats for movie ID: {id}")
    movie = Movie.query.get_or_404(id)
    ratings_count = Rating.query.filter_by(movie_id=movie.id).count()
    reviews_count = Review.query.filter_by(movie_id=movie.id).count()
    response = {
        "ratings_count": ratings_count,
        "reviews_count": reviews_count,
        "actors_count": movie.actors.count()
    }
    logging.debug(f"Movie stats response: {response}")
    return jsonify(response), 200