from flask import Flask

app = Flask("My Web App")
app.config['SECRET_KEY'] = 'you-will-never-guess'

# db initialization
from flask_sqlalchemy import flask_sqlalchemy
db = SQLAlchemy()
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///app.db"
db.init_app(app)

# db from models
from app import models
with app.app_context():
    db.create_all()

from app import routes