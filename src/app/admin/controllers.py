from app import app,db,requires_auth,login_manager
from functools import wraps
from flask import render_template,session
from app.user.models import User
from app.movie.models import Movie
from app.auditorium.models import Auditorium
from app.screening.models import Screening
from app.forms.models import LoginForm,AdminLoginForm

from app.seat.models import Seat
from datetime import *


from flask import Blueprint, request, render_template,flash, g, session, redirect, url_for, jsonify, make_response
from flask_wtf import FlaskForm ,RecaptchaField
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, DateField, SelectField,IntegerField, SelectMultipleField
from werkzeug.security import generate_password_hash, check_password_hash
from flask_bootstrap import Bootstrap
from flask_cors import CORS
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from wtforms.validators import InputRequired, Email, Length,URL
mod_admin = Blueprint('admin', __name__)

@mod_admin.route('/admin')
def admin_form():
	if 'user_id' not in session:
		return render_template('401.html'),401
	else:
		print(session['user_id'])
		use = User.query.filter_by(id = session['user_id']).first()
		print(use.is_admin)
		ans = {'log':"Logout",'val': use.name}


		if use.is_admin is True:
			return render_template('admin.html',log=ans),200
		else:
			return render_template('401.html'),401

@app.before_request
def before_request():
    g.user = current_user

