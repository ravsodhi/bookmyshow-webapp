from flask import Blueprint, request, session, jsonify
from sqlalchemy.exc import IntegrityError
from app import db
from .models import User
# because models.py is in this file
mod_user = Blueprint('user', __name__, url_prefix='/api')
# we are not writing app.route instead of it we are writing @mod_user
# blueprint is use to define routes
# prefix is defined for all routes in this file
# we are importing this blueprint object and registering it in __init__.py
@mod_user.route('/login', methods=['GET'])
def check_login():
    if 'user_id' in session:
        user = User.query.filter(User.id == session['user_id']).first()
        return jsonify(success=True, user=user.to_dict())

    return jsonify(success=False), 401

@mod_user.route('/login', methods=['POST'])
def login():
    try:
        email = request.form['email']
        password = request.form['password']
    except KeyError as e:
        return jsonify(success=False, message="%s not sent in the request" % e.args), 400

    user = User.query.filter(User.email == email).first()
    if user is None:
        return jsonify(success=False, message="Email is not registered")
    if not user.check_password(password):
        return jsonify(success=False, message="Wrong Password")
    session['user_id'] = user.id

    return jsonify(success=True, user=user.to_dict())

@mod_user.route('/logout', methods=['POST'])
def logout():
    session.pop('user_id')
    return jsonify(success=True)

#session exists until browser is closed
#browser throws away cookie after some time

@mod_user.route('/register', methods=['POST'])
def create_user():
    try:
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        confirmpassword = request.form['confirmpassword']
        

    except KeyError as e:
        return jsonify(success=False, message="%s not sent in the request" % e.args), 400

    if '@' not in email:
        return jsonify(success=False, message="Please enter a valid email")

    u = User(name, email, password)
    db.session.add(u)
    try:
        if password != confirmpassword:
            return jsonify(success=False, message="Password's don't match")
        db.session.commit()
    except IntegrityError as e:
        return jsonify(success=False, message="Email is already registered")

    return jsonify(success=True)

#This route is needed to show user's booking history
@mod_user.route('/user_info', methods=['GET'])
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
        return jsonify(success=True, info={'name':name, 'email':email})
    except:
        return jsonify(success=False, message="Error in fetching user info"), 404