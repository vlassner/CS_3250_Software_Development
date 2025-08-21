'''
CS3250 - Software Development Methods and Tools - Spring 2024
Instructor: Thyago Mota
Student:Victoria Lassner
Description: Homework 01 - Forms for the Recipes Web App
'''

from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField, DateField, SelectField, SubmitField, validators
from wtforms.validators import DataRequired

# TODOd #2: complete the recipe form with the missing fields (title, type, and tags)
class RecipeForm(FlaskForm):
    number = StringField('Recipe#', validators=[DataRequired()])
    title = StringField('Title', validators=[DataRequired()])
    type = SelectField('Type', choices = [( 'breakfast'), ('appetizer'), ('side dish'), ('main course'), ('dessert')], validators=[DataRequired()])
    tags = StringField('Tags')
    submit = SubmitField('Submit')
    