from flask import session, request

from application import workshop_db, workshop_cursor


def get_ingredients(recipe_id):
    query = "SELECT * FROM ingredients WHERE recipe_id=%s"
    workshop_cursor.execute(query, (recipe_id,))
    ingredients = workshop_cursor.fetchall()
    return ingredients


def get_nutrition(recipe_id):
    query = "SELECT * FROM nutrition WHERE recipe_id=%s"
    workshop_cursor.execute(query, (recipe_id,))
    nutrition = workshop_cursor.fetchall()
    return nutrition


def get_user_id():
    query = "SELECT user_id FROM users WHERE user_name=%s"
    user_name = session.get("cookie")
    workshop_cursor.execute(query, (user_name,))
    user_id = workshop_cursor.fetchall()
    return user_id


def get_username(user_id):
    query = "SELECT user_name FROM users WHERE users.user_id=%s"
    workshop_cursor.execute(query, (user_id,))
    username = workshop_cursor.fetchall()
    return username[0]


def get_comments(user_id):
    query = "SELECT * FROM comments WHERE comments.user_id=%s"
    workshop_cursor.execute(query, (user_id[0][0],))
    commnt = workshop_cursor.fetchall()
    return commnt


def add_comment(comment_id, recipe, user_id):
    comment_content = request.form.get("comment")
    if comment_content is None:
        return
    query = 'INSERT INTO comments (comment_id, post_id, content, user_id) VALUES (%s, %s, %s, %s)'
    workshop_cursor.execute(query, (comment_id, recipe[0][8], comment_content, user_id[0][0]))
    workshop_db.commit()