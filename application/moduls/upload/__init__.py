from flask import session

from application.Classes import *


def upload_recipe(value):
    contributer = get_current_user_id()

    # parse form data
    name = value['name']
    descriptor = value['descriptor']
    steps = value['steps']
    n_steps = value['n_steps']
    ingredients = value['ingredients']
    n_ingredient = value['n_ingredient']
    minutes = value['minutes']
    calories = value['calories']
    total_fat = value['total_fat']
    sugar = value['sugar']
    sodium = value['sodium']
    protein = value['protein']
    saturated_fat = value['saturated_fat']
    carbohydrate = value['carbohydrate']

    post_id = generate_id()

    # update posts table
    new_post = Post(name, post_id)
    new_post.insert_to_db()

    # update recipe table
    new_recipe = Recipe(name, post_id, minutes, contributer, n_steps, steps, descriptor, n_ingredient, post_id)
    new_recipe.insert_to_db()

    # update nutrition table
    new_nutrition = Nutrition(post_id, calories, total_fat, sugar, sodium, protein, saturated_fat, carbohydrate)
    new_nutrition.insert_to_db()

    # update ingredients table
    new_ingredients = Ingredients(post_id, n_ingredient, ingredients)
    new_ingredients.insert_to_db()
