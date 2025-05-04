from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# Initializes the SQLAlchemy for database operations
db = SQLAlchemy()

# Initializing the Migrate for handling the migrations
migrate = Migrate()
