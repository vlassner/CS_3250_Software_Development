from app import db

class Student(db.Model):
    _tablename_='students'
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)