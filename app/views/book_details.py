"""Book details page view."""

from .abc import View


class BookDetailsView(View):
    """Display the book details."""

    def __init__(self, commands, book):
        """Init."""
        super().__init__(commands)
        self.title = "Book details"
        self.book = book

    def display_body(self):
        """Display the book details."""
        print(self.book)
