from .levelelement import LevelElement


class NullElement(LevelElement):
    """For when there is no element found."""

    level_symbol = "?"
    string_symbol = "?"
