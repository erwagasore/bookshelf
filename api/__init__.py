from flask import Flask

from api.factory import create_api

api = create_api()


@api.route("/")
def hello_world():
    return "<p>Hello, World!</p>"
