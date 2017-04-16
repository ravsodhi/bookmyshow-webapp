from app import db

class Seat (db.Model):
    __tablename__ = "seat"
    id = db.Column('id', db.Integer, primary_key = True)
    row = db.Column('row', db.String)   #Row will be alphabetical A,B,C
    column = db.Column('column', db.Integer)
    cost = db.Column('cost',db.Integer)
    def __init__(self,row,column,cost):
        self.row = row
        self.column = column
        self.cost = cost

    def to_dict_seat(self):
    	return {
    	'id' : self.id , 
    	'row' : self.row ,
    	'column' : self.column,
        'cost' : self.cost 
    	}

    def __repr__(self):
        return "'Seat' { 'row': %r, 'column': %r , 'cost': %r}"%(self.row,self.column,self.cost)
