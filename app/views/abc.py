"""Base view."""

from typing import List


class View:
    """ABC view."""

    SEPARATOR = "-"
    CENTER_LENGTH = 30
    SEPARATORS = SEPARATOR * CENTER_LENGTH

    messages: List[str] = []
    wrong_command = "Wrong command. Please, retry."
    enter_choice = "Enter a choice: "

    def __init__(self, commands):
        """Init."""
        self.title = ""
        self.commands = commands

    def print_part(self, part):
        """Print a part."""
        print(part.center(self.SEPARATORS))

    def display(self, *args, **kwargs):
        """Display the page."""
        self.display_header()
        print()
        self.display_messages()
        print()
        self.display_body(*args, **kwargs)
        print()
        self.display_footer()
        print()
        print(self.enter_choice)

    def display_header(self):
        """Display the Header."""
        self.print_part(self.title)

    def display_messages(self):
        """Display the messages."""
        for message in self.messages:
            print(message)
        self.messages = []

    def display_body(*args, **kwargs):
        """Display the body."""
        pass

    def display_footer(self):
        """Display the footer."""
        self.print_part("Commands")
        for command in self.commands:
            self.print_part(command.readable_key)
