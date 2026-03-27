from flask import Flask,render_template,request,redirect,url_for,session
from flask_sqlalchemy import SQLAlchemy
from random import randrange
from email_utils import send_email
app = Flask(__name__)

app.secret_key = "secret123"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Student(db.Model):
    en = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    gmail = db.Column(db.String(50))
    sem = db.Column(db.Integer)
    div = db.Column(db.String(1))

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/student/home")
def studentHome():
    return render_template("student.html")

@app.route("/student/givefeedback")
def givefeedback():
    return render_template("givefd.html")

@app.route("/faculty/home")
def facultyHome():
    return render_template("faculty.html")

@app.route("/student/register")
def studentRegister():
    return render_template("student-register.html")

@app.route("/student/register/submit",methods=["POST"])
def stdRegisterSubmit():
    en = request.form.get("en")
    name = request.form.get("name")
    gmail = request.form.get("gmail")
    sem = request.form.get("sem")
    div = request.form.get("div")
    # s1 = Student(en=en,name=name,gmail=gmail,sem=sem,div=div)
    # db.session.add(s1)
    # db.session.commit()
    # print("En:",en)
    # print("Name:",name)
    # print("Gmail:",gmail)
    # print("Sem:",sem)
    # print("Div:",div)
    session["en"] = en
    session["name"] = name
    session["gmail"] = gmail
    session["sem"] = sem
    session["div"] = div
    otptemp = randrange(1000,9999)
    session["otp"] = otptemp
    session["alert"] = ""
    send_email(gmail,otptemp)
    return redirect(url_for("otp"))

@app.route("/otp", methods=["GET", "POST"])
def otp():
    if request.method == "GET":
        en = session.get("en")
        name = session.get("name")
        gmail = session.get("gmail")
        sem = session.get("sem")
        div = session.get("div")
        otp = session.get("otp")
        
        # print("En:",en)
        # print("Name:",name)
        # print("Gmail:",gmail)
        # print("Sem:",sem)
        # print("Div:",div)
        print("OTP:",otp)
        return render_template("verify-otp.html")
    if request.method == "POST":
        otp = session.get("otp")
        userOtp = request.form.get("otp")
        userOtp = int(userOtp)
        if otp == userOtp:
            print("OTP Correct!")
            return redirect(url_for("studentHome"))
        else:
            print("OTP Incorrect")
            msg = "OTP Incorrect!"
            session["alert"] = msg
            return redirect(url_for("otp"))

if __name__ == "__main__":
    with app.app_context():
        db.create_all()

app.run(debug=True)