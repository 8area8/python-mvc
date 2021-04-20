"""Entry point."""

from app.app import Application
from app.views import MainPage
from app.models import Book


if __name__ == "__main__":
    app = Application(MainPage(Book.list()))
    app.run()
