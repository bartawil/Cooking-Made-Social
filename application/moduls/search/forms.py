from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, SelectField, RadioField \
    , TextAreaField, SelectFieldBase, SearchField, FloatField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class FindRecipeForm(FlaskForm):
    name = StringField('Recipe Name', validators=[Length(min=0, max=255)])

    user_name = StringField('User Name', validators=[Length(min=0, max=255)])

    likes = IntegerField('Number of Likes', default=0)
    comments = IntegerField('Number of Comments', default=0)

    calories = FloatField('Calories Max Value', default=float('inf'))
    fat = FloatField('Fat Max Value', default=float('inf'))
    protein = FloatField('Protein Max Value', default=float('inf'))

    sort_by = SelectField('Sort By',
                          choices=[('name', 'Sort by Name'), ('time', 'Duration Time '),
                                   ('earliest', 'Earliest to Latest'), ('latest', 'Latest to Earliest')])

    submit = SubmitField('Search')

