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
    if user is None or not user.check_password(password):
        return jsonify(success=False, message="Invalid Credentials"), 400

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
        if password != confirmpassword:
            return jsonify(success=False, message="Re-type Password"), 400

    except KeyError as e:
        return jsonify(success=False, message="%s not sent in the request" % e.args), 400

    if '@' not in email:
        return jsonify(success=False, message="Please enter a valid email"), 400

    u = User(name, email, password)
    db.session.add(u)
    try:
        db.session.commit()
    except IntegrityError as e:
        return jsonify(success=False, message="This email already exists"), 400

    return jsonify(success=True)
