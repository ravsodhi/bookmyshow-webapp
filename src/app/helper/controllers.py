from flask import Blueprint, request, session, jsonify,redirect,url_for
from app import db,requires_auth
from functools import wraps
from flask import render_template
mod_todo = Blueprint('todo', __name__)
from app.user.models import User
from app.movie.models import Movie

@mod_todo.route('/api/todo', methods=['POST'])
def form_auth():
      if 'user_id' not in session:
           return jsonify(success=False)
      return jsonify(success=True)

@mod_todo.route('/home')
def load_html():
	if 'user_id' not in session:
		ans = {'log':"Login",'val':"Signup"}
		#ans.log = "Login"
		#ans.val = "Signup"
	else:
		name = User.query.filter_by(id = session['user_id']).first()
		print(name)
		print(type(name))
		name = name.name	
		ans = {'log':"Logout",'val':name}
		#ans.log = "Logout"
		#ans.val = User.query.filter_by(id = user_id).first()
	return render_template("movie.html",log =ans)

@mod_todo.route('/temp')
def login_html():
	if 'user_id' not in session:
		ans = {'log':"Login",'val':"Signup"}
		#ans.log = "Login"
		#ans.val = "Signup"
	else:
		name = User.query.filter_by(id = session['user_id']).first()
		print(name)
		print(type(name))
		name = name.name	
		ans = {'log':"Logout",'val':name}
		#ans.log = "Logout"
		#ans.val = User.query.filter_by(id = user_id).first()
	return render_template("movie.html",log =ans)

@mod_todo.route('/')
def redirect_chola():
	return redirect(url_for('.load_html'))

@mod_todo.route('/movie/<movie_id>')
def load_screening(movie_id):
	if 'user_id' not in session:
		ans = {'log':"Login",'val':"Signup"}
		#ans.log = "Login"
		#ans.val = "Signup"
	else:
		name = User.query.filter_by(id = session['user_id']).first()
		print(name)
		print(type(name))
		name = name.name	
		ans = {'log':"Logout",'val':name}
	movie = Movie.query.filter(Movie.id == movie_id).first()
	return render_template('screening.html',movie=movie,log=ans)


@mod_todo.route('/admin')
def admin_form():
	return render_template('admin.html')


