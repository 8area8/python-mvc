"""Quit command."""

from .abc import Command


class QuitCommand(Command):
    """Quit command."""

    def execute(self, context):
        """Quit the program."""
        context.running = False
