from flask import Flask, render_template, url_for, flash, redirect, request
from forms import RegistrationForm, LoginForm, CreateRecipeForm
import mysql.connector

app = Flask(__name__)

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
    }
]

# Create S.K. for anti csrf attack
app.config['SECRET_KEY'] = '2136cdc56a8ad364b251f9bb645d1e56'
#  Connect to mysql database
workshop_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='database_workshop'
)
# Gives access to mysql db
workshop_cursor = workshop_db.cursor()


def some_query():
    workshop_cursor.execute("select name_id, descriptor from recipe where post_id=38")
    output = workshop_cursor.fetchall()
    # print((output[0]))
    posts[0]['title'] = (output[0])[0]
    posts[0]['content'] = (output[0])[1]
    workshop_cursor.execute("select name_id, descriptor from recipe where post_id=39")
    output = workshop_cursor.fetchall()
    # print((output[0]))
    # cur.close()
    posts[1]['title'] = (output[0])[0]
    posts[1]['content'] = (output[0])[1]


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'barrtawil@gmail.com' and form.password.data == 'password':
            flash(f'You have been loggen in!', 'success')
            return redirect(url_for('home'))
        else:
            flash(f'Login Unsuccessful. Please check username and password!', 'danger')
    return render_template('login.html', title='Login', form=form)


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
    form = CreateRecipeForm()
    if form.validate_on_submit():
        flash(f'Recipe "{form.name.data}" Upload successfully!', 'success')
        upload_recipe(form.data)
        return redirect(url_for('home'))
    return render_template('create_recipe.html', title='Create Recipe', form=form)


if __name__ == '__main__':
    some_query()
    app.run(debug=True)
