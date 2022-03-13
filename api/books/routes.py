from api.books import books


@books.route("/", methods=['POST'])
def create():
    """Create book request."""
    pass



@books.route("/", methods=['GET'])
def read(id):
    """Get book request by id."""
    pass


@books.route("/", methods=['GET'])
def list():
    """Get all book requests"""
    pass


@books.route("/", methods=['DELETE'])
def delete(id):
    """Delete book request by id."""
    pass
