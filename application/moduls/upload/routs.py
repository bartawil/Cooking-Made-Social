import flask
from flask import Blueprint, render_template, session, url_for, flash, redirect

from application.moduls.upload import upload_recipe
from application.moduls.upload.forms import *

upload = Blueprint('upload', __name__)


@upload.route("/create_recipe", methods=['GET', 'POST'])
def create_recipe():
    if not session.get("cookie"):
        return flask.redirect('login')
    else:
        form = CreateRecipeForm()
        if form.validate_on_submit():
            flash(f'Recipe "{form.name.data}" ', 'success')
            upload_recipe(form.data)
            return redirect(url_for('main.home'))
        return render_template('create_recipe.html', title='Create Recipe', form=form)


