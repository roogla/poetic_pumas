from __future__ import annotations

from typing import Type

from .block import Block
from .blockdude import BlockDude
from .bottomwall import BottomWall
from .exitdoor import ExitDoor
from .ground import Ground
from .levelelement import LevelElement
from .space import Space
from .topbottomwall import TopBottomWall
from .topwall import TopWall
from .wall import Wall

# All of the elements that will be used in the game layout.
active_elements: tuple[Type[LevelElement], ...] = (
    Wall,
    TopWall,
    BottomWall,
    TopBottomWall,
    Block,
    BlockDude,
    Ground,
    Space,
    ExitDoor,
)
