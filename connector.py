from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import os

db = SQLAlchemy() # creates an instance of SQLAlchemy

def configure(app):
    """Initialize the db connection to URI using sqlalchemy"""

    db_password = os.getenv('DB_PASSCODE') # get the pasword from enviroment variable
    URI = f"postgresql://postgres:{db_password}@localhost:5000/practiceDB"
    app.config['SQLALCHEMY_DATABASE_URI'] = URI # sets the URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # sets changes tracking to off
    create_db(URI) # creates the database
    db.init_app(app) # initialize the connection of SQLAlchemy and flask
    return db

def create_db(db_uri):
    """Creates the database if doesnt exists"""
    engine = create_engine(db_uri)
    if not database_exists(engine.url):
        create_database(engine.url)
        print(f'Database {engine.url.database} created successfully.')
    else:
        print(f'Database {engine.url.database} already exists.')
