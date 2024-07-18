from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
import os

db = SQLAlchemy() # Crea una instancia de SQLAlchemy

def configure(app):
    """Initialize the db connection to URI using sqlalchemy"""
    URI = 'sqlite:///your_database_name.db'
    #db_password = os.getenv('DB_PASSCODE') # get the pasword from enviroment variable
    #URI = f"postgresql://postgres:{db_password}@localhost:5000/practiceDB" # utilizamos postgres
    app.config['SQLALCHEMY_DATABASE_URI'] = URI # sets the URI
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # Para que el programa corra mas rapido
    #create_db(URI) # creates the database if not exists, No se necesita para sqlite
    db.init_app(app) # Inicializamos la connecion entre el app y SQLAlchemy
    return db # devolvemos db para utilizarlo mas adelante si necesario

def create_db(db_uri):
    """Creates the database if doesnt exists
        No es necesario si usamos sqlite3
    """
    engine = create_engine(db_uri)
    if not database_exists(engine.url):
        create_database(engine.url)
        print(f'Database {engine.url.database} created successfully.')
    else:
        print(f'Database {engine.url.database} already exists.')
