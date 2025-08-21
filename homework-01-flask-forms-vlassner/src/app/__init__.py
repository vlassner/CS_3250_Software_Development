'''
CS3250 - Software Development Methods and Tools - Spring 2024
Instructor: Thyago Mota
Student:
Description: Homework 01 - Recipes Web App
'''

from flask import Flask

app = Flask('Recipes Web App')

# consider using an ENVIRONMENT VARIABLE to improve security
app.secret_key = 'you-will-never-guess'

from app import routes