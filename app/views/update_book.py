"""Book uodate page view."""

from .abc import View


class BookUpdateView(View):
    """Display the book updates."""

    def __init__(self, commands, book):
        """Init."""
        super().__init__(commands)
        self.title = "Book update"
        self.book = book

    def display_body(self):
        """Display the book update."""
        print(self.book)
