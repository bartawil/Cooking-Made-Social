from application.Classes import Post, find_posts_by_name, find_post_by_user_name


def search_recipe(value):
    # search post by name
    name = value['name']
    user_name = value['user_name']
    likes = value['likes']
    comments = value['comments']
    calories = value['calories']
    fat = value['fat']
    protein = value['protein']

    if user_name == '':
        posts_list = find_posts_by_name(name)
    else:
        posts_list = find_post_by_user_name(name, user_name)

    return posts_list
