'''
CS3250 - Software Development Methods and Tools - Fall 2023
Instructor: Thyago Mota
Description: Activity 10 - Time Tracking Tool
'''

from flask import Flask
import os, bcrypt
from datetime import datetime

app = Flask("Time Tracking Web App")
app.secret_key = os.environ['SECRET_KEY']

from app import routes