from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField, SelectField, RadioField \
    , TextAreaField, SelectFieldBase, SearchField, FloatField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class FindRecipeForm(FlaskForm):
    name = StringField('Recipe Name', validators=[DataRequired(), Length(min=0, max=255)])
    calories = FloatField('Calories Max Value')
    fat = FloatField('Fat Max Value')
    protein = FloatField('Protein Max Value')
    sort_by = SelectField('Sort',
                          choices=[('name', 'Name'), ('time', 'Duration Time '), ('earliest', 'Earliest to Latest'),
                                   ('latest', 'Latest to Earliest')])

    user_name = StringField('User Name', validators=[DataRequired(), Length(min=0, max=255)])
    likes = IntegerField('Number of Likes')
    comments = IntegerField('Number of Comments')
    submit = SubmitField('Search')

