from flask import Flask
from connector import configure
from models.user import User
# from dotenv import load_dotenv

# load_dotenv() # loads the enviroment variables

def create_app():
    """Starts the flask app and initializes the connection with db"""
    app = Flask(__name__)
    db = configure(app)
    
    with app.app_context():
        """Crea todas las tablas neccesarias en base a tus objetos
            en este ejemplo so lo crea una para User
        """
        db.create_all()
    return app

if __name__ == '__main__':
    app = create_app() # llamamos a create_app() que nos devuelve el app ya configurada
    with app.app_context(): # usamos app_context para que python sepa en que contexto hacemos lo ejecutado
        new_user = User(username="William", email="william@email.com", password="demo12345") # Creamos usuario cualquiera
        new_user.save() # utilizamos el save del user Windows(CTRL + Click save) or Mac(COMMAND + Click save) para ir al metodo
    app.run(host="0.0.0.0", port=8000, debug=True)