from __future__ import annotations

from dataclasses import dataclass

import src.elements.levelelement as levelelement

# named this way to avoid conflict with var name in ElementData
import src.level as lvl
from src.renderer import Renderer


@dataclass
class ElementData:
    """Object aggregation for easier movement through code.

    Packages up the data LevelElements need to know in order to move properly
    and render appropriately.
    """

    level: lvl.Level
    renderer: Renderer
    level_element: levelelement.LevelElement
