from flask import Flask
from connector import configure
from models.user import User
from dotenv import load_dotenv

load_dotenv() # loads the enviroment variables

def create_app():
    """Starts the flask app and initializes the connection with db"""
    app = Flask(__name__)
    db = configure(app)
    
    with app.app_context():
        """Creates all the neccesary tables"""
        db.create_all()
    
    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        new_user = User(username="William", email="william@email.com", password="demo12345")
        new_user.save()
    app.run(host="0.0.0.0", port=8000, debug=True)