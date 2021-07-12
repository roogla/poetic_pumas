from __future__ import annotations

from .levelelement import LevelElement


class Block(LevelElement):
    """The basic block that Block Dude can interact with."""

    level_symbol = "B"
    string_symbol = "■"
