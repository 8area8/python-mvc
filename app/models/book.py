"""Book module."""

from typing import Optional


class Book:
    """Handle the books."""

    books = {
        1: {"name": "Le seigneur des anneaux", "price": 12},
        2: {"name": "L'oiseau d'amérique", "price": 8},
        3: {"name": "Bambie", "price": 10},
    }

    def __init__(self, name: str, price: int):
        """Init."""
        self.name = name
        self.price = price
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
        to_dict = {key: value for key, value in vars(self).items() if key != "id"}
        if not self.id:
            new_id = self.last_id + 1
            self.books[new_id] = to_dict
        else:
            self.books[self.id] = to_dict

    def delete(self):
        """Delete the book."""
        if self.id:
            del self.books[self.id]

    @classmethod
    def get(cls, id: int) -> Optional["Book"]:
        """Get a book from the given ID."""
        db_book = cls.books.get(id)
        if db_book:
            book = Book(**db_book)  # type: ignore
            book.id = id
            return book
        return None

    @classmethod
    def list(cls):
        """List the books."""
        books = []
        for id, db_book in cls.books.items():
            book = Book(**db_book)
            book.id = id
            books.append(book)
        return books

    def __str__(self):
        """Return the book details."""
        return f"id: {self.id}\nname: {self.name}\nprice: {self.price}"
