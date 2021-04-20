"""Base view."""

import os
from typing import List

from app import commands


class View:
    """ABC view."""

    name = "abc"

    wrong_command = "'{}' is not a valid command. Please retry."

    def __init__(self, *args, **kwargs):
        """Init."""
        self.title = "ABC"
        self.messages: List[str] = []
        self.commands = [commands.Quit, commands.Blank]

        self.sep = "-"
        self.length = 30
        self.line = self.sep * self.length

    def print_part(self, part: str):
        """Print a part."""
        print(f" {part} ".center(self.length, self.sep))

    def clear(self):
        """Clear the console."""
        os.system("cls" if os.name == "nt" else "clear")

    def display(self):
        """Display the page."""
        self.clear()
        self.display_header()
        self.display_messages()
        self.display_body()
        self.display_footer()
        print()
        print("Enter a choice: ", end="")

    def display_header(self):
        """Display the Header."""
        print(self.line)
        self.print_part(self.title)

    def display_messages(self):
        """Display the messages."""
        if self.messages:
            print()
            for message in self.messages:
                print("*", message)
        self.messages = []
        print()

    def display_body(self):
        """Display the body."""
        pass

    def display_footer(self):
        """Display the footer."""
        print()
        self.print_part("Commands")
        for command in self.commands:
            if command.key:
                print(command.readable_key, ":", command.description)

    def prompt_for_command(self):
        """Prompt for a command."""
        choice = input()

        for Command in self.commands:
            if choice in Command.get_choices():
                return Command(choice)

        self.messages.append(self.wrong_command.format(choice))
        return commands.Blank()
