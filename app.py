from flask import Flask,render_template,request,redirect,url_for,session,flash
from werkzeug.security import generate_password_hash
from extensions import db
from models import Student,College

import os
from dotenv import load_dotenv
from routes.student import student
from routes.faculty import faculty
from routes.college import college
from routes.admin import admin
from email_utils import send_otp
from datetime import timedelta
import random

load_dotenv()
app = Flask(__name__)

app.secret_key = os.getenv("SECRET_KEY")

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DB_URL")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# app.config["SQLALCHEMY_DATABASE_URI"] = (
#     os.environ.get("DB_URL")
#     or "sqlite:///users.db"
# )
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


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

@app.route("/forgot-password", methods=["GET","POST"])
def forgot():
    show_otp = False
    if request.method == "POST":
        action = request.form.get("action")

        if action == "send-otp":
            role = request.form.get("role")
            mail = request.form.get("mail")

            if role == "student":
                user = Student.query.filter_by(gmail=mail).first()

            # elif role == "faculty":
            #     user = Faculty.query.filter_by(email=mail).first()

            elif role == "college":
                user = College.query.filter_by(email=mail).first()

            if user:
                otp = str(random.randint(000000,999999))
                session["otp"] = {
                    "role":role,
                    "mail":mail,
                    "otp":otp
                }
                print(otp)
                # send_otp(mail,otp)

                show_otp = True
                flash("OTP sent successfully.")
            else:
                flash("Email not found.")

        elif action == "verify-otp":
            userotp = request.form.get("otp")
            otpdata =  session.get("otp")
            if userotp == otpdata["otp"]:
                return render_template("reset-password.html",title="Reset Password",action="/reset-password")
            else:
                show_otp = True
                flash("OTP Incorrect!")
       
    return render_template("forgot-password.html",show_otp=show_otp)

@app.route("/reset-password",methods=["POST"])
def resetPassword():
    pw = request.form.get("pw")
    cpw = request.form.get("cpw")
    if pw == cpw:
        otpdata = session.get("otp")
        role = otpdata["role"]
        mail = otpdata["mail"]
        hashed = generate_password_hash(cpw)
        if role == "student":
            print(cpw)
            user = Student.query.filter_by(gmail=mail).first()

        # elif role == "faculty":
        #     user = Faculty.query.filter_by(email=email).first()

        elif role == "college":
            user = College.query.filter_by(email=mail).first()

        if user:
            print(hashed)
            user.password = hashed
            db.session.commit()
            session.pop("otp",None)
    else:
        flash("Password Didn't Match!")
        return render_template("reset-password.html",title="Reset Password",action="/reset-password")
    return redirect(url_for("/"))


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
