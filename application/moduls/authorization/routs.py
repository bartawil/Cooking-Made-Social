import flask
from flask import Blueprint, render_template, session, request, url_for
from application.Classes import get_preview_from_db, Users

authorization = Blueprint('authorization', __name__)


@authorization.route("/login", methods=['GET', 'POST'])
def login():
    return render_template("Login.html")


@authorization.route("/logout")
def logout():
    session['cookie'] = None
    return flask.redirect('login')


@authorization.route("/process_login", methods=['POST'])
def process_login():
    userName = request.form.get("username")
    userPassword = request.form.get("userpassword")

    if userName=="" or userPassword =="":
        return render_template("Login.html", user_error="All fields must have value")

    user = Users(userName, userPassword)
    result = user.check_user_password()

    if result is None:
        return render_template("Login.html", user_error="Error in given credentials")
    session['cookie'] = userName
    return flask.redirect(url_for('authorization.target', name=userName, password=userPassword))


@authorization.route("/register", methods=['GET'])
def reg():
    return render_template("Register.html")


@authorization.route("/process-registration", methods=['POST'])
def handle2():
    userName = request.form.get("regUserName").strip()
    pw = request.form.get("regUserPw").strip()
    cnf_pw = request.form.get("cnfRegUserPw").strip()

    if userName == "" or pw == "" or cnf_pw == "":
        return render_template("Register.html", user_error="All fields must have value")
    if len(userName) > 45:
        return render_template("Register.html", user_error="User name is too long")

    # # Check if user already exists in DB
    new_user = Users(userName, pw)
    result = new_user.check_if_user_exist()

    if result is not None:
        return render_template("Register.html", user_error="User already exists")

    # Check matching password
    if cnf_pw == pw:
        # Add user to DB
        new_user.insert_to_db()

        return flask.redirect(url_for('authorization.login', name=userName, password=pw))
    else:
        return render_template("Register.html", password_error="Passwords do not match")


@authorization.route("/target/<name>&<password>", methods=['GET', 'POST'])
def target(name, password):
    posts = get_preview_from_db()
    return render_template("home.html", posts=posts)