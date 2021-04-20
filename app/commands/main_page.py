"""Main page command."""

from app import models

from .abc import Command


class MainPage(Command):
    """Handle the main page navigation."""

    key = "main"
    readable_key = key
    description = "return to the main page."

    def execute(self, context):
        """Go to the main page."""
        context.change_page("main_page", books=models.Book.list())
