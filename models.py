from extensions import db

class Student(db.Model):
    en = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    gmail = db.Column(db.String(50))
    sem = db.Column(db.Integer)
    div = db.Column(db.String(1))
    password = db.Column(db.String(8))
