"""Handle the main page."""

from app.commands import BookDetailsCommand
from app.views import MainPageView
from app.models.book import Book

from .abc import Controller


class MainPageController(Controller):
    """Main page."""

    def __init__(self):
        """Init."""
        super().__init__()
        self.commands = [BookDetailsCommand] + self.commands
        self.view = MainPageView(self.commands)

    def display(self):
        """Display the main page."""
        books = Book.list()
        self.view.display(books=books)
