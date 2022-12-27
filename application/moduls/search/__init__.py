from application.Classes import Post, find_posts_by_name, find_post_by_user_name


def search_recipe(value):
    # search post by name
    name = value['name']
    user_name = value['user_name']

    calories = value['calories']
    if calories == float('inf'):
        calories = 1e100  # 1e100 - a very large number

    fat = value['fat']
    if fat == float('inf'):
        fat = 1e100  # 1e100 - a very large number

    protein = value['protein']
    if protein == float('inf'):
        protein = 1e100  # 1e100 - a very large number

    sort_by = value['sort_by']
    if sort_by == 'name':
        sort_by = 'name_id'
    elif sort_by == 'time':
        sort_by = 'minutes asc'
    elif sort_by == 'earliest':
        sort_by = 'recipe_id asc'
    elif sort_by == 'latest':
        sort_by = 'recipe_id desc'

    if user_name == '':
        posts_list = find_posts_by_name(name, calories, fat, protein, sort_by)
    else:
        posts_list = find_post_by_user_name(name, user_name, calories, fat, protein, sort_by)

    return posts_list
