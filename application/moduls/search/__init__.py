from application.Classes import Post, find_posts_by_name


def search_recipe(value):
    # search post by name
    name = value['name']
    post_list = find_posts_by_name(name)
    return post_list
