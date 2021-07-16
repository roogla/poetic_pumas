from __future__ import annotations

from typing import Type

from src.level import Level

from .block import Block
from .bottomwall import BottomWall
from .dude import Dude
from .exitdoor import ExitDoor
from .ground import Ground
from .levelelement import LevelElement
from .null_element import NullElement
from .space import Space
from .topbottomwall import TopBottomWall
from .topwall import TopWall
from .wall import Wall
from .roof import Roof
from .tele_block import TelekinesisBlock
from .tele_pad import TelekinesisPad
# All of the elements that will be used in the game layout.
active_elements: tuple[Type[LevelElement], ...] = (
    Wall,
    TopWall,
    BottomWall,
    TopBottomWall,
    Block,
    Dude,
    Ground,
    Roof,
    Space,
    ExitDoor,
    TelekinesisBlock,
    TelekinesisPad,
)

# Expose for better pep compliance
__all__ = (
    "Block",
    "Dude",
    "BottomWall",
    "ExitDoor",
    "Ground",
    "Roof",
    "Level",
    "NullElement",
    "Space",
    "TopBottomWall",
    "TopWall",
    "Wall",
    "TelekinesisBlock",
    "TelekinesisPad",
)
