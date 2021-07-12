from dataclasses import dataclass
from typing import Any

# from src.level import Level
from src.renderer import Renderer

# from .levelelement import LevelElement


@dataclass
class ElementData:
    """Packages up the data LevelElements need to know in order to move properly
    and render appropriately.
    """

    level: Any  # Level
    renderer: Renderer
    level_element: Any  # LevelElement
