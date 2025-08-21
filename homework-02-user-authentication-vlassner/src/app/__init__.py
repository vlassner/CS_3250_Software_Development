'''
CS3250 - Software Development Methods and Tools - Spring 2024
Instructor: Thyago Mota
Student: Victoria Lassner
Description: Homework 02 - User Authentication Web App
'''

from flask import Flask
import os

app = Flask("Authentication Web App")
# app.secret_key = os.environ['SECRET_KEY']
app.config['SECRET_KEY'] = 'The quick brown fox jumps over the lazy dog!'

# db initialization
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
db.init_app(app)

from app import models
with app.app_context(): 
    db.create_all()

# login manager
from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)

from app.models import User

# user_loader callback
@login_manager.user_loader
def load_user(id):
    try: 
        return db.session.query(User).filter(User.id==id).one()
    except: 
        return None

from app import routes