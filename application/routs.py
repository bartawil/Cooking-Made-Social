import flask
from flask import render_template, request, url_for, flash, redirect, session

from application import app, workshop_cursor, workshop_db
from application.forms import CreateRecipeForm, FindRecipeForm


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template("Login.html")
    else:
        userName = request.form.get("username")
        userPassword = request.form.get("userpassword")

        # Check if user already exists in DB
        sql_q = "SELECT user_name FROM users WHERE user_name=%s and user_password=%s"
        param_q = (userName, userPassword)

        workshop_cursor.execute(sql_q, param_q)
        result = workshop_cursor.fetchone()

        if result is None:
            return "Error in login credentials"
        return f"{userName, userPassword} - You are now logged in"


@app.route("/login", methods=['GET', 'POST'])
def login():
    return render_template("Login.html")


@app.route("/logout")
def logout():
    session['cookie'] = None
    return flask.redirect('login')


@app.route("/process_login", methods=['POST'])
def process_login():
    userName = request.form.get("username")
    userPassword = request.form.get("userpassword")

    if userName=="" or userPassword =="":
        return render_template("Login.html", user_error="All fields must have value")

    # Check if user already exists in DB
    sql_q = "SELECT user_name FROM users WHERE user_name=%s and user_password=%s"
    param_q = (userName, userPassword)

    workshop_cursor.execute(sql_q, param_q)
    result = workshop_cursor.fetchone()

    if result is None:
        return render_template("Login.html", user_error="Error in given credentials")
    session['cookie'] = userName
    return flask.redirect(url_for('target', name=userName, password=userPassword))


@app.route("/register", methods=['GET'])
def reg():
    return render_template("Register.html")


@app.route("/process-registration", methods=['POST'])
def handle2():
    userName = request.form.get("regUserName").strip()
    pw = request.form.get("regUserPw").strip()
    cnf_pw = request.form.get("cnfRegUserPw").strip()

    if userName == "" or pw == "" or cnf_pw == "":
        return render_template("Register.html", user_error="All fields must have value")
    if len(userName) > 45:
        return render_template("Register.html", user_error="User name is too long")

    # Check if user already exists in DB
    sql_q = "SELECT user_name FROM users WHERE user_name=%s"
    param_q = (userName, )
    workshop_cursor.execute(sql_q, param_q)

    if workshop_cursor.fetchone() is not None:
        return render_template("Register.html", user_error="User already exists")

    # Check matching password
    if cnf_pw == pw:
        # Add user to DB
        workshop_cursor.execute("INSERT INTO users(user_password, user_name) VALUES(%s, %s)", (pw, userName))
        workshop_db.commit()

        return flask.redirect(url_for('login', name=userName, password=pw))
    else:
        return render_template("Register.html", password_error="Passwords do not match")


posts = [
    {
        'author': 'Corey Schafer',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'April 20, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 3',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 4',
        'content': 'Second post content',
        'date_posted': 'April 21, 2018'
    }
]


@app.route("/target/<name>&<password>", methods=['GET', 'POST'])
def target(name, password):
    return render_template("home.html", posts=posts)


@app.route("/home")
def home():
    if not session.get("cookie"):
        return flask.redirect('login')
    return render_template('home.html', posts=posts)


def upload_recipe(value):
    # create id for new post
    workshop_cursor.execute("SELECT MAX(post_id) FROM post")
    output = workshop_cursor.fetchall()
    post_id = (output[0])[0] + 1

    # values from form
    contributer = value["contributer"]
    name = value['name']
    descriptor = value['descriptor']
    n_steps = value['n_steps']
    steps = value['steps']
    n_ingredient = value['n_ingredient']
    minutes = value['minutes']
    # print(contributer, name, descriptor, steps, n_ingredient, minutes)

    # update post scheme
    q = "INSERT INTO post (recipe_name, post_id) VALUES (%s, %s)"
    workshop_cursor.execute(q, (name, post_id))

    # update recipe scheme
    q = "INSERT INTO recipe (name_id, recipe_id, minutes, contributer_id, n_steps, steps, " \
        "descriptor, n_ingredient, post_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    workshop_cursor.execute(q, (name, post_id, minutes, contributer, n_steps, steps, descriptor, n_ingredient, post_id))
    workshop_db.commit()


@app.route("/create_recipe", methods=['GET', 'POST'])
def create_recipe():
    if not session.get("cookie"):
        return flask.redirect('login')
    else:
        form = CreateRecipeForm()
        if form.validate_on_submit():
            flash(f'Recipe "{form.name.data}" Upload successfully!', 'success')
            upload_recipe(form.data)
            return redirect(url_for('home'))
        return render_template('create_recipe.html', title='Create Recipe', form=form)


@app.route("/recipe_catalog", methods=['GET', 'POST'])
def recipe_catalog():
    if not session.get("cookie"):
        return flask.redirect('login')
    else:
        form = FindRecipeForm()
        if form.validate_on_submit():
            # flash(f'Recipe "{form.name.data}" Upload successfully!', 'success')
            # upload_recipe(form.data)
            return redirect(url_for('home'))
        return render_template('recipe_catalog.html', title='Recipe Catalog', form=form)

