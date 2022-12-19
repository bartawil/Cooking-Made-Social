from flask import Flask, render_template, request

app = Flask(__name__)

recipes = [
    {
        'name': 'Pancakes',
        'ingredients': ['flour', 'eggs', 'milk', 'baking powder'],
        'instructions': '1. In a large mixing bowl, combine the flour, eggs, milk, and baking powder. Stir until well combined. 2. Heat a large nonstick pan over medium heat. Pour in enough batter to make a small pancake. Cook until bubbles form on the surface, then flip and cook until the pancake is golden brown on both sides. 3. Repeat with the remaining batter. Serve hot, with your favorite toppings.'
    },
    {
        'name': 'Spaghetti Bolognese',
        'ingredients': ['ground beef', 'spaghetti', 'tomato sauce', 'onion', 'garlic'],
        'instructions': '1. In a large pot, bring salted water to a boil. Add the spaghetti and cook according to the package instructions. 2. In a separate pan, cook the ground beef over medium heat until it is browned. Add the onion and garlic and cook until the onion is translucent. 3. Add the tomato sauce to the pan with the ground beef and bring to a simmer. 4. Drain the cooked spaghetti and add it to the pan with the sauce. Toss to combine. 5. Serve hot, garnished with grated Parmesan cheese.'
    }
]

@app.route('/')
def home():
    return render_template('home.html', recipes=recipes)

@app.route('/recipe/<int:index>')
def recipe(index):
    return render_template('recipe.html', recipe=recipes[index])

if __name__ == '__main__':
    app.run()
