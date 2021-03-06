from dataclasses import dataclass

from blessed.keyboard import Keystroke


@dataclass(init=False)
class Key:
    """A collection of all the valid key inputs for the game."""

    UP = u"KEY_UP"
    W = u"W"
    w = u"w"
    LEFT = u"KEY_LEFT"
    A = u"A"
    a = u"a"
    DOWN = u"KEY_DOWN"
    S = u"S"
    s = u"s"
    RIGHT = u"KEY_RIGHT"
    D = u"D"
    d = u"d"
    ESCAPE = u"KEY_ESCAPE"
    SPACE = u" "
    q = u"q"
    Q = u"Q"
    w = u"w"
    W = u"W"
    a = u"a"
    A = u"A"
    s = u"s"
    S = u"S"
    d = u"d"
    D = u"D"
    r = u"r"
    R = u"R"

    def __init__(self, keystroke: Keystroke):
        self._keystroke = keystroke

    @property
    def name(self) -> str:
        """The stringified appearance of the keystroke.

        `Blessed.py` loves to obscure away the name depending on whether it's a
        character or a keystroke input like `LEFT_KEY`.
        """
        keystroke = self._keystroke
        return str(keystroke) if keystroke.name is None else keystroke.name
