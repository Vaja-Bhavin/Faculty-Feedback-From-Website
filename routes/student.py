from flask import Blueprint,app,render_template,request,session,redirect,flash,url_for
from models import Student
from extensions import db
from email_utils import send_email,send_pass,send_login_info
from random import randrange

student = Blueprint("student",__name__)

@student.route("/student/home")
def studentHome():

    if "student_en" not in session:
        return redirect(url_for("student.studentLogin"))

    s1 = Student.query.get(session["student_en"])
    return render_template("student.html", s1=s1)


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
    otptemp = randrange(1000,9999)

    session["registration"] = {
    "en": en,
    "name": name,
    "gmail": gmail,
    "sem": sem,
    "div": div,
    "otp":otptemp,
    "alert":""
}
    # session["en"] = en
    # session["name"] = name
    # session["gmail"] = gmail
    # session["sem"] = sem
    # session["div"] = div
    # session["otp"] = otptemp
    # session["alert"] = ""
    send_email(gmail,otptemp)
    return redirect(url_for("otp"))

@student.route("/otp", methods=["GET", "POST"])
def otp():
    data = session.get("registration")
    # en = session.get("en")
    # name = session.get("name")
    # gmail = session.get("gmail")
    # sem = session.get("sem")
    # div = session.get("div")
    # otp = session.get("otp")

    en=data["en"],
    name=data["name"],
    gmail=data["gmail"],
    sem=data["sem"],
    div=data["div"],
    otp = data["otp"]
    if request.method == "GET":
        
        # print("En:",en)
        # print("Name:",name)
        # print("Gmail:",gmail)
        # print("Sem:",sem)
        # print("Div:",div)
        print("OTP:",otp)
        return render_template("verify-otp.html")
    if request.method == "POST":
        userOtp = request.form.get("otp")
        userOtp = int(userOtp)
        if otp == userOtp:
            print("OTP Correct!")
            password = str(randrange(11111111,99999999))
            s1 = Student(en=en,name=name,gmail=gmail,sem=sem,div=div,password=password)
            db.session.add(s1)
            db.session.commit()
            session.pop("registration", None)
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
    if s1 and pass1 == s1.password:
        session["student_en"] = s1.en
        send_login_info(s1.gmail)
        flash("Login successful!")
        return redirect(url_for("student.studentHome"))
    else:
        flash("Enrollment Or Password Is Incorrect")
        print("Enrollment Or Password Is Incorrect")
        return redirect(url_for("student.studentLogin"))
