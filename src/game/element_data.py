from __future__ import annotations

from contextlib import contextmanager
from typing import Iterator

from src.elements.levelelement import ControllableLevelElement

from .level import Level
from .soundboard import Soundboard


class ElementData:
    """Object aggregation for easier movement through code.

    Packages up the data LevelElements need to know in order to move properly
    and render appropriately.
    """

    def __init__(self, level: Level, soundboard: Soundboard):
        self.level = level
        self.soundboard = soundboard

    @property
    def active_element(self) -> ControllableLevelElement:
        """The level active element."""
        return self.level.active_element

    @active_element.setter
    def active_element(self, element: ControllableLevelElement) -> None:
        """Set the level active element."""
        self.level.set_active_element(element)

    @contextmanager
    def setting_active_element(self, element: ControllableLevelElement) -> Iterator:
        """Set the level active element."""
        prev_element = self.active_element
        self.level.set_active_element(element)
        yield
        self.level.set_active_element(prev_element)
