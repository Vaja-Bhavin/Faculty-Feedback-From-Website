from flask import Blueprint,render_template,request,redirect,url_for,flash
from os import getenv

admin = Blueprint("admin",__name__)

@admin.route("/admin")
def adminHome():
    return render_template("admin.html")

@admin.route("/admin/login",methods=["GET","POST"])
def adminLogin():
    if request.method == "GET":
        return render_template("admin-login.html")

    if request.method == "POST":
        password = request.form.get("pass")
        if password == getenv("ADMIN_PASSWORD"):
            print("Login Successfull!")
            return redirect(url_for("admin.adminHome"))
        flash("Password Incorrect!")
        return redirect(url_for("admin.adminLogin"))