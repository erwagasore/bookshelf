from flask import Flask

from api.factory import db, create_api

api = create_api()
