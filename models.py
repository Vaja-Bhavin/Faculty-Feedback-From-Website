from extensions import db

class Student(db.Model):
    en = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    gmail = db.Column(db.String(50))
    sem = db.Column(db.Integer)
    div = db.Column(db.String(1))
    password = db.Column(db.String(8))

class Collage(db.Model):
    id = db.Column(db.Integer, primary_key=True)

    college_code = db.Column(db.String(20), unique=True, nullable=False)
    college_name = db.Column(db.String(150), nullable=False)

    email = db.Column(db.String(120), unique=True, nullable=False)
    contact_no = db.Column(db.String(15), nullable=False)

    address = db.Column(db.Text, nullable=False)

    university = db.Column(db.String(150))
    website = db.Column(db.String(150))

    password = db.Column(db.String(255), nullable=True)

    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())
