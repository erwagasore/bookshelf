from flask import Flask

from api.factory import db, marshmallow, create_api
from api.books.models import Book

api = create_api()
