from app import app, db 
from flask import render_template, redirect, url_for, request
from app.models import Student
from app.forms import StudentsCreateForm

@app.route('/students')
def list_students():
    students = Student.query.all()
    return render_template("students.html", students = students)

@app.route('/students/create', methods = ['GET', 'POST'])
def create_student():
    form = StudentsCreateForm()
    if form.validate_on_submit():
        id = request.args.get('id')
        name = request.args.get('name')
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('list_students'))
    else:
        return render_template('students_create.html', form=form)
