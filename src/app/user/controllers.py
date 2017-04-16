from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from app import app,db,requires_auth,login_manager
from functools import wraps
from flask import render_template,session
from app.user.models import User
from app.forms.models import LoginForm,RegisterForm
from flask import Blueprint, request, render_template,flash, g, session, redirect, url_for, jsonify, make_response
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, DateField, SelectField,IntegerField, SelectMultipleField
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from wtforms.validators import InputRequired, Email, Length,URL
import random
random = random.SystemRandom()
mod_user = Blueprint('user', __name__)

# because models.py is in this file
# we are not writing app.route instead of it we are writing @mod_user
# blueprint is use to define routes
# prefix is defined for all routes in this file
# we are importing this blueprint object and registering it in __init__.py

@app.before_request
def blueprintefore_request():
    g.user = current_user

@mod_user.route('/login', methods=['GET', 'POST'])
def login():
    print('lun')
    #print(self.request.url)
    print("/login")
    if not session.get('k'):
        session['k'] = url_for('helper.load_html')
    #session['k'] = url_for('helper.load_html')

    print(url_for('helper.load_html'))
    if 'user_id' in session:
        return redirect(session['k'])
    print("dscksjck")
    print(session['k'])
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            print(user.password)
            print(form.password.data)
            if check_password_hash(user.password, form.password.data):
                session['user_id'] = user.id
                p =  session['k']
                login_user(user)
                session['k'] = p

                print(session['k'])
                return redirect(session['k'])
            return render_template('login.html', form=form,message= "password is incorrect")
        else:
            return render_template('login.html', form=form,message= "Email is not registered")
    return render_template('login.html', form=form)

@mod_user.route('/logout')
def logout():
    #print('lun',self.request.url)
    g.user = None
    session.clear()
    logout_user()
    ans = {'log':"Login",'val':"Signup"}
    return redirect(url_for('helper.load_html'))

#This route is needed to show user's booking history
@mod_user.route('/api/user_info', methods=['GET'])
def get_user_info():
    try:
        if 'user_id' in session:
            user_id = session['user_id']
        else:
            print('notloggedin')
            return jsonify(success=False), 404
        user_touple = User.query.filter(User.id == user_id).first()
        name = user_touple.name
        email = user_touple.email
        id = user_touple.id
        return jsonify(success=True, info={'name':name, 'email':email,'id':id})
    except:
        return jsonify(success=False, message="Error in fetching user info"), 404
