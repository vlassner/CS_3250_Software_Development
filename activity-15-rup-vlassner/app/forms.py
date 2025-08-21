'''
CS3250 - Software Development Methods and Tools - Fall 2023
Instructor: Thyago Mota
Team:
Description: Project 1 - Windoors Web App
'''

from flask_wtf import FlaskForm, Form
from wtforms import StringField, IntegerField, FieldList, FormField, SelectField, PasswordField, TextAreaField, DateField, SubmitField, validators
from wtforms.validators import DataRequired

class SignUpForm(FlaskForm):
    id = StringField('Id', validators=[DataRequired()])
    passwd = PasswordField('Password', validators=[DataRequired()])
    passwd_confirm = PasswordField('Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Confirm')

class SignInForm(FlaskForm):
    id = StringField('Id', validators=[DataRequired()])
    passwd = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Confirm')
