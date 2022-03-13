from api import db


class BookRequest(db.Model):
    """"Represent book request record structure."""
    __tablename__ = 'book_requests'
    id = db.Column(db.Integer, primary_key=True)
    available = db.Column(db.Boolean, default=True)
    title = db.Column(db.String)
    timestamp = db.Column(db.String)
