import os
from typing import Dict, List

from pygame import mixer


class Soundboard:
    """Creates a Soundboard object which controls sounds used in the game"""

    SFX_DIR = os.path.join(".", "src", "sounds", "sfx")
    MUSIC_DIR = os.path.join(".", "src", "sounds", "music")

    def __init__(self):
        mixer.init()
        self.sfx, self.music = self.load_sounds()
        self.play_music("blockdude")

    def __del__(self):
        """Quit the soundboard mixer."""
        mixer.quit()

    def load_sounds(self) -> Dict[str, mixer.Sound]:
        """Loads all sounds from the default sound directories SFX_DIR and MUSIC_DIR

        :return: a dictionary of mixer.Sound objects sorted by filename (no
        extension)
        """
        # reserves one channel, does not reserve channel 1
        mixer.set_reserved(1)
        sfx = {
            x[:-4]: mixer.Sound(os.path.join(self.SFX_DIR, x))
            for x in os.listdir(self.SFX_DIR)
            if x.endswith(".wav")
        }
        music = {
            x[:-4]: mixer.Sound(os.path.join(self.MUSIC_DIR, x))
            for x in os.listdir(self.MUSIC_DIR)
            if x.endswith(".wav")
        }
        return sfx, music

    def get_loaded_sounds(self) -> List[str]:
        """Returns a list of all currently loaded sounds by filename"""
        return list(self.sfx.keys()) + list(self.music.keys())

    def play_sfx(self, name: str) -> None:
        """Play a file by name, (no extension)

        :param name: the name of the file in the sfx directory
        """
        mixer.find_channel(True).play(self.sfx[name])

    def play_music(self, name: str) -> None:
        """Play a file by name, (no extension), and loop it

        :param name: the name of the file in the sfx directory
        """
        mixer.Channel(0).play(self.music[name], loops=-1)
