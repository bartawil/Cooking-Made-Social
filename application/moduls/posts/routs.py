import flask
from flask import Blueprint, session, request, render_template

from application.Classes import RecipePost

posts = Blueprint('posts', __name__)
r = RecipePost()


@posts.route("/recipe/<post_id>", methods=['GET', 'POST'])
def recipe(post_id):
    if not session.get("cookie"):
        return flask.redirect('login')
    else:
        nutrition_cat = ['Calories', 'Total Fat', 'Sugar', 'Sodium', 'Protein', 'Saturated Fat', 'Carbohydrates']
        recipe = r.get_recipe(post_id)

        usr_id = r.get_user_id()
        commnt = r.get_comments(post_id)
        ingredients = r.get_ingredients(recipe[0][1])
        nutrition = r.get_nutrition(recipe[0][1])
        likes = r.get_likes(post_id)

        comment_id = 0
        if len(commnt) != 0:
            comment_id = commnt[-1][0] + 1

        r.add_comment(comment_id, recipe, usr_id)
        commnt = r.get_comments(post_id)

        usernames = []
        for com in commnt:
            usernames.append(r.get_username(com[3]))

        return render_template('Recipe.html', recipe_name=recipe[0][0], recipe_description=recipe[0][6],
                               minuets=recipe[0][2], n_ingredients=recipe[0][7], n_steps=recipe[0][4],
                               recipe_steps=recipe[0][5], comments=commnt, nutrition=nutrition, ingredients=ingredients,
                               nutrition_cat=nutrition_cat, enumerate=enumerate, usernames=usernames, post_id=post_id,
                               likes=likes)


@posts.route('/add_like/<post_id>')
def add_like(post_id):
    r.add_like(post_id)
    return flask.redirect(f'/recipe/{post_id}')
