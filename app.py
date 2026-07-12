from flask import Flask,render_template,request,redirect,url_for,session,flash
from extensions import db
from models import Student

import os
from dotenv import load_dotenv
from routes.student import student
from routes.faculty import faculty
from routes.college import college
from routes.admin import admin
from datetime import timedelta

load_dotenv()
app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY")

# app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DB_URL")
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

app.config["SQLALCHEMY_DATABASE_URI"] = (
    os.environ.get("DB_URL")
    or "sqlite:///users.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


app.permanent_session_lifetime = timedelta(days=7)

db.init_app(app)

@app.after_request
def add_header(response):
    response.headers["Cache-Control"] = "no-store, no-cache, must-revalidate, max-age=0"
    response.headers["Pragma"] = "no-cache"
    response.headers["Expires"] = "0"
    return response

@app.route("/")
def home():

    if "student_en" not in session:
        return render_template("home.html")
        
    s1 = Student.query.get(session["student_en"])
    return redirect(url_for("student.studentHome"))
    # return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))

@app.route("/forgot-password")
def forget():
    return render_template("forgot-password.html")

app.register_blueprint(student)
app.register_blueprint(faculty)
app.register_blueprint(college)
app.register_blueprint(admin)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    # app.run(
    #     host="0.0.0.0",
    #     port=int(os.environ.get("PORT", 5000)),
    #     debug=True
    # )

    app.run(debug=True)
