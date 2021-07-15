# from ..level import Level
from dataclasses import dataclass

from src.vector2D import Vector2D

from .element_data import ElementData
from .levelelement import LevelElement
from .space import is_space_element


@dataclass(init=False)
class Movements:
    """Helper basic movement `Vector2D` instances."""

    LEFT = Vector2D(-1, 0)
    RIGHT = Vector2D(1, 0)
    UP = Vector2D(0, -1)
    DOWN = Vector2D(0, 1)
    UP_LEFT = Vector2D(-1, -1)
    UP_RIGHT = Vector2D(1, 1)


class Dude(LevelElement):
    """Block Dude himself. The main character."""

    level_symbol = "D"
    face = {"LEFT": "👈", "RIGHT": "👉"}
    string_symbol = face["LEFT"]

    def move(self, data: ElementData, direction: Vector2D) -> None:
        """Moves this level element laterally by some number of spaces given.

        The number of spaces can be positive or negative.
        """
        position = data.level.get_element_position(self)
        lateral_position = position + direction
        lateral_element = data.level.get_element_at_position(lateral_position)
        destination = lateral_position

        if is_space_element(lateral_element):
            destination = lateral_position
            data.soundboard.play_sfx("step")
        else:
            destination = position
            data.soundboard.play_sfx("bump")

        data.level.move_element(position, destination)
        self.drop(data)
        data.renderer.render_level(data.level)

    def drop(self, data: ElementData) -> None:
        """Drop this level element down if hanging over space."""
        position = data.level.get_element_position(self)
        below = position + Movements.DOWN
        while is_space_element(data.level.get_element_at_position(below)):
            below.add(Movements.DOWN)

        destination = below + Movements.UP

        data.level.move_element(position, destination)

    def move_up(self, data: ElementData) -> None:
        """Move this level element upward according to the rules."""
        if self.string_symbol == self.face["LEFT"]:
            self.move(data, Movements.UP + Movements.LEFT)
        if self.string_symbol == self.face["RIGHT"]:
            self.move(data, Movements.UP + Movements.RIGHT)

    def move_left(self, data: ElementData) -> None:
        """Move this level element leftward according to the rules.

        If there are any objects to the left of block dude, he cannot move left.
        """
        self.string_symbol = self.face["LEFT"]
        self.move(data, Movements.LEFT)

    def move_right(self, data: ElementData) -> None:
        """Move this level element leftward according to the rules.

        If there are any objects to the left of block dude, he cannot move left.
        """
        self.string_symbol = self.face["RIGHT"]
        self.move(data, Movements.RIGHT)
