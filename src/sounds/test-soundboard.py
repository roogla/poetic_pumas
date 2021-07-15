import os

os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import sys
import time
from blessed import Terminal
from pygame import mixer
from random import choice

# adapted from https://stackoverflow.com/questions/16480898
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))
from src.soundboard import Soundboard


def close():
    """
    Closes the terminal and clears the screen
    """
    print(term.clear)
    mixer.quit()
    sys.exit(0)


def draw(x: int, y: int, char: str):
    print(term.move_xy(x, y) + term.bold_on_red + char, end="", flush=True)


if __name__ == "__main__":
    term = Terminal()
    s = Soundboard()
    with term.cbreak(), term.hidden_cursor():
        # Draw TUI
        print(term.home + term.clear)
        x, y = 0, 0
        sep = term.width // 4
        rand_sounds = {}
        for k in "wasd":
            rand_sounds.update({k: choice(s.get_loaded_sounds())})
            draw(x, y, f"{k}:{rand_sounds[k]}")
            x += sep
            if x > term.width - sep:
                x = 0
                y += term.height // 4
        # Input handler
        wait_time = 0.2
        last_inp = None
        last_inp_time = 0
        while True:
            try:
                inp = repr(term.inkey()).strip("'")
            except KeyboardInterrupt:
                close()
            if inp in "wasd" and (
                inp != last_inp or (time.time() - last_inp_time > wait_time)
            ):
                s.play_sfx(rand_sounds[inp])
            last_inp = inp
            last_inp_time = time.time()
