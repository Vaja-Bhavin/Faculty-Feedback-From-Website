from flask import Flask,render_template,request,redirect,url_for,session,flash
from extensions import db

import os
from dotenv import load_dotenv
from routes.student import student
from routes.faculty import faculty

load_dotenv()
app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")


app.register_blueprint(student)
app.register_blueprint(faculty)

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

app.run(debug=True)