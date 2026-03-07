from flask import Flask, render_template, request, redirect, url_for
import math

app = Flask(__name__)

USERNAME = "Vbrijesh"
PASSWORD = "123Bri"

@app.route("/", methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if username == USERNAME and password == PASSWORD:
            return redirect(url_for("welcome", user=username))
        else:
            return "Invalid Username or Password"

    return render_template("login.html")


@app.route("/welcome/<user>", methods=["GET","POST"])
def welcome(user):

    result = None

    if request.method == "POST":
        number = float(request.form["number"])
        result = math.sqrt(number)

    return render_template("welcome.html", username=user, result=result)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)