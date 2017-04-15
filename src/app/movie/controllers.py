from flask import Blueprint, request, session, jsonify, render_template,redirect
from app import db
from .models import Movie
from app.user.models import User
from sqlalchemy import *
from datetime import *
from app.forms.models import MovieForm
mod_movie = Blueprint('movie', __name__)


@mod_movie.route('/api/movies', methods=['GET'])
def display_movies():
    movies = Movie.query.filter(and_(Movie.release_date <= date.today(),Movie.off_theatre_date >= date.today()))
    upMovies = Movie.query.filter(Movie.release_date > date.today())
    totalMovies = Movie.query.filter(Movie.off_theatre_date >= date.today())
    movie_array = []
    upmovies=[]
    total = []
    for i in totalMovies:
    	total.append(i.to_dict_movies())
    for i in movies:
        movie_array.append(i.to_dict_movies())
    for i in upMovies:
        upmovies.append(i.to_dict_movies())
    print(upmovies)
    print(movie_array)
    print(total)
    return jsonify(success=True, movies=movie_array,upmovies = upmovies,allmovies=total),200

@mod_movie.route('/api/movies/search', methods=['GET'])
def search_movies():
	query = request.args.get("query")
	if query == "":
		return jsonify(success=True,movies=""),200
	print(query)
	all_movies = Movie.query.filter(and_(Movie.release_date <= date.today(),Movie.off_theatre_date >= date.today(),Movie.title.like("%" + query + "%"))).all()
	print(all_movies)
	ju = []
	for i in all_movies:
		ju.append(i.to_dict_movies())
		print(i)
	return jsonify(success=True, movies=ju),200


@mod_movie.route('/movie/add', methods=['GET', 'POST'])
def addmovie():
	if 'user_id' not in session:
		return render_template('401.html'),401
	else:
		print(session['user_id'])
		use = User.query.filter_by(id = session['user_id']).first()
		print(use.is_admin)
		if use.is_admin is False:
			return render_template('401.html'),401
		else:
			form = MovieForm()
			ans = {'log':"Logout",'val':use.name}	
			if form.validate_on_submit():
					print("movie form")
					title = form.title.data
					print(title)
					director = form.director.data
					discription = form.discription.data
					duration = form.duration.data
					url = form.trailer_url.data
					release_date = form.release_date.data
					off_theatre_date = form.off_theatre_date.data
					print(release_date)
					release_date = str(release_date).split("-")
					release_date = date(int(release_date[0]),int(release_date[1]),int(release_date[2]))
					off_theatre_date = str(off_theatre_date).split("-")
					off_theatre_date = date(int(off_theatre_date[0]),int(off_theatre_date[1]),int(off_theatre_date[2]))
					print(release_date)
					print(off_theatre_date)
					new_movie = Movie(title,director,discription,duration,url,release_date,off_theatre_date)
					db.session.add(new_movie)
					db.session.commit()
					return redirect("http://127.0.0.1:5000/admin")
			return render_template('addmovie.html', form=form,log=ans),200

@mod_movie.route('/movie/<movie_id>')
def load_screening(movie_id):
	print(movie_id)
	movie = Movie.query.filter(Movie.id == movie_id).first()
	if movie:
		if 'user_id' not in session:
			print(movie_id)
			session['k'] = "http://127.0.0.1:5000/movie/" + movie_id
			ans = {'log':"Login",'val':"Signup"}
		else:
			name = User.query.filter_by(id = session['user_id']).first()
			print(name)
			print(type(name))
			name = name.name	
			ans = {'log':"Logout",'val':name}
		return render_template('screening.html',movie=movie,log=ans)
	else:
		return render_template('404.html'),404
