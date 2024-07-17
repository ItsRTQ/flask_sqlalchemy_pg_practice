from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import os

db = SQLAlchemy()

def configure(app):
    db_password = os.getenv('DB_PASSCODE')
    URI = f"postgresql://postgres:{db_password}@localhost:5000/practiceDB"
    app.config['SQLALCHEMY_DATABASE_URI'] = URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    create_db(URI)
    db.init_app(app)
    return db

def create_db(db_uri):
    engine = create_engine(db_uri)
    if not database_exists(engine.url):
        create_database(engine.url)
        print(f'Database {engine.url.database} created successfully.')
    else:
        print(f'Database {engine.url.database} already exists.')
