"""Book details page view."""

from app import commands

from .abc import View


class BookDetails(View):
    """Display the book details."""

    name = "book_details"

    def __init__(self, book):
        """Init."""
        super().__init__()
        self.title = "Book Details"
        self.book = book
        self.commands += [commands.MainPage, commands.DeleteBook]

    def display_body(self):
        """Display the book details."""
        print(self.book)
