from .levelelement import LevelElement


class Wall(LevelElement):
    """Default wall when not at the top or making contact with the ground."""

    level_symbol = "W"
    string_symbol = "🟫"
