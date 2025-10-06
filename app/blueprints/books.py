from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.db_connect import get_db

books = Blueprint('books', __name__)

@books.route('/', methods=['GET', 'POST'])
def show_books():
    db = get_db()
    cursor = db.cursor()

    # Handle POST request to add a new book
    if request.method == 'POST':
        title = request.form['title']
        author_id = request.form['author_id']
        isbn = request.form['isbn']
        publication_year = request.form['publication_year']
        genre = request.form['genre']
        pages = request.form['pages']

        # Insert the new book into the database
        cursor.execute('INSERT INTO books (title, author_id, isbn, publication_year, genre, pages) VALUES (%s, %s, %s, %s, %s, %s)',
                       (title, author_id, isbn, publication_year, genre, pages))
        db.commit()

        flash('New book added successfully!', 'success')
        return redirect(url_for('books.show_books'))

    # Handle GET request to display all books with author information
    cursor.execute('''
        SELECT b.book_id, b.title, b.isbn, b.publication_year, b.genre, b.pages,
               b.created_at, b.updated_at, b.author_id,
               a.first_name, a.last_name
        FROM books b
        JOIN authors a ON b.author_id = a.author_id
        ORDER BY b.title
    ''')
    all_books = cursor.fetchall()

    # Get all authors for the dropdown
    cursor.execute('SELECT author_id, first_name, last_name FROM authors ORDER BY last_name, first_name')
    all_authors = cursor.fetchall()

    return render_template('books.html', all_books=all_books, all_authors=all_authors)

@books.route('/update_book/<int:book_id>', methods=['POST'])
def update_book(book_id):
    db = get_db()
    cursor = db.cursor()

    # Update the book's details
    title = request.form['title']
    author_id = request.form['author_id']
    isbn = request.form['isbn']
    publication_year = request.form['publication_year']
    genre = request.form['genre']
    pages = request.form['pages']

    cursor.execute('UPDATE books SET title = %s, author_id = %s, isbn = %s, publication_year = %s, genre = %s, pages = %s WHERE book_id = %s',
                   (title, author_id, isbn, publication_year, genre, pages, book_id))
    db.commit()

    flash('Book updated successfully!', 'success')
    return redirect(url_for('books.show_books'))

@books.route('/delete_book/<int:book_id>', methods=['POST'])
def delete_book(book_id):
    db = get_db()
    cursor = db.cursor()

    # Delete the book
    cursor.execute('DELETE FROM books WHERE book_id = %s', (book_id,))
    db.commit()

    flash('Book deleted successfully!', 'danger')
    return redirect(url_for('books.show_books'))
