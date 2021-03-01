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
        self.commands.append(BookDetailsCommand)
        self.view = MainPageView(self.commands, Book.list())
