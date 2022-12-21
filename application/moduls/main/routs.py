import flask
from flask import Blueprint, render_template, request, session

from application import workshop_cursor
from application.moduls.posts import posts

main = Blueprint('main', __name__)


@main.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("Login.html")
    else:
        userName = request.form.get("username")
        userPassword = request.form.get("userpassword")

        # Check if user already exists in DB
        sql_q = "SELECT user_name FROM authorization WHERE user_name=%s and user_password=%s"
        param_q = (userName, userPassword)

        workshop_cursor.execute(sql_q, param_q)
        result = workshop_cursor.fetchone()

        if result is None:
            return "Error in login credentials"
        return f"{userName, userPassword} - You are now logged in"


@main.route("/home")
def home():
    if not session.get("cookie"):
        return flask.redirect('login')
    return render_template('home.html', posts=posts)
