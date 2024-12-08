from flask import Blueprint, request, jsonify
from .models import Book, Member
from . import db
import datetime
from flask import Flask, jsonify
from app.auth import token_required

app = Flask(__name__)

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return jsonify({'message': 'Welcome to the Library Management System API'})


# CRUD for Books
@main.route('/books', methods=['GET', 'POST'])
def handle_books():
    if request.method == 'GET':
        search_query = request.args.get('search', '')
        books = Book.query.filter(
            (Book.title.contains(search_query)) | 
            (Book.author.contains(search_query))
        ).all()
        return jsonify([{"id": b.id, "title": b.title, "author": b.author} for b in books])

    if request.method == 'POST':
        data = request.get_json()
        new_book = Book(title=data['title'], author=data['author'], published_year=data['published_year'])
        db.session.add(new_book)
        db.session.commit()
        return jsonify({"message": "Book added successfully"}), 201

@main.route('/books/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def handle_book(id):
    book = Book.query.get_or_404(id)

    if request.method == 'GET':
        return jsonify({"id": book.id, "title": book.title, "author": book.author, "published_year": book.published_year})

    if request.method == 'PUT':
        data = request.get_json()
        book.title = data['title']
        book.author = data['author']
        book.published_year = data['published_year']
        db.session.commit()
        return jsonify({"message": "Book updated successfully"})

    if request.method == 'DELETE':
        db.session.delete(book)
        db.session.commit()
        return jsonify({"message": "Book deleted successfully"})


@main.route('/books/page/<int:page>', methods=['GET'])
def paginate_books(page):
    per_page = 5
    paginated_books = Book.query.paginate(page, per_page, False)
    books = [{"id": b.id, "title": b.title, "author": b.author} for b in paginated_books.items]
    return jsonify(books)
@app.route('/protected', methods=['GET'])
@token_required
def protected_route():
    return jsonify({'message': 'This is a protected route!'})


