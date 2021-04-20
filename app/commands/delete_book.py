"""Book delete command."""

from app import views

from .abc import Command
from .main_page import MainPage


class DeleteBook(Command):
    """Handle the book deletion."""

    key = "delete"
    readable_key = key
    description = "delete the book."

    def execute(self, context):
        """Delete the book and go to the main page."""
        context.view.book.delete()
        MainPage().execute(context)
        context.view.messages.append(views.BookUpdate.book_deleted)
