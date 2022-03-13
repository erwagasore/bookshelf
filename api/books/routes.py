from flask import jsonify

from api.books import books


@books.route("/", methods=['POST'])
def create():
    """Create book request."""
    return {
        'message': f"Book created"
    }, 201



@books.route("/<int:id>", methods=['GET'])
def read(id):
    """Get book request by id."""
    return {
        'message': f"Book: {id}"
    }


@books.route("/", methods=['GET'])
def list():
    """Get all book requests"""
    return {
        'message': "All books"
    }

@books.route("/<int:id>", methods=['DELETE'])
def delete(id):
    """Delete book request by id."""
    return {}, 204
