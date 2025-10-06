from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.db_connect import get_db

authors = Blueprint('authors', __name__)

@authors.route('/', methods=['GET', 'POST'])
def show_authors():
    db = get_db()
    cursor = db.cursor()

    # Handle POST request to add a new author
    if request.method == 'POST':
        first_name = request.form['first_name']
        last_name = request.form['last_name']
        birth_year = request.form['birth_year']
        nationality = request.form['nationality']

        # Insert the new author into the database
        cursor.execute('INSERT INTO authors (first_name, last_name, birth_year, nationality) VALUES (%s, %s, %s, %s)',
                       (first_name, last_name, birth_year, nationality))
        db.commit()

        flash('New author added successfully!', 'success')
        return redirect(url_for('authors.show_authors'))

    # Handle GET request to display all authors
    cursor.execute('SELECT * FROM authors')
    all_authors = cursor.fetchall()
    return render_template('authors.html', all_authors=all_authors)

@authors.route('/update_author/<int:author_id>', methods=['POST'])
def update_author(author_id):
    db = get_db()
    cursor = db.cursor()

    # Update the author's details
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    birth_year = request.form['birth_year']
    nationality = request.form['nationality']

    cursor.execute('UPDATE authors SET first_name = %s, last_name = %s, birth_year = %s, nationality = %s WHERE author_id = %s',
                   (first_name, last_name, birth_year, nationality, author_id))
    db.commit()

    flash('Author updated successfully!', 'success')
    return redirect(url_for('authors.show_authors'))

@authors.route('/delete_author/<int:author_id>', methods=['POST'])
def delete_author(author_id):
    db = get_db()
    cursor = db.cursor()

    # Delete the author (cascade will delete associated books)
    cursor.execute('DELETE FROM authors WHERE author_id = %s', (author_id,))
    db.commit()

    flash('Author deleted successfully!', 'danger')
    return redirect(url_for('authors.show_authors'))
