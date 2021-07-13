from .levelelement import LevelElement


class BottomWall(LevelElement):
    """The wall element that makes contact with the ground."""

    level_symbol = "V"
    string_symbol = "║"
