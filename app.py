from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate
from models import db  
from models import db, Movie 
from routes.auth import auth_bp  
from routes.movie_routes import movies_bp  

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///recommender.db"  
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 

db.init_app(app)  
bcrypt = Bcrypt(app)  
jwt = JWTManager(app)  
migrate = Migrate(app, db) 


app.register_blueprint(auth_bp, url_prefix="/auth") 
app.register_blueprint(movies_bp, url_prefix="/movies")  


if __name__ == "__main__":
    app.run(debug=True) 
