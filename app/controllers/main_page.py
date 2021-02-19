"""Handle the main page."""

from .abc import Controller
from app.commands import BlankCommand
from app.models.book import Book


class MainPageController(Controller):
    """Main page."""

    def __init__(self):
        """Init."""
        self.view = MainPageView()

        self.commands = {}
        for index, book in enumerate(Book.books, start=1):
            self.commands[f"l-{index}"] = BookDetailsCommand(book=book)

    def display(self):
        """Display the main page."""
        self.view.display()

    def get_command(self):
        """Get the command."""
        choice = input()

        if choice.startswith("l-"):
            book_id = int(choice.replace("l-", ""))
            book = Book.get(book_id)
            if book:
                return BookDetailsCommand(book=book)

        if choice == "3":
            return QuitCommand()

        return BlankCommand()
