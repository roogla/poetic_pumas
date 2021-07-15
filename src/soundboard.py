import os
from typing import Dict, List

from pygame import mixer


class Soundboard:
    """Creates a Soundboard object which controls sounds used in the game"""

    SFX_DIR = os.path.join(".", "src", "sounds", "sfx")

    def __init__(self):
        # TODO: self.sfx, self.music =
        mixer.init()
        self.sfx = self.load_sounds()

    def load_sounds(self) -> Dict[str, mixer.Sound]:
        """Loads all sounds from the default sound directories SFX_DIR and MUSIC_DIR

        :return: a dictionary of mixer.Sound objects sorted by filename (no
        extension)
        """
        # TODO: implement music, reserve channels
        # mixer.set_reserved(0)
        sfx = {
            x[:-4]: mixer.Sound(os.path.join(self.SFX_DIR, x))
            for x in os.listdir(self.SFX_DIR)
            if x.endswith(".wav")
        }
        return sfx

    def get_loaded_sounds(self) -> List[str]:
        """Returns a list of all currently loaded sounds by filename"""
        # TODO: add music
        return list(self.sfx.keys())

    def play_sfx(self, name: str) -> None:
        """Play a file by name, (no extension)

        :param name: the name of the file in the sfx directory
        """
        mixer.find_channel(True).play(self.sfx[name])

    def quit(self) -> None:
        """Quit the soundboard mixer."""
        mixer.quit()
