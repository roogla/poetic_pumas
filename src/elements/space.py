from __future__ import annotations

from .levelelement import LevelElement


class Space(LevelElement):
    """In the map, this represents empty space. Cannot be interacted with."""

    level_symbol = "."
    string_symbol = "\u2800\u2800"


# TODO: This is an anti-pattern. We can review this.
def is_space_element(level_element: LevelElement) -> bool:
    """Determines whether the object is a `Space` level element or not."""
    return isinstance(level_element, Space)
