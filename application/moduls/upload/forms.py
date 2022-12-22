from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, FloatField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class CreateRecipeForm(FlaskForm):
    name = StringField('Recipe Name', validators=[DataRequired(), Length(min=0, max=255)])
    descriptor = StringField('Description')
    steps = StringField('Steps', validators=[DataRequired(), Length(min=0, max=255)])
    n_steps = IntegerField('Number of steps')
    ingredients = StringField('ingredients', validators=[DataRequired(), Length(min=0, max=255)])
    n_ingredient = IntegerField('Number of ingredient')
    minutes = IntegerField('Duration time in minutes')
    calories = FloatField('Calories')
    total_fat = FloatField('Total Fat')
    sugar = FloatField('Sugar')
    sodium = FloatField('Sodium')
    protein = FloatField('Protein')
    saturated_fat = FloatField('Saturated Fat')
    carbohydrate = FloatField('carbohydrate')
    submit = SubmitField('Create')
