from dataclasses import dataclass


@dataclass(frozen=True, init=False)
class Key:
    """A collection of all the valid key inputs for the game."""

    UP = u"KEY_UP"
    LEFT = u"KEY_LEFT"
    DOWN = u"KEY_DOWN"
    RIGHT = u"KEY_RIGHT"
    SPACE = u" "
