"""Book details controller."""

from app.models import Book
from app.views import BookDetailsView

from .abc import Controller


class BookDetailsController(Controller):
    """Handle the book details."""

    def __init__(self, book: Book):
        """Init."""
        self.book = book
        self.view = BookDetailsView(self.commands)
