"""Book details controller."""

from app.models import Book
from app.views import BookDetailsView
from app.commands import MainPageCommand

from .abc import Controller


class BookDetailsController(Controller):
    """Handle the book details."""

    def __init__(self, book: Book):
        """Init."""
        super().__init__()
        self.book = book
        self.commands = [MainPageCommand] + self.commands
        self.view = BookDetailsView(self.commands)

    def display(self):
        """Display the book details."""
        self.view.display(book=self.book)
