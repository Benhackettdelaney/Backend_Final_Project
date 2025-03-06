# app.py
from flask import Flask
from flask_jwt_extended import JWTManager  
from routes.movie_routes import movie_bp
from routes.ranking_routes import ranking_bp
from routes.watchlist_routes import watchlist_bp
from routes.rating_routes import rating_bp
from routes.auth import auth_bp  
from extensions import db, migrate
from config.config import Config

app = Flask(__name__)
app.config.from_object(Config)
app.config['JWT_SECRET_KEY'] = 'your-secret-key-here' 

jwt = JWTManager(app)  

db.init_app(app)
migrate.init_app(app, db)

app.register_blueprint(movie_bp, url_prefix='/movies')
app.register_blueprint(ranking_bp, url_prefix='/ranking')
app.register_blueprint(watchlist_bp, url_prefix='/watchlists')
app.register_blueprint(rating_bp, url_prefix='/ratings')  
app.register_blueprint(auth_bp, url_prefix='/auth')

@app.route('/', methods=['GET'])
def hello_world():
    return "Hello World"

with app.app_context():
    #db.drop_all()
    #print("All tables dropped.")
    db.create_all()
    print("Database tables created or verified.")

if __name__ == '__main__':
    app.run(port=5000, debug=True)