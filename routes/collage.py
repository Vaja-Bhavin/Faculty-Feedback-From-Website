from flask import Blueprint,render_template

collage = Blueprint("collage",__name__)

@collage.route("/collage/register")
def clgRegister():
    return render_template("collage-register.html")