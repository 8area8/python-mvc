"""Main page view."""

from app import commands

from .abc import View


class MainPageView(View):
    """Display the main page."""

    def __init__(self, commands, books):
        """Init."""
        super().__init__(commands)
        self.title = "Main Page"
        self.books = books

    def display_body(self):
        """Display the books."""
        print("Books:")
        for command, book in zip(commands.BookDetailsCommand.get_choices(), self.books):
            print(command, book.name)  # type: ignore
