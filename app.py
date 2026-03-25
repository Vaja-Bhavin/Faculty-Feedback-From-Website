from flask import Flask,render_template
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/student")
def student():
    return render_template("student.html")
app.run(debug=True)