from flask import Blueprint, request, session, jsonify, render_template
from app import db
from sqlalchemy import *

class Movie (db.Model):
 #Model
    __tablename__ = "movie"
    id = db.Column('id', db.Integer, primary_key = True)
    title = db.Column('title', db.String)
    director = db.Column('director', db.String)
    description = db.Column('description', db.String)
    duration = db.Column('duration', db.Integer)
    url = db.Column('url',db.String)
    def __init__(self,title,director,description,duration,url):
        self.title = title
        self.director = director
        self.description = description
        self.duration = duration
        self.url = url

    def __repr__(self):
        return "Movie {'name': %r, 'director' : %r, 'description' :%r ,'duration' : %r,'url' :%r }"%(self.title,self.director,self.description,self.duration,self.url)

    def to_dict_movies(self):
        return {
        'title': self.title, 
        'director' : self.director,
        'description' :self.description, 
        'id' : self.id,
        'url' : self.url
        }

