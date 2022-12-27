from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, SelectField, RadioField \
    , TextAreaField, SelectFieldBase, SearchField, FloatField, SelectMultipleField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class CreateRecipeForm(FlaskForm):
    name = StringField('Recipe Name', validators=[DataRequired(), Length(min=0, max=255)])
    descriptor = TextAreaField('Description',  validators=[Length(min=0, max=255)])
    steps = TextAreaField('Steps', validators=[DataRequired(), Length(min=0, max=255)])
    n_steps = IntegerField('Steps number', default=0)
    ingredients = StringField('Ingredients', validators=[DataRequired(), Length(min=0, max=255)])
    n_ingredient = IntegerField('Ingredients number', default=0)
    minutes = IntegerField('Duration time in minutes', default=0)
    calories = FloatField('Calories', default=0)
    total_fat = FloatField('Total Fat', default=0)
    sugar = FloatField('Sugar', default=0)
    sodium = FloatField('Sodium', default=0)
    protein = FloatField('Protein', default=0)
    saturated_fat = FloatField('Sat Fat', default=0)
    carbohydrate = FloatField('Carbohydrate', default=0)
    submit = SubmitField('Create')
