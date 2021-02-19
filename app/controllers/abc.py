"""Controller interface."""

from abc import ABC

from app.commands import Command, BlankCommand


class Controller(ABC):
    """Base controller."""

    def display(self):
        """Display the view."""
        pass

    def get_command(self) -> Command:
        """Get the command."""
        return BlankCommand()
