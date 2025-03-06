# app.py
from flask import Flask
from routes.movie_routes import movie_bp
from routes.ranking_routes import ranking_bp
from routes.watchlist_routes import watchlist_bp
from extensions import db, migrate, ratings_table, watchlist_table
from config.config import Config
from models.movie import Movie 
from models.user import User 

app = Flask(__name__)
app.config.from_object(Config)

db.init_app(app)
migrate.init_app(app, db)

app.register_blueprint(movie_bp, url_prefix='/movies')
app.register_blueprint(ranking_bp, url_prefix='/ranking')
app.register_blueprint(watchlist_bp, url_prefix='/watchlist')

@app.route('/', methods=['GET'])
def hello_world():
    return "Hello World"

with app.app_context():
    db.create_all()
    print("Database tables created or verified.")

if __name__ == '__main__':
    app.run(port=5000, debug=True)