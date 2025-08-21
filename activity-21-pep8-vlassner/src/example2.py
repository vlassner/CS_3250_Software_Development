'''
CS3250 - Software Development Methods and Tools - Fall 2023
Instructor: Thyago Mota
Student:
Description: Homework 02 - Routes for the User Authentication Web App
'''

from app import app, db, load_user
from app.models import User
from app.forms import SignUpForm, SignInForm
from flask import render_template, redirect, url_for, request
from flask_login import login_required, login_user, logout_user
import bcrypt

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index(): 
    return render_template('index.html')

# TODO #1: implement the sign-in functionality
@app.route('/users/signin', methods=['GET', 'POST'])
def users_signin():
    return '<p>TODO #1</p>'

# TODO #2: implement the sign-up functionality
@app.route('/users/signup', methods=['GET', 'POST'])
def users_signup():
    return '<p>TODO #2</p>'
    
# TODO #3: implement the sign-out functionality
@app.route('/users/signout', methods=['GET', 'POST'])
def users_signout():
    return '<p>TODO #3</p>'

@app.route('/users')
@login_required
def list_users(): 
    users = User.query.all()
    return render_template('users.html', users=users)