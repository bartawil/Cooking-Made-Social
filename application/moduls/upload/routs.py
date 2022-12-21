import flask
from flask import Blueprint, render_template, session, url_for, flash, redirect

from application import workshop_cursor, workshop_db
from application.moduls.upload.forms import CreateRecipeForm

upload = Blueprint('upload', __name__)


def upload_recipe(value):
    # create id for new posts
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

    # update posts scheme
    q = "INSERT INTO post (recipe_name, post_id) VALUES (%s, %s)"
    workshop_cursor.execute(q, (name, post_id))

    # update recipe scheme
    q = "INSERT INTO recipe (name_id, recipe_id, minutes, contributer_id, n_steps, steps, " \
        "descriptor, n_ingredient, post_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
    workshop_cursor.execute(q, (name, post_id, minutes, contributer, n_steps, steps, descriptor, n_ingredient, post_id))
    workshop_db.commit()


@upload.route("/create_recipe", methods=['GET', 'POST'])
def create_recipe():
    if not session.get("cookie"):
        return flask.redirect('login')
    else:
        form = CreateRecipeForm()
        if form.validate_on_submit():
            flash(f'Recipe "{form.name.data}" Upload successfully!', 'success')
            upload_recipe(form.data)
            return redirect(url_for('main.home'))
        return render_template('create_recipe.html', title='Create Recipe', form=form)
