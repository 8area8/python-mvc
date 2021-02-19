"""Book details command."""

from .abc import Command
from app.controllers import BookDetailsController


class BookDetailsCommand(Command):
    """Handle the book details command."""

    def __init__(self, book):
        """Init."""
        self.book = book

    def execute(self, context):
        """Go to the book details."""
        context.controller = BookDetailsController(book=self.book)
