import time

from blessed import Terminal

term = Terminal()

# Necessary when running with Docker
# Docker's terminal defaults to 8 colors
term.number_of_colors = 1 << 24


def draw_background(term: Terminal):
    for i in range(30):
        with term.location(i, i):
            print("x")


with term.cbreak(), term.hidden_cursor():
    i = 0
    print(term.home + term.clear)
    draw_background(term)
    while True:
        time.sleep(0.10)
        i += 1
        # draw_background(term)
        print(term.move_xy(i + 2, i + 4) + "hi")
