from flask import Blueprint,render_template,request,redirect,url_for,flash,session
from os import getenv

admin = Blueprint("admin",__name__)

@admin.route("/admin")
def adminHome():
    if "is_admin" in session:
        return render_template("admin/admin.html")
    return redirect(url_for("home"))

@admin.route("/admin/login",methods=["GET","POST"])
def adminLogin():
    if request.method == "GET":
        if "student_en" in session:
            return redirect(url_for("student.studentHome"))
        return render_template("admin/admin-login.html")

    if request.method == "POST":
        password = request.form.get("pass")
        if password == getenv("ADMIN_PASSWORD"):
            print("Login Successfull!")
            session.clear()
            session["is_admin"] = True
            return redirect(url_for("admin.adminHome"))
        flash("Password Incorrect!")
        return redirect(url_for("admin.adminLogin"))

@admin.route("/admin/addcollage")
def addClg():
    return render_template("admin/add-collage.html")