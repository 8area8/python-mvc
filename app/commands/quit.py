"""Quit command."""

from .abc import Command


class Quit(Command):
    """Quit command."""

    key = "quit"
    readable_key = key
    description = "quit the program."

    def execute(self, context):
        """Quit the program."""
        context.running = False
