from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/")
def start():
    return redirect(url_for("home"))


@app.route("/home/")
def home():
    return render_template("index.html")


@app.route("/login/")
def login():
    return render_template("login.html")


if __name__ == "__main__":
    app.run(debug=True, port=80)
