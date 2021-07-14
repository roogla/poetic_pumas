from .levelelement import LevelElement


class Ground(LevelElement):
    """The ground surface upon which Block Dude can walk."""

    level_symbol = "G"
    string_symbol = "🟫"
