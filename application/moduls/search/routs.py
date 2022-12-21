import flask
from flask import Blueprint, render_template, session, url_for, redirect

from application.moduls.search.forms import FindRecipeForm

search = Blueprint('search', __name__)


@search.route("/recipe_catalog", methods=['GET', 'POST'])
def recipe_catalog():
    if not session.get("cookie"):
        return flask.redirect('login')
    else:
        form = FindRecipeForm()
        if form.validate_on_submit():
            # flash(f'Recipe "{form.name.data}" Upload successfully!', 'success')
            # upload_recipe(form.data)
            return redirect(url_for('home.home'))
        return render_template('recipe_catalog.html', title='Recipe Catalog', form=form)

