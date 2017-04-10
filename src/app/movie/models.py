from flask import Blueprint, request, session, jsonify, render_template
from app import db
from sqlalchemy import *
from datetime import datetime
from datetime import date
from datetime import time

class Movie (db.Model):
 #Model
    __tablename__ = "movie"
    id = db.Column('id', db.Integer, primary_key = True)
    title = db.Column('title', db.String)
    director = db.Column('director', db.String)
    description = db.Column('description', db.String)
    duration = db.Column('duration', db.Integer)
    url = db.Column('url',db.String)
    release_date= db.Column('release_date',db.Date)
    off_theatre_date= db.Column('off_theatre_date',db.Date)
    def __init__(self,title,director,description,duration,url,release_date,off_theatre_date):
        self.title = title
        self.director = director
        self.description = description
        self.duration = duration
        self.url = url
        self.release_date = release_date
        self.off_theatre_date = off_theatre_date

    def __repr__(self):
        return "'Movie' {'name': %r, 'director' : %r, 'description' :%r ,'duration' : %r,'url' :%r , 'release_date' : %r , 'off_theatre_date' : %r}" %(self.title,self.director,self.description,self.duration,self.url,self.release_date,self.off_theatre_date)

    def to_dict_movies(self):
        return {
        'title': self.title, 
        'director' : self.director,
        'description' :self.description, 
        'id' : self.id,
        'url' : self.url,
        'release_date' : self.release_date,
        'off_theatre_date' : self.off_theatre_date
        }

