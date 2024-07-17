from connector import db
from uuid import uuid4

class User(db.Model):
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
        if check_4_dupe:
            print("User wasn't save, already exists")
            return False
        db.session.add(self)
        db.session.commit()
        return True