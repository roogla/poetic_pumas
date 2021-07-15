from __future__ import annotations

from dataclasses import dataclass

from ..elements.levelelement import LevelElement
from .level import Level
from .renderer import Renderer
from .vector2D import Vector2D


@dataclass
class ElementData:
    """Object aggregation for easier movement through code.

    Packages up the data LevelElements need to know in order to move properly
    and render appropriately.
    """

    level: Level
    renderer: Renderer
    level_element: LevelElement

    def move_left(self) -> None:
        """Return the left-movement level element position according to its rules."""
        position = self.level.get_element_position(self.level_element)
        one_unit_leftward = position + Vector2D(-1, 0)
        self.level.move_element(position, one_unit_leftward)
        self.renderer.render_level(self.level)

    def move_right(self) -> None:
        """Return the left-movement level element position according to its rules."""
        position = self.level.get_element_position(self.level_element)
        one_unit_leftward = position + Vector2D(1, 0)
        self.level.move_element(position, one_unit_leftward)
        self.renderer.render_level(self.level)
