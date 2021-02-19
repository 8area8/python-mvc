"""Handle the main page."""

from app.commands import BlankCommand, QuitCommand, BookDetailsCommand
from app.models.book import Book

from .abc import Controller


class MainPageController(Controller):
    """Main page."""

    def __init__(self):
        """Init."""
        self.view = MainPageView(self.commands)

        self.commands = [QuitCommand, BookDetailsCommand]

    def display(self):
        """Display the main page."""
        books = Book.books
        self.view.display(books=books)

    def get_command(self):
        """Get the command."""
        choice = input()

        if not choice:
            return BlankCommand()

        if not choice.isdigit() or int(choice) not in self.choices:
            return WrongCommand()

        choice = int(choice)

        if choice.startswith("l-"):
            book_id = int(choice.replace("l-", ""))
            book = Book.get(book_id)
            if book:
                return BookDetailsCommand(book=book)

        if choice == "3":
            return QuitCommand()
