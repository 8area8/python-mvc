"""App module."""

from app.controllers import Controller, MainPageController


class Application:
    """Application context.

    Use the strategy pattern.

    Attrs:
    - controller (Controller): the "strategy". Handle a page in the application.
    - running (bool): True if the application is running else False.
    """

    def __init__(self):
        """Initialize the main page."""
        self.controller: Controller = MainPageController()
        self.running = True

    def run(self):
        """Run the application."""
        self.controller.display()
        command = self.controller.get_command()
        command.execute(context=self)