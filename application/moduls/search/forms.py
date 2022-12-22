from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo


class FindRecipeForm(FlaskForm):
    name = StringField('Recipe Name', validators=[DataRequired(), Length(min=0, max=255)])
    submit = SubmitField('Create')
