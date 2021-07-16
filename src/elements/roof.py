from .levelelement import LevelElement


class Roof(LevelElement):
    """The roof of the Level so that the telekinesis box can't crash the game"""

    level_symbol = "R"
    string_symbol = "🟫"
