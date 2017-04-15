from app import app,db,requires_auth,login_manager
from functools import wraps
from flask import render_template,session
from app.user.models import User
from app.movie.models import Movie
from app.auditorium.models import Auditorium
from app.screening.models import Screening
from app.forms.models import LoginForm,AdminLoginForm,AdminRegisterForm,RegisterForm

from app.seat.models import Seat
from datetime import *
from sqlalchemy import *


from flask import Blueprint, request, render_template,flash, g, session, redirect, url_for, jsonify, make_response
from flask_wtf import FlaskForm ,RecaptchaField
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, DateField, SelectField,IntegerField, SelectMultipleField
from werkzeug.security import generate_password_hash, check_password_hash
from flask_cors import CORS
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from wtforms.validators import InputRequired, Email, Length,URL


mod_helper = Blueprint('helper', __name__)

@mod_helper.route('/api/helper', methods=['POST'])
def form_auth():
	print('helper controler',session)
	if 'user_id' not in session:
		return jsonify(success=False)
	return jsonify(success=True)

@mod_helper.route('/home')
def load_html():
	print(session)
	session['k'] = "http://127.0.0.1:5000/home"
	if 'user_id' not in session:
		ans = {'log':"Login",'val':"Signup"}
	else:
		print(session['user_id'])
		name = User.query.filter_by(id = session['user_id']).first()
		print(name)
		print(type(name))
		name = name.name	
		ans = {'log':"Logout",'val':name}
	return render_template("movie.html",log =ans)

@mod_helper.route('/')
def redirect_home():
	return redirect(url_for('.load_html'))

@mod_helper.route('/viewticket')
def view_ticket():
	print('reached at helper controllers')
	return render_template('ticket.html')
	

@mod_helper.route('/user/history')
def user_history():
	if 'user_id' not in session:
		return render_template('401.html'),401
	else:
		return render_template('user.html')
