from __future__ import annotations

from .levelelement import ControllableLevelElement


class Block(ControllableLevelElement):
    """The basic block that Block Dude can interact with."""

    level_symbol = "B"
    string_symbol = "🟩"
