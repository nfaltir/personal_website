from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    return "Hello World"


@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")


@app.route("/resume")
def resume():
    return render_template("resume.html")


@app.route("/bio")
def bio():
    return render_template("bio.html")


# turn off if debug mode if deploying online
if __name__ == "__main__":
    app.run(debug=True)

