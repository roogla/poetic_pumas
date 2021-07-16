from __future__ import annotations

import src.game.element_data as element_data
from src import elements
from src.game.movement import Movement
from src.game.vector2D import Vector2D

from .levelelement import LevelElement
from .space import is_space_element


class Dude(LevelElement):
    """Block Dude himself. The main character."""

    level_symbol = "D"
    face = {
        "LEFT": "👈",
        "RIGHT": "👉",
    }
    string_symbol = face["LEFT"]

    def __init__(self, x: int, y: int):
        super().__init__(x, y)
        # Whether the Level Element is carrying a block
        self.carrying = False

    @property
    def is_facing_left(self) -> bool:
        """Whether the level element is facing left."""
        return self.string_symbol == self.face["LEFT"]

    @property
    def is_facing_right(self) -> bool:
        """Whether the level element is facing right."""
        return self.string_symbol == self.face["RIGHT"]

    def set_facing_left(self) -> None:
        """Changes the direction of the level element to face leftward symbolically."""
        self.string_symbol = self.face["LEFT"]

    def set_facing_right(self) -> None:
        """Changes the direction of the level element to face rightward symbolically."""
        self.string_symbol = self.face["RIGHT"]

    def move(self, data: element_data.ElementData, direction: Vector2D) -> None:
        """Moves this level element laterally by some number of spaces given.

        The number of spaces can be positive or negative.
        """
        lateral_position = self.position + direction
        lateral_element = data.level.get_element_at_position(lateral_position)
        destination = lateral_position

        if is_space_element(lateral_element):
            destination = lateral_position
            data.soundboard.play_sfx("step")
        else:
            destination = self.position
            data.soundboard.play_sfx("bump")

        data.level.move_element(self.position, destination)
        self.drop(data)
        data.renderer.render_level(data.level)

    def drop(self, data: element_data.ElementData) -> None:
        """Drop this level element down if hanging over space."""
        below = self.position + Movement.DOWN
        while is_space_element(data.level.get_element_at_position(below)):
            below.add(Movement.DOWN)

        destination = below + Movement.UP

        data.level.move_element(self.position, destination)

    def move_up(self, data: element_data.ElementData) -> None:
        """Move this level element upward according to the rules."""
        if self.string_symbol == self.face["LEFT"]:
            self.move(data, Movement.UP + Movement.LEFT)
        if self.string_symbol == self.face["RIGHT"]:
            self.move(data, Movement.UP + Movement.RIGHT)

    def move_left(self, data: element_data.ElementData) -> None:
        """Move this level element leftward according to the rules.

        If there are any objects to the left of block dude, he cannot move left.
        """
        self.set_facing_left()
        self.move(data, Movement.LEFT)

    def move_right(self, data: element_data.ElementData) -> None:
        """Move this level element rightward according to the rules.

        If there are any objects to the left of block dude, he cannot move left.
        """
        self.set_facing_right()
        self.move(data, Movement.RIGHT)

    def box_action(self, data: element_data.ElementData) -> None:
        """The box action."""
        lateral_position = Vector2D(0, 0)
        if self.is_facing_left:
            lateral_position = self.position + Movement.LEFT
        if self.is_facing_right:
            lateral_position = self.position + Movement.RIGHT

        lateral_element = data.level.get_element_at_position(lateral_position)
        if self.carrying is False:
            if isinstance(lateral_element, elements.Block):
                data.level.move_element(lateral_position, self.position + Movement.UP)
                self.carrying = True
        if self.carrying is True:
            if isinstance(lateral_element, elements.Space):
                data.level.move_element(self.position + Movement.UP, lateral_position)
                self.carrying = False

        data.renderer.render_level(data.level)
