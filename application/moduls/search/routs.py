import flask
from flask import Blueprint, render_template, session, flash

from application.moduls.search import search_recipe
from application.moduls.search.forms import LikesAndCommentsSearchForm
from application.moduls.search.forms import FindRecipeForm
from application.Classes import ComplexQuery

search = Blueprint('search', __name__)


@search.route("/recipe_catalog", methods=['GET', 'POST'])
def recipe_catalog():
    if not session.get("cookie"):
        return flask.redirect('login')
    else:
        form = FindRecipeForm()
        if form.validate_on_submit():
            # return the last post id
            posts = search_recipe(form.data)
            flash(f'{len(posts)} recipes came from search!', 'success')
            return render_template('home.html', posts=posts)
        return render_template('recipe_catalog.html', title='Recipe Catalog', form=form)


@search.route("/like_and_comments_search", methods=['POST'])
def like_and_comments_search():
    if not session.get("cookie"):
        return flask.redirect('login')
    else:
        form = LikesAndCommentsSearchForm()
        if form.validate_on_submit():
            complex_query = ComplexQuery(form.likes.data, form.comments.data, form.sort_by.data)
            posts = complex_query.execute_complex_query()
            flash(f'{len(posts)} recipes came from search!', 'success')
            return render_template('home.html', posts=posts)
    return render_template('recipe_catalog.html', title='Recipe Catalog', form=form)
