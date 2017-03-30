from flask import *
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import * #for and_ && or_
from flask_cors import CORS
#app=CORS(__name__)
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///project.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



class Movie (db.Model):
 #Model   
    __tablename__ = "movie"
    id = db.Column('id', db.Integer, primary_key = True)
    title = db.Column('title', db.String)
    #director = db.Column('director', db.String)
    #description = db.Column(Column('description', db.Text))
    #duration_min = db.Column('duration_min', db.Integer)
    #rating = db.Column('rating', db.Integer)
    def __init__(self,title):
        self.title = title
        #self.director
        #self.description
        #self.duration_min
        #self.rating

    def __repr__(self):
        return "Movie { name: %r }"%(self.title)
        '''return "Movie {
        name: %r
        director : %r
        description :%r
        duration_min : %r
        rating : %r
        }"%(self.title,self.director,self.description,self.duration_min,self.rating)
        '''

class User (db.Model):
 #Model   
    __tablename__ = "user"
    id = db.Column('id', db.Integer, primary_key = True)
    
    username = db.Column('username', db.String)
    #password = db.Column('password', db.String)
    def __init__(self,username):
        self.username = username
        #self.password = generate_password_hash(password)
    def __repr__(self):
        return "User { username: %r }"%(self.username)
        '''return "User { 
        username: %r
        password: %r}"%(self.username,self.password)
        '''

class Seat (db.Model):
    __tablename__ = "seat"
    id = db.Column('id', db.Integer, primary_key = True)
    row = db.Column('row', db.String)   #Row will be alphabetical A,B,C
    column = db.Column('column', db.Integer)
        
    def __init__(self,row,column):
        self.row = row
        self.column = column
            
    def __repr__(self):
        return "Seat { row: %r column: %r}"%(self.row,self.column)

class Auditorium (db.Model):
    __tablename__ = "auditorium"
    id = db.Column('id', db.Integer, primary_key = True)
    name = db.Column('name', db.String)
    
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return "Auditorium { name: %r }"%(self.name)

class Time (db.Model):
    __tablename__ = "time"
    id = db.Column('id', db.Integer, primary_key = True)
    start_time = db.Column('start_time', db.Integer)
    
    def __init__(self,start_time):
        self.start_time = start_time
    def __repr__(self):
        return "Time { start_time: %r }"%(self.start_time)

class Date(db.Model):
    __tablename__="date"
    id = db.Column('id',db.Integer,primary_key = True)
    show_date = db.Column('show_date',db.String)
    
    def __init__(self,show_date):
        self.show_date = show_date
    def __repr__(self):
        return "Date { show_date: %r }"%(self.show_date)

class Screening (db.Model):
    __tablename__ = "screening"
    id = db.Column('id', db.Integer, primary_key = True)
    movie_id = db.Column('movie_id', db.Integer, db.ForeignKey('movie.id'))
    auditorium_id = db.Column('auditorium_id', db.Integer, db.ForeignKey('auditorium.id'))
    screening_start_time = db.Column('screening_start_time', db.Integer,db.ForeignKey('time.id'))
    screening_date = db.Column('screening_date',db.Integer,db.ForeignKey('date.id'))
    
    def __init__(self,movie_id,auditorium_id,screening_start_time,screening_date):
        self.movie_id = movie_id
        self.auditorium_id = auditorium_id
        self.screening_start_time = screening_start_time
        self.screening_date = screening_date
    
    def __repr__(self):
        return "Screening { movie_id: %r auditorium_id: %r start_time:%r show_date: %r}"%(self.movie_id,self.auditorium_id,self.screening_start_time,self.screening_date)

class Booking (db.Model):
    __tablename__ = "booking"
    id = db.Column('id',db.Integer,primary_key = True)
    user_id = db.Column('user_id',db.Integer,db.ForeignKey('user.id'))
    screening_id = db.Column('screening_id',db.Integer,db.ForeignKey('screening.id'))
    seat_id = db.Column('seat_id',db.Integer,db.ForeignKey('seat.id'))

    def __init__(self,user_id,screening_id,seat_id):
        self.user_id = user_id
        self.screening_id = screening_id
        self.seat_id = seat_id

    def __repr__(self):
        return "Booking { user_id: %r screening_id: %r seat_id: %r}"%(self.user_id,self.screening_id,self.seat_id)


db.create_all()
movie1= Movie("DABANG")
movie2 = Movie("SHOLAY")
user1= User("kunal")
user2 = User("anish")
aud1 = Auditorium("Big")
aud2 = Auditorium("Medium")
aud3 = Auditorium("Small")
time1 = Time("9:30")
time2 = Time("12:30")
time3 = Time("3:30")
time4 = Time("6:30")
time5 = Time("9:30")
date1 = Date("Today")
date2 = Date("Yesterday")
date3 = Date("Tommorow")

db.session.add(date1)
db.session.add(date2)
db.session.add(date3)
db.session.commit()

Screening1 = Screening(1,1,1,1)
Screening2 = Screening(1,1,2,2)
Screening3 = Screening(1,1,3,3)
Screening4 = Screening(1,1,4,4)
Screening5 = Screening(1,1,5,5)

Screening6 = Screening(1,2,1,2)
Screening7 = Screening(1,2,2,2)
Screening8 = Screening(1,2,3,2)
Screening9 = Screening(1,2,4,2)
Screening10 = Screening(1,2,5,2)

Screening11 = Screening(2,1,1,3)
Screening12 = Screening(2,1,2,3)
Screening13  = Screening(2,1,3,3)
Screening14 = Screening(2,1,4,3)
Screening15 = Screening(2,1,5,3)
Screening16 = Screening(2,2,1,3)
Screening17 = Screening(2,2,2,3)
Screening18 = Screening(2,2,3,3)
Screening19 = Screening(2,2,4,3)
Screening20 = Screening(2,2,5,3)
db.session.add(movie1)
db.session.add(movie2)
db.session.add(user2)
db.session.add(user1)
db.session.add(aud1)
db.session.add(aud2)
db.session.add(aud3)
db.session.add(Screening1)
db.session.add(Screening2)
db.session.add(Screening3)
db.session.add(Screening4)
db.session.add(Screening5)
db.session.add(Screening6)
db.session.add(Screening7)
db.session.add(Screening8)
db.session.add(Screening9)
db.session.add(Screening10)
db.session.add(Screening11)
db.session.add(Screening12)
db.session.add(Screening13)
db.session.add(Screening14)
db.session.add(Screening15)
db.session.add(Screening16)
db.session.add(Screening17)
db.session.add(Screening18)
db.session.add(Screening19)
db.session.add(Screening20)

db.session.commit()
k =Movie.query.filter_by(title="SHOLAY").first()
#print(k.id)
l =Screening.query.filter_by(movie_id=k.id).all()
print(l)
k=[]
#l.filter(auditorium_id=1).all()
for j in l:
    if j.screening_start_time == 1:
        k.append(j)
print(k)

#for j in l:
 #   print(j.auditorium_id)

#print(Movie.query.filter_by(title="SHOLAY").all())
#print(Movie.query.filter_by(title="SHOLAY").all())

#db.session.delete(movie1)
db.session.commit()





