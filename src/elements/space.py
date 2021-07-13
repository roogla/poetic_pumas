from .levelelement import LevelElement


class Space(LevelElement):
    """In the map, this represents empty space. Cannot be interacted with."""

    level_symbol = "."
    string_symbol = " "
