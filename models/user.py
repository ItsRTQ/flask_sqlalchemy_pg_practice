from connector import db
from uuid import uuid4

class User(db.Model):
    """Sets up the tables for the database to withhold the users objects"""
    id = db.Column(db.String(44), primary_key=True)
    username = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, id=None, username=None, email=None, password=None):
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
        check_4_dupe = User.query.filter_by(email=self.email).first()
        if check_4_dupe: # verify if a user with same password already exists
            print("User wasn't save, already exists")
            return False
        db.session.add(self) # adds the instance to the sessions
        db.session.commit() # Commits the changes to the sessions/save to db
        return True