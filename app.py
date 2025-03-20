# app.py
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from routes.movie_routes import movie_bp
from routes.ranking_routes import ranking_bp
from routes.watchlist_routes import watchlist_bp
from routes.rating_routes import rating_bp
from routes.auth import auth_bp 
from routes.reviews_routes import review_bp
from extensions import db, migrate
from config.config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = 'your-secret-key-here'
app.config['JWT_SECRET_KEY'] = 'your-jwt-secret-key-here'
app.config['JWT_TOKEN_LOCATION'] = ['cookies', 'headers']  
app.config['JWT_COOKIE_CSRF_PROTECT'] = True
app.config['JWT_ACCESS_TOKEN_EXPIRES'] = 3600

jwt = JWTManager(app)

CORS(app, supports_credentials=True, origins=["http://localhost:3000"])
print("CORS configured with origins: http://localhost:3000")
app.logger.debug("Starting Flask app")

db.init_app(app)
migrate.init_app(app, db)

# Register blueprints
app.register_blueprint(movie_bp, url_prefix='/movies')
app.register_blueprint(ranking_bp, url_prefix='/ranking')
app.register_blueprint(watchlist_bp, url_prefix='/watchlists')
app.register_blueprint(rating_bp, url_prefix='/ratings')
app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(review_bp, url_prefix='/reviews')

@app.route('/', methods=['GET'])
def hello_world():
    return "Hello World"

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(port=5000, debug=True)