from flask import session

from application import workshop_db, workshop_cursor


class Recipe:
    def __init__(self, name: str, recipe_id: int, minutes: int, contributer_id: int, n_steps: int, steps: str,
                 description: str, n_ingredients: int, post_id: int):
        self._name = name
        self._recipe_id = recipe_id
        self._minutes = minutes
        self._contributer_id = contributer_id
        self._n_steps = n_steps
        self._steps = steps
        self._description = description
        self._n_ingredients = n_ingredients
        self._post_id = post_id

    def insert_to_db(self):
        q = "INSERT INTO recipe (name_id, recipe_id, minutes, contributer_id, n_steps, steps, " \
            "descriptor, n_ingredient, post_id) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        workshop_cursor.execute(q, (
            self._name, self._post_id, self._minutes,
            self._contributer_id, self._n_steps, self._steps,
            self._description, self._n_ingredients, self._post_id))
        workshop_db.commit()


def generate_id():
    workshop_cursor.execute("SELECT MAX(post_id) FROM post")
    output = workshop_cursor.fetchall()
    return (output[0])[0] + 1


def find_posts_by_name(name):
    # Returns 4 posts that contain the string sorted from newest to oldest
    q = "SELECT name_id, descriptor FROM recipe WHERE name_id LIKE (%s) ORDER BY recipe_id DESC"
    str = "%" + name + "%"
    workshop_cursor.execute(q, (str,))
    post_list = workshop_cursor.fetchall()
    return post_list


def find_post_by_user_name(name, user_name):
    q = "SELECT r.name_id, r.descriptor " \
        "FROM recipe r " \
        "INNER JOIN users u " \
        "ON r.contributer_id = u.user_id " \
        "WHERE u.user_name " \
        "LIKE (%s) " \
        "AND r.name_id " \
        "LIKE (%s) ORDER BY r.recipe_id DESC"

    str_name = "%" + name + "%"
    str_user_name = "%" + user_name + "%"
    workshop_cursor.execute(q, (str_user_name, str_name,))
    post_list = workshop_cursor.fetchall()
    return post_list


class Post:
    def __init__(self, recipe_name: str, post_id: int):
        self._recipe_name = recipe_name
        self._post_id = post_id

    def insert_to_db(self):
        q = "INSERT INTO post (recipe_name, post_id) VALUES (%s, %s)"
        workshop_cursor.execute(q, (self._recipe_name, self._post_id))
        workshop_db.commit()


def get_preview_from_db():
    q = "SELECT recipe.name_id, recipe.descriptor FROM recipe ORDER BY recipe_id DESC limit 4"
    workshop_cursor.execute(q)
    output = workshop_cursor.fetchall()
    return output


class Nutrition:
    def __init__(self, recipe_id: int, calories: float, total_fat: float, sugar: float, sodium: float, protein: float,
                 saturated_fat: float, carbohydrates: float):
        self._recipe_id = recipe_id
        self._calories = calories
        self._total_fat = total_fat
        self._sugar = sugar
        self._sodium = sodium
        self._protein = protein
        self._saturated_fat = saturated_fat
        self._carbohydrates = carbohydrates

    def insert_to_db(self):
        q = "INSERT INTO nutrition (recipe_id, calories, total_fat, sugar, sodium, " \
            "protein, saturated_fat, carbohydrates) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        workshop_cursor.execute(q, (self._recipe_id, self._calories, self._total_fat, self._sugar,
                                    self._sodium, self._protein, self._saturated_fat, self._carbohydrates))
        workshop_db.commit()


class Ingredients:
    def __init__(self, recipe_id: int, n_ingredient: int, ingredient_list: str):
        self._recipe_id = recipe_id
        self._ingredient_list = ingredient_list
        self.n_ingredient = n_ingredient

    def insert_to_db(self):
        parsed_list = self._ingredient_list.split(",")
        for i in parsed_list:
            q = "INSERT INTO ingredients (recipe_id, ingredient_name) VALUES (%s, %s)"
            workshop_cursor.execute(q, (self._recipe_id, i))
        workshop_db.commit()


def get_current_user_id():
    q = "SELECT user_id FROM users where user_name = (%s)"
    workshop_cursor.execute(q, (session['cookie'],))
    return workshop_cursor.fetchone()[0]


class Users:
    def __init__(self, user_name: str, user_password: str):
        self._user_name = user_name
        self._user_password = user_password

    def insert_to_db(self):
        workshop_cursor.execute("INSERT INTO users(user_password, user_name) VALUES(%s, %s)",
                                (self._user_password, self._user_name))
        workshop_db.commit()

    def check_user_password(self):
        # Check if user already exists in DB
        sql_q = "SELECT user_name FROM users WHERE user_name=%s and user_password=%s"
        param_q = (self._user_name, self._user_password)

        workshop_cursor.execute(sql_q, param_q)
        result = workshop_cursor.fetchone()
        return result

    def check_if_user_exist(self):
        # Check if user already exists in DB
        sql_q = "SELECT user_name FROM users WHERE user_name=%s"
        param_q = (self._user_name,)
        workshop_cursor.execute(sql_q, param_q)
        return workshop_cursor.fetchone()


class Likes:
    def __init__(self, like_id: int, post_id: int, user_id: int):
        self._like_id = like_id
        self._post_id = post_id
        self._user_id = user_id


class Comments:
    def __init__(self, comment_id: int, post_id: int, content: str, user_id: int):
        self._comment_id = comment_id
        self._post_id = post_id
        self._content = content
        self._user_id = user_id