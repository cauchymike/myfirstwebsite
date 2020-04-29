#this is the models.py file
#we must set up db __ inside the init__.py file
from myproject import db
class Puppy(db.Model):

    __tablename__ = 'students'
    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.Text)
    owner = db.relationship('Owner',backref='student',uselist=False)

    def __init__(self,name):
        self.name = name

    def __repr__(self):
        if self.owner:
            return f"Student name is {self.name} and the Parent is {self.owner.name}"
        else:
            return f"Student name is {self.name} and has no Parent registered yet."

class Owner(db.Model):

    __tablename__ = 'parent'

    id = db.Column(db.Integer,primary_key= True)
    name = db.Column(db.Text)
    # We use students.id because __tablename__='students'
    student_id = db.Column(db.Integer,db.ForeignKey('students.id'))

    def __init__(self,name,student_id):
        self.name = name
        self.student_id = student_id

    def __repr__(self):
        return f"Parent Name: {self.name}"
