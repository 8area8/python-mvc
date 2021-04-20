"""Book uodate page view."""

from app import commands

from .abc import View


class BookUpdate(View):
    """Display the book updates."""

    name = "update_book"

    def __init__(self, book):
        """Init."""
        super().__init__()
        self.title = "Book Update"
        self.book = book
        self.commands += [commands.BookDetails]

    def display_body(self):
        """Display the book update."""
        print(self.book)
