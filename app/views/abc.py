"""Base view."""


class View:
    """ABC view."""

    def display(self, *args, **kwargs):
        """Display the page."""
        self.display_header()
        self.display_body(*args, **kwargs)
        self.display_footer()

    def display_header(self):
        """Display the Header."""
        pass

    def display_body(*args, **kwargs):
        """Display the body."""
        pass

    def display_footer(self):
        """Display the footer."""
        pass
