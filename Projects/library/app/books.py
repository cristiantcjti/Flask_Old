from flask import Blueprint, current_app, request
from .model import Book
from .serializer import BookSchema

bp_books = Blueprint('books', __name__)

@bp_books.route('/create', methods=['POST',])
def create():
    bookschema = BookSchema()
    book = bookschema.load(request.json)
    current_app.db.session.add(book)
    current_app.db.session.commit()
    return bookschema.jsonify(book), 201
    #return {}, 201



@bp_books.route('/list', methods=['GET',])
def list():
    bookschema = BookSchema(many=True)
    result = Book.query.all()
    return bookschema.jsonify(result), 200



@bp_books.route('/retrive', methods=['GET',])
def retrive():
    ...


@bp_books.route('/update', methods=['PUT', 'PATCH'])
def update():
    ...


@bp_books.route('/delete', methods=['DELETE',])
def delete():
    ...


