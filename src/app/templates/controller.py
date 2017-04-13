from flask import Blueprint, request, render_template, \
                  flash, g, session, redirect, url_for, jsonify, make_response
from flask_wtf import FlaskForm 
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, DateField
from flask_bootstrap import Bootstrap
from app import db,app,login_manager
from flask_cors import CORS
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from wtforms.validators import InputRequired, Email, Length,URL
#Bootstrap(app)



Bootstrap(app)


class LoginForm(FlaskForm):
    title = StringField('title', validators=[InputRequired(), Length(min=4, max=15)])
    director = StringField('director', validators=[InputRequired(), Length(min=8, max=80)])
    description = StringField('description',validators=[InputRequired()])
    trailer_url = StringField('url',validators=[InputRequired(),URL(message = 'Invalid URL')])
    duration = StringField('duration',validators=[InputRequired()])
    birthdate = DateField('birthdate',validators=[InputRequired()], render_kw={"placeholder": "format: yyyy-mm-dd"})
    
    release_date = DateField('release_date',validators=[InputRequired(),  render_kw={"placeholder": "format: yyyy-mm-dd"}])
    off_theatre_date = DateField('off_theatre_date',validators=[InputRequired(), render_kw={"placeholder": "format: yyyy-mm-dd"}])

'''
@mod_helper.route('/test', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = Buyers.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return render_template('dashboard.html', name=current_user.username)
                

        return '<h1>Invalid username or password</h1>'
        

    return render_template('login.html', form=form)

'''
'''
class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=80)])
    phone_Number = StringField('phone_Number', validators=[InputRequired(),Length(min=7, max=20)])
    address = TextAreaField('address', validators=[InputRequired(), Length(min=10, max=200)])
    birthdate = DateField('birthdate',validators=[InputRequired()], render_kw={"placeholder": "format: yyyy-mm-dd"})


@mod_buyers.route('/login', methods=['GET', 'POST'])
def login():
    if g.user is not None and g.user.is_authenticated:
        return render_template('dashboard.html', name = current_user.username)
    form = LoginForm()

    if form.validate_on_submit():
        user = Buyers.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user, remember=form.remember.data)
                return render_template('dashboard.html', name=current_user.username)
                

        return '<h1>Invalid username or password</h1>'
        

    return render_template('login.html', form=form)

@mod_buyers.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegisterForm()

    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        try:
            new_user = Buyers(username=form.username.data, email=form.email.data, password=hashed_password, phone_Number=form.phone_Number.data, address=form.address.data, birthdate=form.birthdate.data)
            db.session.add(new_user)
            db.session.commit()
            return '<h1>New user has been created!</h1>'
        except:
            return render_template('signup.html', form=form)

                        
        #return '<h1>' + form.username.data + ' ' + form.email.data + ' ' + form.password.data + '</h1>'

    return render_template('signup.html', form=form)


@mod_buyers.route('/logout')
@login_required
def logout():
    g.user = None
    session.clear()
    logout_user()
    return render_template('index.html')


@mod_buyers.route('/showallitems')
@login_required
def showallit():
    array=Product.query.all()
    return render_template("allproduct.html",product=array)
''' 