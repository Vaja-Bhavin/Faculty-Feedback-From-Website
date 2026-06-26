from flask import Blueprint,app,render_template,request,session,redirect,flash,url_for
from models import Student
from extensions import db
from email_utils import send_email,send_pass,send_login_info
from random import randrange

student = Blueprint("student",__name__)

@student.route("/student/home")
def studentHome():
    return render_template("student.html")

@student.route("/student/givefeedback")
def givefeedback():
    return render_template("givefd.html")

@student.route("/student/register")
def studentRegister():
    return render_template("student-register.html")

@student.route("/student/register/submit",methods=["POST"])
def stdRegisterSubmit():
    en = request.form.get("en")
    name = request.form.get("name")
    gmail = request.form.get("gmail")
    sem = request.form.get("sem")
    div = request.form.get("div")
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

@student.route("/otp", methods=["GET", "POST"])
def otp():
    en = session.get("en")
    name = session.get("name")
    gmail = session.get("gmail")
    sem = session.get("sem")
    div = session.get("div")
    otp = session.get("otp")
    if request.method == "GET":
        
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
            password = str(randrange(11111111,99999999))
            s1 = Student(en=en,name=name,gmail=gmail,sem=sem,div=div,password=password)
            db.session.add(s1)
            db.session.commit()
            send_pass(gmail,password)

            return redirect(url_for("student.studentLogin"))
        else:
            print("OTP Incorrect")
            flash("Otp Incorrect")
            return redirect(url_for("otp"))
        
@student.route("/student/login")
def studentLogin():
    return render_template("student-login.html")

@student.route("/student/login/submit",methods=["POST"])
def stdLoginSubmit():
    en1 = int(request.form.get("en"))
    pass1 = request.form.get("pass")

    s1 = Student.query.filter_by(en=en1).first()
    if pass1 == s1.password:
        send_login_info(s1.gmail)
        flash("Login successful!")
        return redirect(url_for("student.studentHome"))
    else:
        flash("Enrollment Or Password Is Incorrect")
        print("Enrollment Or Password Is Incorrect")
        return redirect(url_for("student.studentLogin"))
