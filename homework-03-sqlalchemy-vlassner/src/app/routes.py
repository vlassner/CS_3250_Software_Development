'''
CS3250 - Software Development Methods and Tools - Spring 2024
Instructor: Thyago Mota
Student: Victoria Lassner
Description: Homework 03 - Routes for the SQLAlchemy Relationship Web App
'''

from app import app, db, load_user
from app.models import User, Recipe
from app.forms import SignUpForm, LoginForm, RecipeForm
from flask import render_template, redirect, url_for, request
from flask_login import login_required, login_user, logout_user, current_user
import bcrypt

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index(): 
    return render_template('index.html')

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

@app.route('/users/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
   
    if form.validate_on_submit():
        user = db.session.get(User,form.id.data)
        
        if bcrypt.checkpw(form.passwd.data.encode('utf-8'), user.passwd_hashed):
            login_user(user)
            recipes = current_user.recipes
            return render_template("recipes.html", recipes = recipes)
            # return redirect(url_for('recipes'))
        else:
            return redirect(url_for('errorpage'))
      

    return render_template('login.html', form=form)

    
@app.route('/users/signout', methods=['GET', 'POST'])
def signout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/recipes')
@login_required
def recipes(): 
    recipes = current_user.recipes
    return render_template("recipes.html", user=current_user, recipes=recipes)


# TO-DO #2: get the list of recipes from the logged-in user (current_user); then, create a new recipe with the information gathered from the form and append it to the list of recipes; commit to persist the information into the database
@app.route('/recipes/create', methods=['GET','POST'])
@login_required
def recipes_create():
    form = RecipeForm()

    if form.validate_on_submit(): 
        recipe = current_user.recipes
        recipe.append(
            Recipe(
                number = form.number.data,
                title = form.title.data,
                type = form.type.data,
                tags = form.tags.data
            )
        )
        
        current_user.recipes = recipe
        db.session.commit()
        return redirect(url_for('recipes'))
    else:
       return render_template('recipes_create.html', form=form)

# TO-DO #3: create an SQLAlchemy query to get a reference of the recipe to be deleted; then call delete (passing that reference) followed by commit
@app.route('/recipes/<number>/delete', methods=['GET','POST'])
@login_required
def recipes_delete(number):
    recipe = db.session.query(Recipe).filter_by(number=number).one()
    db.session.delete(recipe)
    db.session.commit()
    return redirect(url_for('recipes'))

    
