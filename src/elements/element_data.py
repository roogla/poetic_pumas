from __future__ import annotations

from dataclasses import dataclass

import src.elements.levelelement as levelelement
import src.level as lvl  # named this way to avoid conflict with var name in ElementData
from src.renderer import Renderer
from src.soundboard import Soundboard


@dataclass
class ElementData:
    """Object aggregation for easier movement through code.

    Packages up the data LevelElements need to know in order to move properly
    and render appropriately.
    """

    level: lvl.Level
    renderer: Renderer
    level_element: levelelement.LevelElement
    soundboard: Soundboard
