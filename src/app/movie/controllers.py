from flask import Blueprint, request, session, jsonify, render_template
from app import db
from .models import Movie
from sqlalchemy import *
from datetime import *

mod_movie = Blueprint('movie', __name__, url_prefix='/api')


@mod_movie.route('/movies', methods=['GET'])
def display_movies():
    movies = Movie.query.filter(Movie.off_theatre_date >= date.today())
    movie_array = []

    for i in movies:
        movie_array.append(i.to_dict_movies())
    return jsonify(success=True, movies=movie_array),200

@mod_movie.route('/movie/add', methods=['POST'])
def add_movie():
	print("hdwdjw")
	title = request.form['title']
	print(title)
	director = request.form['director']
	discription = request.form['discription']
	duration = request.form['duration']
	url = request.form['url']
	release_date = request.form['release_date']
	off_theatre_date = request.form['off_theatre_date']
	print(release_date)
	release_date = release_date.split("-")
	release_date = date(int(release_date[0]),int(release_date[1]),int(release_date[2]))
	off_theatre_date = off_theatre_date.split("-")
	off_theatre_date = date(int(off_theatre_date[0]),int(off_theatre_date[1]),int(off_theatre_date[2]))
	print(release_date)
	print(off_theatre_date)
	new_movie = Movie(title,director,discription,duration,url,release_date,off_theatre_date)
	db.session.add(new_movie)
	db.session.commit()
	return jsonify(success=True),200

