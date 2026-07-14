from flask import Blueprint,render_template,request,redirect,url_for,flash,session
from os import getenv
from werkzeug.security import generate_password_hash, check_password_hash
from models import College
from extensions import db
from email_utils import clg_register_info

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

@admin.route("/admin/addcollege",methods=["GET","POST"])
def addClg():

    if request.method == "POST":
        cc = request.form.get("cc")
        name = request.form.get("name")
        mail = request.form.get("mail")
        cn = request.form.get("cn")
        addr = request.form.get("addr")
        uni = request.form.get("uni")
        web = request.form.get("web")
        pw = request.form.get("pass")
        hashpw = generate_password_hash("pw")
        print(cc,name,mail,cn,addr,uni,web,pw,hashpw)
        
        c1 = College(college_code=cc,college_name=name,email=mail,contact_no=cn,address=addr,university=uni,website=web,password=hashpw)
        db.session.add(c1)
        db.session.commit()
        clg_register_info(mail)
        return redirect(url_for("admin.adminHome"))

    if "is_admin" in session:
        return render_template("admin/add-collage.html")
    return redirect(url_for("admin.adminLogin"))
