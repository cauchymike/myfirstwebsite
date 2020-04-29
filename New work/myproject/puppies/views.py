from flask import Blueprint, render_template, redirect, url_for
from myproject import db
from myproject.puppies.forms import AddForm, DelForm
from myproject.models import Puppy

students_blueprint=Blueprint('students', __name__,
                            template_folder='templates/puppies')


@students_blueprint.route('/add', methods=['GET', 'POST'])#NOTE we use blueprints for routing between their own view.py files
#and inorder for it to work, we must register them in our init.py file.
def add():
    form = AddForm()

    if form.validate_on_submit():
        name = form.name.data

        # Add new student to database
        new_pup = Puppy(name)
        db.session.add(new_pup)
        db.session.commit()

        return redirect(url_for('students.list'))

    return render_template('add.html',form=form)

@students_blueprint.route('/list')
def list():
    # Grab a list of puppies from database.
    students = Puppy.query.all()
    return render_template('list.html', students=students)

@students_blueprint.route('/delete', methods=['GET', 'POST'])
def delete():

    form = DelForm()

    if form.validate_on_submit():
        id = form.id.data
        pup = Puppy.query.get(id)
        db.session.delete(pup)
        db.session.commit()

        return redirect(url_for('students.list'))
    return render_template('delete.html',form=form)

