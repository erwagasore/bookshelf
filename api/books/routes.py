from datetime import datetime

from http import HTTPStatus
from flask import request, abort
from marshmallow import Schema, fields

from api import db
from api.books import books
from api.books.models import Book, BookSchema


schema = BookSchema()


class RequestBookSchema(Schema):
    title = fields.Str(required=True)
    email = fields.Email(required=True)


@books.route("/request", methods=['POST'])
def get_request():
    """Get book request by id."""
    data = request.get_json()
    request_schema = RequestBookSchema()
    errors = request_schema.validate(data)

    # TODO: clean erros for better message
    if errors:
        return {
            'message': str(errors)
        }

    title = data.get('title')
    book = Book.query.filter_by(title=title).first_or_404()

    book.available = False
    book.timestamp = datetime.now().isoformat()
    db.session.commit()

    return schema.dump(book)



@books.route("/request/<int:id>", methods=['GET'])
def read(id):
    """Get book request by id."""
    book = Book.query.get_or_404(id)
    return schema.dump(book)


@books.route("/request", methods=['GET'])
def list():
    """Get all book requests"""
    available_books = Book.query.all()

    return {
        'books': schema.dump(available_books, many=True)
    }


@books.route("/request/<int:id>", methods=['DELETE'])
def delete(id):
    """Delete book request by id."""
    book = Book.query.get_or_404(id)
    db.session.delete(book)
    db.session.commit()

    return {}, 204
