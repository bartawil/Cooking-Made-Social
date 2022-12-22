import flask
from flask import Blueprint, render_template, session, url_for, redirect, flash

from application.moduls.search import search_recipe
from application.moduls.search.forms import FindRecipeForm

search = Blueprint('search', __name__)


@search.route("/recipe_catalog", methods=['GET', 'POST'])
def recipe_catalog():
    if not session.get("cookie"):
        return flask.redirect('login')
    else:
        form = FindRecipeForm()
        if form.validate_on_submit():
            # return the last post id
            post_id = search_recipe(form.data)
            if len(post_id) != 0:
                flash(f'"{len(post_id)}" recipes came from search!', 'success')
            else:
                flash(f'Cannot find recipe that contains this string', 'danger')
        return render_template('recipe_catalog.html', title='Recipe Catalog', form=form)
