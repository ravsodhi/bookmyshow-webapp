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
		ans = {'log':"Logout",'val': 'Hi! '+ use.name}


		if use.is_admin is True:
			return render_template('admin.html',log=ans),200
		else:
			return render_template('401.html'),401

@app.before_request
def before_request():
    g.user = current_user
'''
@mod_admin.route('/adminregister', methods=['GET','POST'])
def adminsignup():
	if 'user_id' in session:
		return redirect("http://127.0.0.1:5000/home")
	form = AdminRegisterForm()
	print('/adminregister')
	if form.validate_on_submit():
		print('/admin validate')
		if form.password.data != form.check_password.data:
			return render_template('adminregister.html', form=form ,message = "Passwords don't match")
		if '@' not in form.email.data:
			return render_template('adminregister.html',form=form, message="Please enter a valid email")
		try:
			print('admin added')
			print(form.password.data)
			new_user = User(name=form.username.data, email=form.email.data, password=form.password.data,is_admin = True)
			db.session.add(new_user)
			print(new_user)
			db.session.commit()
			print('admin added')
			print('lalala')
			print(new_user.id)
			session['user_id'] = new_user.id
			print(new_user.id)
			print(session['user_id'])
			login_user(new_user)
			print(session['user_id'])
			return redirect("http://127.0.0.1:5000/admin")
		except:
			print('admin not added')
			return render_template('adminregister.html', form=form,message = "Email is already Registered")
	return render_template('adminregister.html', form=form)
'''
@mod_admin.route('/adminlogin', methods=['GET', 'POST'])
def adminlogin():
	print("/adminlogin")
	if 'user_id' in session:
		return redirect("http://127.0.0.1:5000/home")
#	if g.user is not None and g.user.is_authenticated:
#		return redirect(session['k'])
	#	return redirect("http://127.0.0.1:5000/home")
	print("dscksjck")
	print(session['k'])

	form = AdminLoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user:
			print(user.is_admin)
			print(form.password.data)
			print(user.password)
			if check_password_hash(user.password, form.password.data):
				print('correct password')
				if user.is_admin is False:
					return render_template('adminlogin.html', form=form,message= "Access Denied")
				else:
					session['user_id'] = user.id
					login_user(user)
					print(session['k'])
					print('redirect to /admin')
					return redirect("http://127.0.0.1:5000/admin")
			print('password incorrect')
			return render_template('adminlogin.html', form=form,message= "password is incorrect")
		else:
			return render_template('adminlogin.html', form=form,message= "Email is not registered")
	return render_template('adminlogin.html', form=form)	