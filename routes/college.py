from flask import Blueprint,render_template

college = Blueprint("college",__name__)

@college.route("/college/home")
def clgHome():
    return render_template("college/college-home.html")

@college.route("/college/register")
def clgRegister():
    return render_template("college/college-register.html")

@college.route("/college/login")
def clgLogin():
    return render_template("college/college-login.html")