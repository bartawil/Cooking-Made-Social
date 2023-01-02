import flask
from flask import Blueprint, session, request, render_template

from application import workshop_cursor, workshop_db
from application.moduls.posts.forms import get_user_id, get_comments, get_ingredients, get_nutrition, add_comment, \
    get_username

posts = Blueprint('posts', __name__)


@posts.route("/recipe", methods=['GET', 'POST'])
#TODO: bring ingredients of recipe
def recipe():
    if not session.get("cookie"):
        return flask.redirect('login')
    else:
        nutrition_cat = ['Calories', 'Total Fat', 'Sugar', 'Sodium', 'Protein', 'Saturated Fat', 'Carbohydrates']
        query = "SELECT * FROM recipe WHERE recipe.name_id='low fat berry blue frozen dessert'"
        workshop_cursor.execute(query)
        recipe = workshop_cursor.fetchall()

        usr_id = get_user_id()
        commnt = get_comments(usr_id)
        ingredients = get_ingredients(recipe[0][1])
        nutrition = get_nutrition(recipe[0][1])

        comment_id = 0
        if len(commnt) != 0:
            comment_id = commnt[-1][0] + 1

        add_comment(comment_id, recipe, usr_id)
        commnt = get_comments(usr_id)

        usernames = []
        for com in commnt:
            usernames.append(get_username(com[3]))

        return render_template('Recipe.html', recipe_name=recipe[0][0], recipe_description=recipe[0][6],
                               minuets=recipe[0][2], n_ingredients=recipe[0][7], n_steps=recipe[0][4],
                               recipe_steps=recipe[0][5], comments=commnt, nutrition=nutrition, ingredients=ingredients,
                               nutrition_cat=nutrition_cat, enumerate=enumerate, usernames=usernames)