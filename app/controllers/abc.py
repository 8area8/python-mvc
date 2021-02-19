"""Controller interface."""

from abc import ABC

from app.commands import Command, BlankCommand
from app.views import View


class Controller(ABC):
    """Base controller."""

    def __init__(self, *args, **kwargs):
        """Init."""
        self.view: View = View()

    def display(self):
        """Display the view."""
        self.view.display()

    def get_command(self) -> Command:
        """Get the command."""
        return BlankCommand()
