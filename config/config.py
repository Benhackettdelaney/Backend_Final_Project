import os

# Configuration to store the app settings 
class Config:
    # URI to connect to the SQLite database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///databasemovie.db'  
    SQLALCHEMY_TRACK_MODIFICATIONS = False
