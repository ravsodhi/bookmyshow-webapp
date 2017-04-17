from flask_sqlalchemy import SQLAlchemy
from app import db
from app.user.models import User
from app.movie.models import Movie
from app.auditorium.models import Auditorium
from app.screening.models import Screening
from app.seat.models import Seat
from datetime import *
from flask import Blueprint, request, render_template,flash, g, session, redirect, url_for, jsonify, make_response
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, DateField, SelectField,IntegerField, SelectMultipleField
from werkzeug.security import generate_password_hash, check_password_hash
from wtforms.validators import InputRequired, Email, Length,URL













class NonValidatingSelectMultipleField(SelectMultipleField):
    """
    Attempt to make an open ended select multiple field that can accept dynamic
    choices added by the browser.
    """
    def pre_validate(self, form):
        pass
class NonValidatingSelectField(SelectField):
    """
    Attempt to make an open ended select multiple field that can accept dynamic
    choices added by the browser.
    """
    def pre_validate(self, form):
        pass



#session['URLI'] = "http://127.0.0.1/5000/home"
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(message="Please Enter your Email address"), Email(message='Invalid email'),Length(min=4, max=80)], render_kw={"placeholder": "Email"})
    password = PasswordField('Password', validators=[InputRequired(message="Please Enter password")],render_kw={"placeholder": "Password"})

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(message="Please Enter your Name"), Length(min=4, max=15)],render_kw={"placeholder": "Name"})
    email = StringField('Email', validators=[InputRequired(message="Please Enter your Email address"), Email(message='Invalid email'), Length(max=50)] ,render_kw={"placeholder": "Email"})
    password = PasswordField('Password', validators=[InputRequired(message="Please Enter your Password"), Length(min=5, max=80)],render_kw={"placeholder": "Password"})
    check_password = PasswordField('Retype password', validators=[InputRequired(message="Please Re-enter your Password"), Length(min=5, max=80)],render_kw={"placeholder": "Retype - Password"})

class AdminLoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired(message="Please Enter your Email address"), Email(message='Invalid email'),Length(min=4, max=80)], render_kw={"placeholder": "Email"})
    password = PasswordField('Password', validators=[InputRequired(message="Please Enter password")],render_kw={"placeholder": "Password"})

class AdminRegisterForm(FlaskForm):
    username = StringField('Username', validators=[InputRequired(message="Please Enter your Name"), Length(min=1, max=40)],render_kw={"placeholder": "Name"})
    email = StringField('Email', validators=[InputRequired(message="Please Enter your Email address"), Email(message='Invalid email'), Length(max=50)] ,render_kw={"placeholder": "Email"})
    password = PasswordField('Password', validators=[InputRequired(message="Please Enter your Password"), Length(min=8)],render_kw={"placeholder": "Password (Minimum 8 characters)"})
    check_password = PasswordField('Retype password', validators=[InputRequired(message="Please Re-enter your Password"), Length(min=8)],render_kw={"placeholder": "Retype - Password"})

class MovieForm(FlaskForm):
    title = StringField('Title', validators=[InputRequired(message="Please Enter Movie Title"), Length(min=1, max=40)],render_kw={"placeholder": "Title"})
    director = StringField('Director', validators=[InputRequired(message="Please Enter Movie Director"), Length(min=1, max=80)],render_kw={"placeholder": "Director"})
    discription = StringField('Description',validators=[InputRequired(message="Please Enter Movie description")],render_kw={"placeholder": "Description"})
    trailer_url = StringField('Url',validators=[InputRequired(),URL(message = 'Invalid URL')],render_kw={"placeholder": "URL"})
    duration = StringField('Duration',validators=[InputRequired(message="Please Enter Movie Duration")],render_kw={"placeholder":"Duration"})
    release_date = DateField('Release Date',validators=[InputRequired()],render_kw={"placeholder": "Release Date format: yyyy-mm-dd"})
    off_theatre_date = DateField('Off Theatre Date',validators=[InputRequired()], render_kw={"placeholder": "Off Theatre Date FlaskFormat: yyyy-mm-dd"})

class HallForm(FlaskForm):
    hall_name = StringField('Theatre Name', validators=[InputRequired(message="Please Enter New Hall Name"), Length(min=2, max=15)],render_kw={"placeholder": "Theatre Name"})
    hall_type = SelectField('Theatre Type', choices = [('Small', 'Small'),('Medium','Medium'),('Big', 'Big')])


class CostForm(FlaskForm):
    platinum = IntegerField('Platinum Seat Cost', validators=[InputRequired()],render_kw={"placeholder": "Platinum Cost"})
    gold = IntegerField('Gold Seat Cost', validators=[InputRequired()],render_kw={"placeholder": "Gold Cost"})
    silver = IntegerField('Silver Seat Cost', validators=[InputRequired()],render_kw={"placeholder": "Silver Cost"})

class ScreeningForm(FlaskForm):
	"""docstring for ScreeningForm"""
	selectmovie = NonValidatingSelectField('Select Movie', choices = [])
	selecthall = NonValidatingSelectMultipleField('Select Hall', choices = [])
	selecttime = NonValidatingSelectMultipleField('Select Timings', choices = [('09:00', '9:00am'),('12:00','12:00pm'),('15:00', '3:00pm'),('18:00','6:00pm'),('21:00','9:00pm')])
	
class Globalvar(db.Model):
    __tablename__ = "variables"
    id = db.Column('id', db.Integer,primary_key = True)
    token = db.Column('token', db.String)
    def __init__(self,token):
        self.token = token
    def __repr__(self):
        return "{'token':%r}"%(str(self.token))
