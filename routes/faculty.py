from flask import Blueprint,render_template

faculty = Blueprint("faculty",__name__)


@faculty.route("/faculty/home")
def facultyHome():
    return render_template("faculty.html")
