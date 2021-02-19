"""Command interface."""

from abc import ABC
from typing import Any


class Command(ABC):
    """Absctract command."""

    def execute(self, context: Any):
        """Execute the command."""
        pass
