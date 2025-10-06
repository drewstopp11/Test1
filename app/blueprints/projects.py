from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.db_connect import get_db

projects = Blueprint('projects', __name__)

@projects.route('/', methods=['GET', 'POST'])
def show_projects():
    db = get_db()
    cursor = db.cursor()

    # Handle POST request to add a new project
    if request.method == 'POST':
        project_name = request.form['project_name']
        description = request.form['description']
        start_date = request.form['start_date']
        status = request.form['status']

        # Insert the new project into the database
        cursor.execute('INSERT INTO projects (project_name, description, start_date, status) VALUES (%s, %s, %s, %s)',
                       (project_name, description, start_date, status))
        db.commit()

        flash('New project added successfully!', 'success')
        return redirect(url_for('projects.show_projects'))

    # Handle GET request to display all projects
    cursor.execute('SELECT * FROM projects')
    all_projects = cursor.fetchall()
    return render_template('projects.html', all_projects=all_projects)

@projects.route('/update_project/<int:project_id>', methods=['POST'])
def update_project(project_id):
    db = get_db()
    cursor = db.cursor()

    # Update the project's details
    project_name = request.form['project_name']
    description = request.form['description']
    start_date = request.form['start_date']
    status = request.form['status']

    cursor.execute('UPDATE projects SET project_name = %s, description = %s, start_date = %s, status = %s WHERE project_id = %s',
                   (project_name, description, start_date, status, project_id))
    db.commit()

    flash('Project updated successfully!', 'success')
    return redirect(url_for('projects.show_projects'))

@projects.route('/delete_project/<int:project_id>', methods=['POST'])
def delete_project(project_id):
    db = get_db()
    cursor = db.cursor()

    # Delete the project (cascade will delete associated tasks)
    cursor.execute('DELETE FROM projects WHERE project_id = %s', (project_id,))
    db.commit()

    flash('Project deleted successfully!', 'danger')
    return redirect(url_for('projects.show_projects'))
