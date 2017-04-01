from flask_sqlalchemy import SQLAlchemy
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
class User (db.Model):
    """
    Create an User table
    """
    __tablename__ = "users"
    id = db.Column('id', db.Integer, primary_key = True,autoincrement=True)
    name = db.Column('name', db.String(255))
    password = db.Column('password', db.String(255))
    email = db.Column('email',db.String(255), unique = True)
    is_admin = db.Column(db.Boolean, default=False)

    def __init__(self,name,email,password):
        self.name = name
        self.password = generate_password_hash(password)
        self.email = email

    def check_password(self, password):
        """
        Check if hashed password matches actual password
        """
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            'id' : self.id,
            'name': self.name,
            'email': self.email,
        }
    def __repr__(self):
        #return "User { username: %r }"%(self.username)
        return "User { id :%r,username: %r }"%(self.id,self.name)
'''
In the User model, we make use of some of Werkzeug's handy security helper
methods, generate_password_hash, which allows us to hash passwords, 
and check_password_hash, which allows us ensure the hashed password
matches the password. To enhance security, we have a password method 
which ensures that the password can never be accessed; instead an
error will be raised.
we have an is_admin field which is set to False by default. 
We will override this when creating the admin user
'''