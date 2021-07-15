from __future__ import annotations

from dataclasses import dataclass

from .levelelement import LevelElement
# named this way to avoid conflict with var name in ElementData
from ..level import Level as lvl
from ..renderer import Renderer


@dataclass
class ElementData:
    """Object aggregation for easier movement through code.

    Packages up the data LevelElements need to know in order to move properly
    and render appropriately.
    """

    level: lvl
    renderer: Renderer
    level_element: LevelElement
