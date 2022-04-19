from flask import Blueprint, current_app, request, jsonify
from flask.helpers import make_response
from .model import Book
from .serializer import BookSchema

bp_books = Blueprint('books', __name__)

@bp_books.route('/create', methods=['POST',])
def create():
    bookschema = BookSchema()
    book = bookschema.load(request.json)
    current_app.db.session.add(book)
    current_app.db.session.commit()
    result = bookschema.dump(book)
    return make_response(jsonify({"created":result}))


@bp_books.route('/list', methods=['GET',])
def list():
    get_results = Book.query.all()
    bookschema = BookSchema(many=True)
    result = bookschema.dump(get_results)
    return make_response(jsonify({"all":result}))



@bp_books.route('/retrive/<id>', methods=['GET',])
def retrive(id):
    get_result = Book.query.get(id)
    bookschema = BookSchema()
    result = bookschema.dump(get_result)
    return make_response(jsonify({"result":result}))


@bp_books.route('/update/<id>', methods=['PUT', 'PATCH'])
def update(id):
    query = Book.query.get(id)
    data = request.get_json()
    if data.get('title'):
       query.title = data['title']
    if data.get('author'):
       query.author = data['author']
    current_app.db.session.add(query)
    current_app.db.session.commit()
    bookschema = BookSchema()
    result = bookschema.dump(query)
    return make_response(jsonify({"updated":result}))
   


@bp_books.route('/delete/<id>', methods=['DELETE',])
def delete(id):
    Book.query.filter(Book.id == id).delete()
    current_app.db.session.commit()
    # return jsonify('Register deleted')
    return make_response(jsonify("Successuly deleted"))

