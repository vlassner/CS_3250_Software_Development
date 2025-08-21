'''
CS3250 - Software Development Methods and Tools - Fall 2023
Instructor: Thyago Mota
Description: Activity 10 - Time Tracking Tool
'''

from app import app
from flask import render_template, redirect, url_for
from app.forms import SignInForm, SignUpForm
from datetime import datetime

@app.route('/')
@app.route('/index')
@app.route('/index.html')
def index(): 
    return render_template('index.html')

@app.route('/users/signin', methods=['GET', 'POST'])
def users_signin():
    form = SignInForm()
    if form.validate_on_submit(): 
        return redirect(url_for('activities'))
    else:
        return render_template('users_signin.html', form=form)

@app.route('/users/signup', methods=['GET', 'POST'])
def users_signup():
    form = SignUpForm()
    if form.validate_on_submit(): 
        return redirect(url_for('index'))
    else:
        return render_template('users_signup.html', form=form)  
      
@app.route('/users/signout', methods=['GET', 'POST'])
def users_signout():
    return redirect(url_for('index'))

@app.route('/activities')
def activities():
    activities = [
        { 
            'id': 123,
            'project_code': 'PRJ001', 
            'name': 'database design',
            'start': '09/21/23',
            'end': '09/27/23',
            'status': 'ongoing', 
            'days': 5, 
            'hours': 15 
        }, 
                { 
            'id': 234,
            'project_code': 'PRJ001', 
            'name': 'system architecture design',
            'start': '09/19/23',
            'end': '09/25/23',
            'status': 'late', 
            'days': 7, 
            'hours': 11 
        },
        { 
            'id': 345,
            'project_code': 'PRJ002', 
            'name': 'screen design',
            'start': '09/19/22',
            'end': '09/21/23',
            'status': 'paused', 
            'days': 4, 
            'hours': 20 
        },
                { 
            'id': 345,
            'project_code': 'PRJ003', 
            'name': 'database design',
            'start': '09/19/21',
            'end': '09/30/23',
            'status': 'concluded', 
            'days': 10, 
            'hours': 40 
        }
    ]
    user = {
        'activities': activities
    }
    return render_template('activities.html', user=user)

@app.route('/activities/<id>/tasks')
def tasks(id):
    activity = { 
            'id': 123,
            'project_code': 'PRJ001', 
            'name': 'database design',
            'start': '09/21/23',
            'end': '09/27/23',
            'status': 'ongoing', 
            'days': 5, 
            'hours': 15, 
            'tasks': [
                { 
                    'seq': 1, 
                    'name': 'draw an UML class diagram', 
                    'start': '09/21/23', 
                    'end': '09/21/23', 
                    'hours': 5
                },
                                { 
                    'seq': 2, 
                    'name': 'write an SQL script', 
                    'start': '09/22/23', 
                    'end': '09/22/23', 
                    'hours': 4
                },
                                { 
                    'seq': 3, 
                    'name': 'populate the tables', 
                    'start': '09/23/23', 
                    'end': '09/23/23', 
                    'hours': 2
                },
                                { 
                    'seq': 4, 
                    'name': 'grant privileges', 
                    'start': '09/24/23', 
                    'end': '09/24/23', 
                    'hours': 2
                },
                                { 
                    'seq': 5, 
                    'name': 'backup the database', 
                    'start': '09/25/23', 
                    'end': '09/25/23', 
                    'hours': 2
                }
            ]
        }
    return render_template('tasks.html', activity=activity)

@app.route('/activities/<id>/delete')
def delete_activity(id):
    return 'TODO'

@app.route('/activities/<id>/tasks/create')
def task_create(id):
    return 'TODO'