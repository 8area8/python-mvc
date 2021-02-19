"""Book module."""

from typing import Optional


class Book:
    """Handle the books."""

    books = {1: {"name": "Le seigneur des anneaux"}}

    def __init__(self, name: str):
        """Init."""
        self.name = name
        self.id: Optional[int] = None

    @property
    def last_id(self):
        """Return the last ID or 1."""
        try:
            return list(self.books.keys())[-1]
        except IndexError:
            return 1

    def save(self):
        """Save the book.

        Create the book if the ID is None, or update it.
        """
        if not self.id:
            new_id = self.last_id + 1
            self.books[new_id] = {"name": self.name}
        else:
            self.books[self.id] = {"name": self.name}

    @classmethod
    def get(cls, id: int) -> Optional["Book"]:
        """Get a book from the given ID."""
        db_book = cls.books.get(id)
        if db_book:
            book = Book(name=db_book["name"])
            book.id = id
            return book
        return None
