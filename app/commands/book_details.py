"""Book details command."""

from app.controllers import BookDetailsController
from app.models import Book

from .abc import Command


class BookDetailsCommand(Command):
    """Handle the book details command."""

    key = "b-"
    readable_key = "b-<number>"

    def __init__(self, choice: str):
        """Init."""
        book_id = int(choice.replace(self.key, ""))
        self.book = Book.get(id=book_id)

    @classmethod
    def get_choices(cls):
        """Return the possible choices."""
        return [f"{cls.key}{index}" for index in range(1, len(Book.list()) + 1)]

    def execute(self, context):
        """Go to the book details."""
        context.controller = BookDetailsController(book=self.book)  # type: ignore
