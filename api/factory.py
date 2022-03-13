import os
from http import HTTPStatus

from flask import Flask, jsonify
from flask.cli import load_dotenv
from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def bad_request(e):
    response = jsonify({
        'error': HTTPStatus.BAD_REQUEST.phrase,
        'message': HTTPStatus.BAD_REQUEST.description
    })
    response.status_code = HTTPStatus.BAD_REQUEST.value
    return response


def not_found(e):
    response = jsonify({
        'error': HTTPStatus.NOT_FOUND.phrase,
        'message': HTTPStatus.NOT_FOUND.description
    })
    response.status_code = HTTPStatus.NOT_FOUND.value
    return response


def method_not_allowed(e):
    response = jsonify({
        'error': HTTPStatus.METHOD_NOT_ALLOWED.phrase,
        'message': HTTPStatus.METHOD_NOT_ALLOWED.description
    })
    response.status_code = HTTPStatus.METHOD_NOT_ALLOWED.value
    return response


def internal_server_error(e):
    response = jsonify({
        'error': HTTPStatus.INTERNAL_SERVER_ERROR.phrase,
        'message': HTTPStatus.INTERNAL_SERVER_ERROR.description
    })
    response.status_code = HTTPStatus.INTERNAL_SERVER_ERROR.value
    return response

def create_api():
    api = Flask(__name__)


    # configurations
    PROJECT_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
    api.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{PROJECT_DIR}/bookshelf.db'
    api.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # initialize extensions
    db.init_app(api)

    # register blueprints
    from api.books import books
    api.register_blueprint(books)

    # register errorhandlers
    # TODO: add more error handlers to cover all api excptions
    api.register_error_handler(HTTPStatus.BAD_REQUEST.value, bad_request)
    api.register_error_handler(HTTPStatus.NOT_FOUND.value, not_found)
    api.register_error_handler(HTTPStatus.NOT_FOUND.value, method_not_allowed)
    api.register_error_handler(Exception, internal_server_error)

    return api
