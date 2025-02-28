from flask import Flask
from routes.movie_routes import movie_bp
from extensions.__init__ import db, migrate
from config.config import Config
from models.movie import Movie 
from models.user import User 

app = Flask(__name__)


app.config.from_object(Config)


db.init_app(app)
migrate.init_app(app, db)


app.register_blueprint(movie_bp, url_prefix='/movies')

@app.route('/', methods=['GET'])
def hello_world():
    return "Hello World"

with app.app_context():
    db.create_all()

if __name__ == '__main__':
    app.run(port=3000, debug=True)
