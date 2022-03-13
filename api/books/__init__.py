from flask import Blueprint


books = Blueprint('books', __name__)
from api.books import routes    # NOQA
