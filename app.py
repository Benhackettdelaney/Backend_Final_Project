from flask import Flask, session
from flask_cors import CORS
from routes.movie_routes import movie_bp
from routes.ranking_routes import ranking_bp
from routes.watchlist_routes import watchlist_bp
from routes.rating_routes import rating_bp
from routes.auth import auth_bp 
from extensions import db, migrate
from config.config import Config
from models.user import User
from models.movie import Movie
from models.watchlist import Watchlist
from models.rating import Rating

app = Flask(__name__)
app.config.from_object(Config)
app.secret_key = 'your-secret-key-here'

app.secret_key = 'your-secret-key-here'
app.config['SESSION_COOKIE_SAMESITE'] = 'None'
app.config['SESSION_COOKIE_SECURE'] = False
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

@app.route('/', methods=['GET'])
def hello_world():
    return "Hello World"

if __name__ == '__main__':
    app.run(port=5000, debug=True)
