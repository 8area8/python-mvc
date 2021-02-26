"""Main page view."""

from app.commands import BookDetailsCommand

from .abc import View


class MainPageView(View):
    """Display the main page."""

    def __init__(self, commands):
        """Init."""
        super().__init__(commands)
        self.title = "Main Page"

    def display_body(self, books):
        """Display the books."""
        print("Books:")
        for command, book in zip(BookDetailsCommand.get_choices(), books):
            print(command, book.name)
