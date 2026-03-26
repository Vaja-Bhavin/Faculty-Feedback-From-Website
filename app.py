from flask import Flask,render_template,request
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/student/home")
def studentHome():
    return render_template("student.html")

@app.route("/student/givefeedback")
def givefeedback():
    return render_template("givefd.html")

@app.route("/faculty/home")
def facultyHome():
    return render_template("faculty.html")

@app.route("/submit",methods=["POST"])
def submit():
    en = request.form.get("en")
    gmail = request.form.get("gmail")
    print("En:",en)
    print("Gmail:",gmail)
    return render_template("student.html")

@app.route("/student/register")
def studentRegister():
    return render_template("student-register.html")

app.run(debug=True)