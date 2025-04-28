from flask import Blueprint, jsonify, request
from extensions import db
from models.actor import Actor
from models.movie import Movie
from flask_jwt_extended import jwt_required
from routes.auth import admin_required
from datetime import datetime
import pycountry

actor_bp = Blueprint('actor_bp', __name__)

def is_valid_country(nationality):
    """Check if nationality is a valid country name using pycountry."""
    if not nationality:
        return True  
    return any(country.name.lower() == nationality.lower() for country in pycountry.countries)

@actor_bp.route('/countries', methods=['GET'])
@jwt_required()
def get_countries():
    """Return a list of valid country names."""
    try:
        countries = [country.name for country in pycountry.countries]
        return jsonify(countries), 200
    except Exception as e:
        return jsonify({'error': f'Failed to fetch countries: {str(e)}'}), 500

@actor_bp.route('', methods=['GET'])
@jwt_required()
def get_all_actors():
    actors = Actor.query.all()
    return jsonify([{
        'id': actor.id,
        'name': actor.name,
        'description': actor.description,
        'previous_work': actor.previous_work,
        'birthday': actor.birthday.isoformat() if actor.birthday else None,
        'nationality': actor.nationality,
        'movie_count': actor.movies.count()
    } for actor in actors]), 200

@actor_bp.route('', methods=['POST'])
@jwt_required()
@admin_required
def create_actor():
    if not request.is_json:
        return jsonify({'error': 'Content-Type must be application/json'}), 400
    
    data = request.json
    if not data or 'name' not in data:
        return jsonify({'error': 'Name is required'}), 400

    try:
        if len(data['name']) > 100:
            return jsonify({'error': 'Name must be 100 characters or less'}), 400
        description = data.get('description')
        if description and len(description) > 500:
            return jsonify({'error': 'Description must be 500 characters or less'}), 400
        previous_work = data.get('previous_work')
        if previous_work and len(previous_work) > 200:
            return jsonify({'error': 'Previous work must be 200 characters or less'}), 400
        nationality = data.get('nationality')
        if nationality and not is_valid_country(nationality):
            return jsonify({'error': 'Nationality must be a valid country name'}), 400
        
        birthday = data.get('birthday')
        if birthday and isinstance(birthday, str):
            try:
                birthday = datetime.strptime(birthday, '%Y-%m-%d')
            except ValueError:
                return jsonify({'error': 'Birthday must be in YYYY-MM-DD format'}), 400

        new_actor = Actor(
            name=data['name'],
            description=description,
            previous_work=previous_work,
            birthday=birthday,
            nationality=nationality
        )
        db.session.add(new_actor)
        db.session.commit()
        return jsonify({
            'message': 'Actor created successfully',
            'id': new_actor.id,
            'name': new_actor.name,
            'description': new_actor.description,
            'previous_work': new_actor.previous_work,
            'birthday': new_actor.birthday.isoformat() if new_actor.birthday else None,
            'nationality': new_actor.nationality
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Failed to create actor: {str(e)}'}), 500

@actor_bp.route('/<actor_id>', methods=['GET'])
@jwt_required()
def get_actor(actor_id):
    actor = Actor.query.get_or_404(actor_id)
    movies = [{'id': movie.id, 'movie_title': movie.movie_title} for movie in actor.movies.all()]
    return jsonify({
        'id': actor.id,
        'name': actor.name,
        'description': actor.description,
        'previous_work': actor.previous_work,
        'birthday': actor.birthday.isoformat() if actor.birthday else None,
        'nationality': actor.nationality,
        'movies': movies
    }), 200

@actor_bp.route('/<actor_id>', methods=['PUT'])
@jwt_required()
@admin_required
def update_actor(actor_id):
    if not request.is_json:
        return jsonify({'error': 'Content-Type must be application/json'}), 400
    
    data = request.json
    if not data or 'name' not in data:
        return jsonify({'error': 'Name is required'}), 400

    actor = Actor.query.get_or_404(actor_id)
    try:
        if len(data['name']) > 100:
            return jsonify({'error': 'Name must be 100 characters or less'}), 400
        description = data.get('description', actor.description)
        if description and len(description) > 500:
            return jsonify({'error': 'Description must be 500 characters or less'}), 400
        previous_work = data.get('previous_work', actor.previous_work)
        if previous_work and len(previous_work) > 200:
            return jsonify({'error': 'Previous work must be 200 characters or less'}), 400
        nationality = data.get('nationality', actor.nationality)
        if nationality and not is_valid_country(nationality):
            return jsonify({'error': 'Nationality must be a valid country name'}), 400
        
        birthday = data.get('birthday', actor.birthday)
        if birthday and isinstance(birthday, str):
            try:
                birthday = datetime.strptime(birthday, '%Y-%m-%d')
            except ValueError:
                return jsonify({'error': 'Birthday must be in YYYY-MM-DD format'}), 400

        actor.name = data['name']
        actor.description = description
        actor.previous_work = previous_work
        actor.birthday = birthday
        actor.nationality = nationality
        
        db.session.commit()
        return jsonify({
            'message': 'Actor updated successfully',
            'id': actor.id,
            'name': actor.name,
            'description': actor.description,
            'previous_work': actor.previous_work,
            'birthday': actor.birthday.isoformat() if actor.birthday else None,
            'nationality': actor.nationality
        }), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Failed to update actor: {str(e)}'}), 500

@actor_bp.route('/<actor_id>', methods=['DELETE'])
@jwt_required()
@admin_required
def delete_actor(actor_id):
    actor = Actor.query.get_or_404(actor_id)
    try:
        db.session.delete(actor)
        db.session.commit()
        return jsonify({'message': f'Actor {actor.name} deleted successfully'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Failed to delete actor: {str(e)}'}), 500

@actor_bp.route('/movies/<movie_id>/actors/<actor_id>', methods=['DELETE'])
@jwt_required()
@admin_required
def remove_actor_from_movie(movie_id, actor_id):
    movie = Movie.query.get_or_404(movie_id)
    actor = Actor.query.get_or_404(actor_id)
    
    try:
        if actor not in movie.actors:
            return jsonify({'error': f'Actor {actor.name} is not associated with this movie'}), 404
        
        movie.actors.remove(actor)
        db.session.commit()
        return jsonify({'message': f'Actor {actor.name} removed from movie {movie.movie_title}'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': f'Failed to remove actor from movie: {str(e)}'}), 500