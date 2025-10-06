from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.db_connect import get_db

tasks = Blueprint('tasks', __name__)

@tasks.route('/', methods=['GET', 'POST'])
def show_tasks():
    db = get_db()
    cursor = db.cursor()

    # Handle POST request to add a new task
    if request.method == 'POST':
        task_name = request.form['task_name']
        project_id = request.form['project_id']
        description = request.form['description']
        due_date = request.form['due_date']
        priority = request.form['priority']
        status = request.form['status']

        # Insert the new task into the database
        cursor.execute('INSERT INTO tasks (task_name, project_id, description, due_date, priority, status) VALUES (%s, %s, %s, %s, %s, %s)',
                       (task_name, project_id, description, due_date, priority, status))
        db.commit()

        flash('New task added successfully!', 'success')
        return redirect(url_for('tasks.show_tasks'))

    # Handle GET request to display all tasks with project information
    cursor.execute('''
        SELECT t.task_id, t.task_name, t.description, t.due_date, t.priority, t.status,
               t.created_at, t.updated_at, t.project_id,
               p.project_name
        FROM tasks t
        JOIN projects p ON t.project_id = p.project_id
        ORDER BY t.due_date
    ''')
    all_tasks = cursor.fetchall()

    # Get all projects for the dropdown
    cursor.execute('SELECT project_id, project_name FROM projects ORDER BY project_name')
    all_projects = cursor.fetchall()

    return render_template('tasks.html', all_tasks=all_tasks, all_projects=all_projects)

@tasks.route('/update_task/<int:task_id>', methods=['POST'])
def update_task(task_id):
    db = get_db()
    cursor = db.cursor()

    # Update the task's details
    task_name = request.form['task_name']
    project_id = request.form['project_id']
    description = request.form['description']
    due_date = request.form['due_date']
    priority = request.form['priority']
    status = request.form['status']

    cursor.execute('UPDATE tasks SET task_name = %s, project_id = %s, description = %s, due_date = %s, priority = %s, status = %s WHERE task_id = %s',
                   (task_name, project_id, description, due_date, priority, status, task_id))
    db.commit()

    flash('Task updated successfully!', 'success')
    return redirect(url_for('tasks.show_tasks'))

@tasks.route('/delete_task/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    db = get_db()
    cursor = db.cursor()

    # Delete the task
    cursor.execute('DELETE FROM tasks WHERE task_id = %s', (task_id,))
    db.commit()

    flash('Task deleted successfully!', 'danger')
    return redirect(url_for('tasks.show_tasks'))
