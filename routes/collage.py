from flask import Blueprint,render_template

collage = Blueprint("collage",__name__)

@collage.route("/collage/home")
def clgHome():
    return render_template("collage/collage-home.html")

@collage.route("/collage/register")
def clgRegister():
    return render_template("collage/collage-register.html")