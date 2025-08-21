'''
CS3250 - Software Development Methods and Tools - Spring 2024
Instructor: Thyago Mota
Student: Victoria Lassner
Description: Homework 02 - Routes for the User Authentication Web App
'''

from app import app, db
from app.models import User
from app.forms import SignUpForm, LoginForm
from flask import render_template, redirect, url_for, request
from flask_login import login_required, login_user, logout_user
import bcrypt

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index(): 
    return render_template('index.html')

@app.route("/error")
def errorpage():
    return render_template('errorpage.html')

# TODO #1: implement the sign-up functionality:
# * if passwords match, generate a "salted" hashed password using bcrypt
# * instantiate a user object from form information
# * store the user information in the database (hint: use db.session)
# * redirect to index
@app.route('/users/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    new_user = User()

    if form.validate_on_submit():
        if form.passwd.data == form.passwd_confirm.data:
            new_user.id = form.id.data
            new_user.name = form.name.data
            new_user.psswd = form.passwd.data
            new_user.about = form.about.data
            new_user.passwd = form.passwd.data.encode('utf-8')
            new_user.passwd_hashed = bcrypt.hashpw(form.passwd.data.encode('utf-8'), bcrypt.gensalt())
            db.session.add(new_user)
            db.session.commit()
            return redirect(url_for('index'))

    return render_template('signup.html', form=form)
    
# TODO #2: implement the login functionality:
# * query the database for the user with given id 
# * if passwords match, complete the login procedure
@app.route('/users/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    user = User()
   
    
    if form.validate_on_submit():
        user = db.session.get(User,form.id.data)
        
        if bcrypt.checkpw(form.passwd.data.encode('utf-8'), user.passwd_hashed):
            login_user(user)
            return redirect(url_for('list_users'))
        else:
            return redirect(url_for('errorpage'))
      

    return render_template('login.html', form=form)

# TODO #3: implement the sign-out functionality
@app.route('/users/signout', methods=['GET', 'POST'])
def signout():
    logout_user()
   # db.session.delete()
   # db.session.commit()
    return redirect(url_for('index'))

@app.route('/users')
@login_required
def list_users(): 
    users = User.query.all()
    return render_template('users.html', users=users)