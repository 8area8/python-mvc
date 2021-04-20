"""App module."""

from typing import List, Type

from app import views


Views = List[Type[views.View]]


class Application:
    """Application context.

    Use the strategy pattern.

    Attrs:
    - view (View): the "strategy". Handle a page in the application.
    - running (bool): True if the application is running else False.
    """

    views: Views = [views.MainPage, views.BookDetails, views.BookUpdate]

    def __init__(self, view):
        """Initialize the main page."""
        self.view: views.View = view
        self.running = True

    def run(self):
        """Run the application."""
        while self.running:
            self.view.display()
            command = self.view.prompt_for_command()
            command.execute(context=self)

    def change_page(self, view_name: str, *args, **kwargs):
        """Go to a new page."""
        for view in self.views:
            if view.name == view_name:
                self.view = view(*args, **kwargs)
                return

        raise ValueError(
            f"The view '{view_name}' does not exists. "
            f"Possible views are: {[v.name for v in self.views]}"
        )
