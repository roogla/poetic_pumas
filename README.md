# Python Discord 2021 Summer Code Jam 8 - Team Poetic Pumas
## Blockdude Returns!
From the TI-83/84 you abandoned somewhere in your room after college,
<b>Blockdude</b> is back and better than ever, now with a sleek new Unicode
look, extensible levels, new powers and more--all on your favorite terminal
emulator!

### Compatibility
Note that this game heavily uses modern Unicode (particularly emojis)
so your terminal may not be able to render them out of the box, or at all.
On some Linux flavors (like Debian or older Ubuntu versions), you may need to
install the following font to get started:
```bash
sudo apt install fonts-noto-color-emoji
```

We have tested our game runs well on the following emulators:

- [Powershell](https://docs.microsoft.com/en-us/powershell/)
- [Terminator](https://github.com/gnome-terminator/terminator)
- [Gnome Terminal](https://help.gnome.org/users/gnome-terminal/stable/)
- [Xfce Terminal](https://xfce.org/)

Our game may also work on the following with patches or alternate fonts, but we
have not tested them

- [st](suckless.org/st) - may be possible with a patch, see
[here](https://wiki.archlinux.org/title/St#Crashes_if_page_contains_emoji_characters)

The game unfortunately does not yet run without a display server like X, but we
are hoping to add compatibility for more! We would also like to add options to
disable sound for such systems; note that sound currently works best
with headphones and you might get lagged sound on some monitors.

## Installation (w/ Docker)
```ps
$ git clone https://github.com/roogla/poetic_pumas.git
$ cd poetic_pumas
$ docker build -t "cj8-poetic-pumas" .
```

### Running in Docker
```ps
$ docker run -it "cj8-poetic-pumas"
```

## Installing from source (no Docker)
You must have [Python 3.9](https://www.python.org/downloads/release/python-396/)
installed and [pip](https://bootstrap.pypa.io/get-pip.py).
```ps
$ git clone https://github.com/roogla/poetic_pumas.git
$ cd poetic_pumas
$ pip install -r requirements.txt
$ python blockdude.py
```
You can also use a virtual environment prior to installing to avoid installing
the dependencies globally:
```ps
$ python -m venv env
$ source ./env/bin/activate
```

On some flavors of Linux, python3.9 might not be default and should be
installed separately:
```bash
$ sudo apt install python3.9 python3.9-venv
```
Replace "python" in the above commands with "python3.9"


## Roadmap/Help wanted
- Improve sounds and text graphics
- Wider terminal and character support
- Build new mechanics and expand the telekinesis mechanic
- Create music per level to mix things up
- More levels!
- Add timer support to challenge your friends
- Port to new platforms. Termux? A calculator? A teletype?
