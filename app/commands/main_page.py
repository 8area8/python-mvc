"""Main page command."""

from .abc import Command
from app.controllers import MainPageController


class MainPageCommand(Command):
    """Handle the main page navigation."""

    def execute(self, context):
        """Go to the main page."""
        context.controller = MainPageController()
