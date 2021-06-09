from datetime import timezone
from enum import unique
from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func # get current DateTime
from datetime import datetime

class Note(db.Model):    
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


# defining a schema
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True) # unique email
    first_name = db.Column(db.String(150))
    password = db.Column(db.String(150))
    notes = db.relationship('Note') # referencing the name of the class