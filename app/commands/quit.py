"""Quit command."""

from .abc import Command


class QuitCommand(Command):
    """Quit command."""

    key = "quit"
    readable_key = key
    lang_en = "quit the program."

    def execute(self, context):
        """Quit the program."""
        context.running = False
