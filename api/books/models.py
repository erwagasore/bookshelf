from api import db, marshmallow


class Book(db.Model):
    """"Represent books record structure."""
    __tablename__ = 'books'
    id = db.Column(db.Integer, primary_key=True)
    available = db.Column(db.Boolean, default=True)
    title = db.Column(db.String)
    timestamp = db.Column(db.String)

    def __init__(self, id, available, title, timestamp):
        self.id = id
        self.available = available
        self.title = title
        self.timestamp = timestamp


class BookSchema(marshmallow.SQLAlchemyAutoSchema):
    class Meta:
        model = Book
