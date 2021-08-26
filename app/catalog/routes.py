from app.catalog import main
from app.catalog.models import Book, Publication
from app import db
from flask import render_template


@main.route('/')
def display_books():
    books = Book.query.all()
    return render_template('home.html', books=books)
