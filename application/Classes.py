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


def newRecipes(recipes: list):
    recipeLst = list()
    for recipe in recipes:
        name, recipe_id, minutes, contributer_id, n_steps, steps, description, n_ingredients, post_id = recipe
        recipeLst.append(Recipe(name, recipe_id, minutes, contributer_id, n_steps, steps, description, n_ingredients,
                                post_id))
    return recipeLst


class Post:
    def __init__(self, recipe_name: str, post_id: int):
        self._recipe_name = recipe_name
        self._post_id = post_id


def newPosts(posts: list):
    postLst = list()
    for post in posts:
        recipe_name, post_id = post
        postLst.append(Post(recipe_name, post_id))
    return postLst


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


def newNutrition(nutritions: list):
    nutritionLst = list()
    for nutrition in nutritions:
        recipe_id, calories, total_fat, sugar, sodium, protein, saturated_fat, carbohydrates = nutrition
        nutritionLst.append(Nutrition(recipe_id, calories, total_fat, sugar, sodium, protein, saturated_fat, carbohydrates))
    return nutritionLst


class Ingredients:
    def __init__(self, recipe_id: int, ingredient_name: str):
        self._recipe_id = recipe_id
        self._ingredient_name = ingredient_name


def newIngredients(ingredients: list):
    ingredientLst = list()
    for ingredient in ingredients:
        recipe_id, ingredient_name = ingredient
        ingredientLst.append(Post(recipe_id, ingredient_name))
    return ingredientLst


class Users:
    def __init__(self, user_id: int, user_password: str, user_name: str):
        self._user_id = user_id
        self._user_password = user_password
        self._user_name = user_name


def newUsers(users: list):
    userLst = list()
    for user in users:
        user_id, user_password, user_name = user
        userLst.append(Users(user_id, user_password, user_name))
    return userLst


class Likes:
    def __init__(self, like_id: int, post_id: int, user_id: int):
        self._like_id = like_id
        self._post_id = post_id
        self._user_id = user_id


def newLikes(likes: list):
    likesLst = list()
    for like in likes:
        like_id, post_id, user_id = like
        likesLst.append(Likes(like_id, post_id, user_id))
    return likesLst


class Comments:
    def __init__(self, comment_id: int, post_id: int, content: str, user_id: int):
        self._comment_id = comment_id
        self._post_id = post_id
        self._content = content
        self._user_id = user_id


def newComments(comments: list):
    commentsLst = list()
    for comment in comments:
        comment_id, post_id, content, user_id = comment
        commentsLst.append(Comments(comment_id, post_id, content, user_id))
    return commentsLst

# class SearchHandler:
#     def __init__(self, cursor, db):
#         self.cursos = cursor
#         self.db = db
#     def execute_command(self):
#         q = 'SELECT * FROM authorization'
#         self.cursos.execute(q)
#         res = self.cursos.fetchall()
#         for row in res:
#             print(row)