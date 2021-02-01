from app import db #taking it from the application? interesting

class User(db.Model):#Inherits from db.Model, a base class for all models
    id=db.Column(db.Integer, primary_key=True)
    username=db.Column(db.String(64), index=True, unique=True)
    email= db.Column(db.String(120), index=True, unique=True)
    password_hash= db.Column(db.String(128))
    def __repr__(self):
        return "<User {}>".format(self.username)#Tells python interpreter how to print objects in this class
