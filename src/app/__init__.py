# Import flask and template operators
from flask import Flask, render_template, session, jsonify

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

from functools import wraps

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

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
   return render_template('index.html'), 200

def requires_auth(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        if 'user_id' not in session:
        	next_url = get_current_url() # However you do this in Flask
        	login_url = '%s?next=%s' % (url_for('login'), next_url)
        	return redirect(login_url)
           # return jsonify(message="Unauthorized", success=False), 401
        return f(*args, **kwargs)
    return decorated

# Import a module / component using its blueprint handler variable (mod_auth)
from app.user.controllers import mod_user
from app.screening.controllers import mod_screening
from app.movie.controllers import mod_movie
from app.helper.controllers import mod_todo
from app.auditorium.controllers import mod_auditorium
from app.seat.controllers import mod_seat
from app.booking.controllers import mod_booking


# instead of doing app.route
# Register blueprint(s)
app.register_blueprint(mod_user)
app.register_blueprint(mod_screening)
app.register_blueprint(mod_movie)
app.register_blueprint(mod_todo)
app.register_blueprint(mod_auditorium)
app.register_blueprint(mod_seat)
app.register_blueprint(mod_booking)


# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()
