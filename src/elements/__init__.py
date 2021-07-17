from __future__ import annotations

from typing import Type

from .block import Block
from .bottomwall import BottomWall
from .dude import Dude
from .exitdoor import ExitDoor
from .ground import Ground
from .levelelement import ControllableLevelElement, LevelElement
from .null_element import NullElement
from .space import Space
from .topbottomwall import TopBottomWall
from .topwall import TopWall
from .wall import Wall
from .tele_pad import TelekinesisPad
from .tele_block import TelekinesisBlock

# All of the elements that will be used in the game layout.
ACTIVE_ELEMENTS: tuple[Type[LevelElement], ...] = (
    Wall,
    TopWall,
    BottomWall,
    TelekinesisBlock,
    TelekinesisPad,
    TopBottomWall,
    Block,
    Dude,
    Ground,
    Space,
    ExitDoor,
)

# Expose for better pep compliance
__all__ = [
    "ACTIVE_ELEMENTS",
    "Block",
    "BottomWall",
    "Dude",
    "ExitDoor",
    "Ground",
    "ControllableLevelElement",
    "LevelElement",
    "NullElement",
    "Space",
    "TelekinesisBlock",
    "TelekinesisPad",
    "TopBottomWall",
    "TopWall",
    "Wall",
]
