"""Book details page view."""

from .abc import View


class BookDetailsView(View):
    """Display the book details."""

    def __init__(self, commands):
        """Init."""
        super().__init__(commands)
        self.title = "Book details"

    def display_body(self, book):
        """Display the book details."""
        print(book)
