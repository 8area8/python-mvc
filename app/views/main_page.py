"""Main page view."""

from app import commands

from .abc import View


class MainPage(View):
    """Display the main page."""

    name = "main_page"

    def __init__(self, books):
        """Init."""
        super().__init__()
        self.title = "Main Page"
        self.books = books
        self.commands += [commands.BookDetails]

    def display_body(self):
        """Display the books."""
        print("Books:")
        for command, book in zip(commands.BookDetails.get_choices(), self.books):
            print(command, book.name)  # type: ignore
