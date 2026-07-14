from flask import Blueprint,render_template,request,session,redirect,url_for,flash
from werkzeug.security import check_password_hash

from models import College
from extensions import db


college = Blueprint("college",__name__)

@college.route("/college/home")
def clgHome():
    if "college_code" not in session:
        return redirect(url_for("college.clgLogin"))
    return render_template("college/college-home.html")

@college.route("/college/register")
def clgRegister():
    return render_template("college/college-register.html")

@college.route("/college/login",methods=["GET","POST"])
def clgLogin():
    if request.method == "POST":
        cc = int(request.form.get("cc"))
        pass1 = request.form.get("pass")
        c1 = College.query.filter_by(college_code=cc).first()
        if cc and check_password_hash(c1.password,pass1):
            session.clear()
            session["college_code"] = cc
            return redirect(url_for("college.clgHome"))
        else:
            flash("College Code Or Password Is Inccorect!")

    return render_template("college/college-login.html")