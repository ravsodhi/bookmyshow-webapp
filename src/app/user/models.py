from flask_sqlalchemy import SQLAlchemy
from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from hashlib import md5 
class User (db.Model):
    """
    Create an User table
    """
    __tablename__ = "user"
    id = db.Column('id', db.Integer, primary_key = True,autoincrement=True)
    name = db.Column('name', db.String(255))
    password = db.Column('password', db.String(255))
    email = db.Column('email',db.String(255), unique = True)
    is_admin = db.Column('is_admin',db.Boolean)

    def __init__(self,name,email,password,is_admin):
        self.name = name
        self.password = generate_password_hash(password)
        self.email = email
        self.is_admin = is_admin

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
    def is_active(self):
        """True, as all users are active."""
        return True

    def get_id(self):
        """Return the email address to satisfy Flask-Login's requirements."""
        return self.id

    def is_authenticated(self):
        """Return True if the user is authenticated."""
        return self.authenticated

    def is_anonymous(self):
        """False, as anonymous users aren't supported."""
        return False
    def avatar(self,size):
        return 'http://www.gravatar.com/avatar/%s?id=identicon&s=%d' % (md5(self.email.encode('utf-8')).hexdigest(), size)

    def __repr__(self):
        #return "User { username: %r }"%(self.username)
        return "'User' { 'id' :%r,'name': %r }"%(self.id,self.name)
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