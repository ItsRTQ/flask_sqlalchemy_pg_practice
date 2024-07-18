from connector import db # <- IMPORTANTE, utilizamos el mismo db al que le hicimos init_app pq es el que esta connectado con el app de flask
from uuid import uuid4

class User(db.Model): # <- extendemos de db.Model para poder crear el modelo para la tabla
    """Sets up the tables for the database to withhold the users objects
        Settea las columnas para la tabla de user
    """
    id = db.Column(db.String(44), primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, id=None, username=None, email=None, password=None):
        """Inicializamos los usuarios con los attributos neccesarios"""
        if not id:
            self.id = str(uuid4())
        else:
            self.id = id
        if username and email and password:
            self.username = str(username)
            self.email = str(email)
            self.password = str(password)
        else:
            raise Exception("All attributes except id must be provided")
    
    def save(self):
        """Guardamos los datos a la base de datos"""
        check_4_dupe = User.query.filter_by(email=self.email).first() # vemos si el email ya existe. Ejamplo, ya esta registrado
        if check_4_dupe: # verificamos el valor de check_4_dupe el cual debe ser None si el email no existe en la Base de datos
            print("User wasn't save, already exists")
            return False # no guardamos y solo devolvemos falso ya que no paso nada
        db.session.add(self) # añade la instancia a la session
        db.session.commit() # Commete los cambias añadidos a la session. En este caso guardando la instancia a la base de datos
        return True # devolvemos True pq todo corrio correctamente. No es necesario solo son detalles para saber que pasa detras de todo