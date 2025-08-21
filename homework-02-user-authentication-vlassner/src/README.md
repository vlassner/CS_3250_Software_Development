[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/vRIGT7HH)
# Overview

In this homework assignment you are asked to incorporate authentication to the simple web app described below using screens and paths. 

![pic1.png](pics/pic1.png)

An attempt to open the "/users" page without being signed in should result in the error message below. 

![pic2.png](pics/pic2.png)

The app is organized like the following: 

![pic3.png](pics/pic3.png)

Most of the code required for this app is shared with you.  You are asked to finish key parts of this web app to get it working. 

# Setup 

You are required to install the following Python packages: 

```
flask==3.0.1
flask-wtf==1.2.1
flask-sqlalchemy==3.1.1
flask-login==0.6.3
bcrypt==4.1.2
```

There is a **requirements.txt** file that you can use to install all of the packages above using: 

```
pip3 install -r requirements.txt
```

You will also need to define the following environment variables (from **src**): 

```
export FLASK_APP=app
export SECRET_KEY='The quick brown fox jumps over the lazy dog!'
```

Note that the app's secret key (used to sign cookies) is defined as an environment variable for extra security. 

# Flask-Login 

One of the requirements present in virtually all software is user authentication. [Flask-Login](https://flask-login.readthedocs.io/en/latest/) is a package that simplifies authenticating web app users, associating them to sessions. A session is where web apps maintain state information associated with users. 

Flask-Login comes with a login manager class. The snippet of code below shows how to configure the login manager for your web app. 

```
# login manager
from flask_login import LoginManager
login_manager = LoginManager()
login_manager.init_app(app)
```

In this assignment, **Flask-Login** will be used in conjunction with **SQLAlchemy**.  The following **User** model will be used: 

```
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    id = db.Column(db.String, primary_key=True)
    name = db.Column(db.String)
    about = db.Column(db.String)
    passwd_salt = db.Column(db.LargeBinary)
    passwd_hashed = db.Column(db.LargeBinary)
```

As it can be seen from the definition above, a **User** is defined by an id, a name, an about, a password salt, and a hashed password.  When storing user credentials in a database (like SQLite), it is recommended to hash the passwords, avoiding storing passwords in clear text. A hashing algorithm, like SHA, MD5, or BCrypt for example, turn plaintext into an unintelligible series of numbers and letters. In the event of a security breach, any compromised passwords are just a nonsense sequence that has nothing to do with the actuall password, making their use considerably more difficult. As an extra security, it is also recommended to "salt" the passwords before the actual hashing computation. A salt is a random sequence that is added to the password to make it even more difficult reversing the hashed password (in case the user database is compromised).

Flask-Login requires the definition of a "user_loader" callback function, which is used to load a user object from the datastore (in our example, an SQLite db). Below is a typical implementation for the "user_loader" callback. 

```
# user_loader callback
@login_manager.user_loader
def load_user(id):
    return db.session.query(User).filter(User.id==id).one()
```

# TO-DOs

## TO-DO #1 - User's Sign Up 

The sign-up functionality allows users to create their credentials. Use the given **SignUpForm** class, together with **signup.html**, to read the information provided by the user. If the provided passwords match, a "salted" hashed password should be generated using **bcrypt**. Learn how to do that [here](https://pypi.org/project/bcrypt/).

The user information should then be stored in the database. That can be done by instantiating a **User** object and persisting it into the database. [Here](https://docs.sqlalchemy.org/en/20/orm/session_basics.html) is SQLAlchemy documentation to help. After the user is saved, redirect to the "index" page. 

## TO-DO #2 User's Login

Use the given **LoginForm** class, together with **login.html**, to read the user id and password. If the provided password matches the one stored in the database, authenticate the user (hint: use Flask-Login's **login_user** function) and redirect to the "/users" page. 

## TO-DO #3 User Sign Out

If the users click on the sign-out button, you should remove the user information from the current session (hint: use Flask-Login's **logout_user**) and then redirect to the "/" page. 

# Submission 

Once you are done completing all to-do's, submit all code changed using "final submission" as the commit message. 

# Rubric 

This homework is worth 5 points distributed like the following: 

+2 TO-DO #1 

+2 TO-DO #2 

+1 TO-DO #3

+1 BONUS (redirect to error page when passwords do not match)