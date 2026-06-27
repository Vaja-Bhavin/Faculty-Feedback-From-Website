from flask import Flask,render_template,request,redirect,url_for,session,flash
from extensions import db

import os
from dotenv import load_dotenv
from routes.student import student
from routes.faculty import faculty
from routes.collage import collage
from datetime import timedelta

load_dotenv()
app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY")

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False


app.permanent_session_lifetime = timedelta(days=7)

db.init_app(app)


@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("home"))

app.register_blueprint(student)
app.register_blueprint(faculty)
app.register_blueprint(collage)


if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=True
    )
