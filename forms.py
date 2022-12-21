from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class CreateRecipeForm(FlaskForm):
    contributer = IntegerField('Author Id', validators=[DataRequired()])
    name = StringField('Recipe Name', validators=[DataRequired(), Length(min=0, max=255)])
    descriptor = StringField('Description')
    steps = StringField('Steps', validators=[DataRequired(), Length(min=0, max=255)])
    n_steps = IntegerField('Number of steps')
    n_ingredient = IntegerField('Number of ingredient')
    minutes = IntegerField('Duration time in minutes')
    submit = SubmitField('Create')


class FindRecipeForm(FlaskForm):
    contributer = IntegerField('Author Id', validators=[DataRequired()])
    name = StringField('Recipe Name', validators=[DataRequired(), Length(min=0, max=255)])
    descriptor = StringField('Description')
    steps = StringField('Steps', validators=[DataRequired(), Length(min=0, max=255)])
    n_steps = IntegerField('Number of steps')
    n_ingredient = IntegerField('Number of ingredient')
    minutes = IntegerField('Duration time in minutes')
    submit = SubmitField('Create')
