'''
CS3250 - Software Development Methods and Tools - Fall 2023
Instructor: Thyago Mota
Description: Activity XX - Routes for the User Authentication Web App
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

@app.route('/users/signin', methods=['GET', 'POST'])
def users_signin():
    form = SignInForm()
    if form.validate_on_submit(): 
        try: 
            user = load_user(form.id.data)
            if bcrypt.checkpw(
                form.passwd.data.encode('utf-8'), 
                user.passwd
            ): 
                login_user(user)
                return redirect(url_for('list_users'))
            else:
                return '<p>Wrong password!</p>'
        except Exception as ex: 
                return f'<p>Could not find a user with the given id: {ex}</p>'
    else:
        return render_template('users_signin.html', form=form)

@app.route('/users/signup', methods=['GET', 'POST'])
def users_signup():
    form = SignUpForm()
    if form.validate_on_submit(): 
        if form.passwd.data != form.passwd_confirm.data: 
            return '<p>Passwords do not match!</p>'
        try: 
            passwd = bcrypt.hashpw(
                form.passwd.data.encode('utf-8'), 
                bcrypt.gensalt()
            )
            user = User(
                id = form.id.data,
                name = form.name.data, 
                about = form.about.data, 
                passwd = passwd
            )
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('index'))
        except Exception as ex: 
            return f'<p>Problem signing up the user: {ex}</p>' 
    else:
        return render_template('users_signup.html', form=form)
    
@app.route('/users/signout', methods=['GET', 'POST'])
def users_signout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/users')
@login_required
def list_users(): 
    users = User.query.all()
    return render_template('users.html', users=users)