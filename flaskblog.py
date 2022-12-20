from flask import Flask, render_template, url_for
from flask_mysqldb import MySQL

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


@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)


@app.route("/about")
def about():
    return render_template('about.html', title='About')


def connect_to_db():
    db = MySQL()

    app.config['MYSQL_HOST'] = 'localhost'
    app.config['MYSQL_USER'] = 'root'
    app.config['MYSQL_PASSWORD'] = '1234'
    app.config['MYSQL_DB'] = 'database_workshop'

    return db


def some_query(data_base):
    with app.app_context():
        data_base = connect_to_db()
        data_base.init_app(app)
        cur = data_base.connect.cursor()
        cur.execute("select name_id, descriptor from recipe where post_id=38")
        output = cur.fetchall()
        print((output[0]))
        posts[0]['title'] = (output[0])[0]
        posts[0]['content'] = (output[0])[1]
        cur.execute("select name_id, descriptor from recipe where post_id=39")
        output = cur.fetchall()
        print((output[0]))
        cur.close()
        posts[1]['title'] = (output[0])[0]
        posts[1]['content'] = (output[0])[1]


if __name__ == '__main__':
    db = connect_to_db()
    some_query(db)

    app.run(debug=True)

