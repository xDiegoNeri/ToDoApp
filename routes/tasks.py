from flask import Blueprint, render_template, redirect, url_for, abort
from flask_login import current_user, login_required
from werkzeug.utils import secure_filename
from forms import TaskForm
from models import Task, db
import os

tasks_blueprint = Blueprint('tasks', __name__)

@tasks_blueprint.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    form = TaskForm()
    if form.validate_on_submit():
        filename = None
        if form.image.data:
            filename = secure_filename(form.image.data.filename)
            form.image.data.save(os.path.join('static/uploads', filename))
        new_task = Task(
            title=form.title.data,
            description=form.description.data,
            priority=form.priority.data,
            owner=current_user,
            image=filename
        )
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('tasks.dashboard'))
    
    tasks = Task.query.filter_by(owner=current_user).order_by(Task.priority).all()
    return render_template('dashboard.html', form=form, tasks=tasks)

@tasks_blueprint.route('/edit/<int:task_id>', methods=['GET', 'POST'])
@login_required
def edit_task(task_id):
    task = Task.query.get_or_404(task_id)
    if task.owner != current_user:
        abort(403)
    
    form = TaskForm(obj=task)
    if form.validate_on_submit():
        task.title = form.title.data
        task.description = form.description.data
        task.priority = form.priority.data
        if form.image.data:
            filename = secure_filename(form.image.data.filename)
            form.image.data.save(os.path.join('static/uploads', filename))
            task.image = filename
        db.session.commit()
        return redirect(url_for('tasks.dashboard'))
    
    return render_template('edit_task.html', form=form, task=task)

@tasks_blueprint.route('/toggle_complete/<int:task_id>', methods=['POST'])
@login_required
def toggle_complete(task_id):
    task = Task.query.get(task_id)
    if task and task.owner == current_user:
        task.is_complete = not task.is_complete
        db.session.commit()
    return redirect(url_for('tasks.dashboard'))
