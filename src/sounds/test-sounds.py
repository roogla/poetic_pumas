import os
import sys
import time
from random import choice
from string import ascii_lowercase as KEYS
from typing import Dict

from blessed import Terminal
from pygame import mixer

from src.soundboard import Soundboard

# adapted from https://stackoverflow.com/questions/16480898
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))


def close() -> None:
    """Closes the terminal and clears the screen"""
    print(term.clear)
    mixer.quit()
    sys.exit(0)


def draw(x: int, y: int, char: str) -> None:
    """Test"""
    print(term.move_xy(x, y) + term.bold_on_red + char, end="", flush=True)


def load_sounds() -> Dict[str, Dict[str, mixer.Sound]]:
    """Loads all sounds in the current directory.

    Returns a (random) keymap to play the sounds.

    :return: a dictionary with each key pointing to a tuple with the name of
    the file and the corresponding mixer.Sound object
    """
    sounds = [
        {"name": x, "sound": mixer.Sound(os.path.join(Soundboard.SFX_DIR, x))}
        for x in sorted(os.listdir(Soundboard.SFX_DIR))
        if x.endswith(".wav")
    ]
    keys = []
    while len(keys) < len(sounds):
        k = choice(KEYS)
        if k not in keys:
            keys.append(k)

    keymap = {k: v for k, v in zip(sorted(keys), sounds)}
    mixer.set_num_channels(len(sounds))
    return keymap


if __name__ == "__main__":
    term = Terminal()
    mixer.init()
    keymap = load_sounds()
    with term.cbreak(), term.hidden_cursor():
        # clear the screen
        print(term.home + term.clear)
        x, y = 0, 0
        sep = term.width // 6
        # Draw TUI
        for k in sorted(keymap.keys()):
            draw(x, y, f"{k}:{keymap[k]['name']}")
            x += sep
            if x > term.width - sep:
                x = 0
                y += term.height // 4
        wait_time = 0.2
        last_inp = None
        last_inp_time = 0
        inp = ""
        while True:
            try:
                inp = repr(term.inkey()).strip("'")
            except KeyboardInterrupt:
                close()
            if inp in keymap.keys() and (
                inp != last_inp or (time.time() - last_inp_time > wait_time)
            ):
                mixer.find_channel(True).play(keymap[inp]["sound"])
            last_inp = inp
            last_inp_time = time.time()
