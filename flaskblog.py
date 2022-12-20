from flask import Flask, render_template, url_for, flash, redirect, request
from flask_mysqldb import MySQL
from forms import RegistrationForm, LoginForm, CreateRecipeForm

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

# def connect_to_db():
#     db = MySQL()
#
#     app.config['SECRET_KEY'] = '2136cdc56a8ad364b251f9bb645d1e56'
#     app.config['MYSQL_HOST'] = 'localhost'
#     app.config['MYSQL_USER'] = 'root'
#     app.config['MYSQL_PASSWORD'] = '1234'
#     app.config['MYSQL_DB'] = 'database_workshop'
#
#     return db
data_base = MySQL()

app.config['SECRET_KEY'] = '2136cdc56a8ad364b251f9bb645d1e56'
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '1234'
app.config['MYSQL_DB'] = 'database_workshop'
with app.app_context():
    data_base.init_app(app)
    cur = data_base.connect.cursor()


def some_query():
    # with app.app_context():
    #     data_base.init_app(app)
    #     cur = data_base.connect.cursor()
    cur.execute("select name_id, descriptor from recipe where post_id=38")
    output = cur.fetchall()
    print((output[0]))
    posts[0]['title'] = (output[0])[0]
    posts[0]['content'] = (output[0])[1]
    cur.execute("select name_id, descriptor from recipe where post_id=39")
    output = cur.fetchall()
    print((output[0]))
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


def check(value):
    # data_base = connect_to_db()
    # with app.app_context():
    #     data_base = connect_to_db()
    #     data_base.init_app(app)
    #     cur = data_base.connect.cursor()
    q = "INSERT INTO post (recipe_name) VALUES (%s)"
    cur.execute(q, (value,))

    cur.execute(q)
    cur.close()


@app.route("/create_recipe", methods=['GET', 'POST'])
def create_recipe():
    form = CreateRecipeForm()
    if form.validate_on_submit():
        flash(f'Recipe "{form.name.data}" Upload successfully!', 'success')
        check(form.name.data)
        return redirect(url_for('home'))
    else:
        flash(f'Please try again', 'danger')
    return render_template('create_recipe.html', title='Create', form=form)


if __name__ == '__main__':
    # db = connect_to_db()
    some_query()

    app.run(debug=True)
