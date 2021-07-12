from __future__ import annotations

from dataclasses import dataclass

import src.elements.levelelement as levelelement
import src.level as level
from src.renderer import Renderer


@dataclass
class ElementData:
    """Object aggregation for easier movement through code.

    Packages up the data LevelElements need to know in order to move properly
    and render appropriately.
    """

    level: level.Level
    renderer: Renderer
    level_element: levelelement.LevelElement
