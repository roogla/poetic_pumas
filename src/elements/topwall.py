from .levelelement import LevelElement


class TopWall(LevelElement):
    """The last wall element at the top of a series of walls."""

    level_symbol = "T"
    string_symbol = "🟫"
