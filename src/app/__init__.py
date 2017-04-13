# Import flask and template operators
from flask import Flask, render_template, session, jsonify
from flask_login import LoginManager
# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap


from functools import wraps

from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
# Define the WSGI application object

app = Flask(__name__)
# this is imported in run.py

# Configurations
app.config.from_object('config')
# this will try to import that config file

#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)
from app.user.models import User


# Sample HTTP error handling
migrate = Migrate(app,db)
manager = Manager(app)
manager.add_command('db',MigrateCommand)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.session_protection = "strong"
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(user_id)

@app.errorhandler(404)
def not_found(error):
   return render_template('404.html'), 200

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user_id' not in session:
            return jsonify(message="Unauthorized", success=False), 401
        	#next_url = get_current_url() # However you do this in Flask
        	#login_url = '%s?next=%s' % (url_for('login'), next_url)
        	#return redirect(login_url)
           # return jsonify(message="Unauthorized", success=False), 401
        return f(*args, **kwargs)
    return decorated

# Import a module / component using its blueprint handler variable (mod_auth)
from app.user.controllers import mod_user
from app.screening.controllers import mod_screening
from app.movie.controllers import mod_movie
from app.helper.controllers import mod_helper
from app.auditorium.controllers import mod_auditorium
from app.seat.controllers import mod_seat
from app.booking.controllers import mod_booking
from app.admin.controllers import mod_admin


# instead of doing app.route
# Register blueprint(s)
app.register_blueprint(mod_user)
app.register_blueprint(mod_screening)
app.register_blueprint(mod_movie)
app.register_blueprint(mod_helper)
app.register_blueprint(mod_auditorium)
app.register_blueprint(mod_seat)
app.register_blueprint(mod_booking)
app.register_blueprint(mod_admin)
Bootstrap(app)


# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()
