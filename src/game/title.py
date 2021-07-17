from blessed import Terminal
import os
import sys


class Title:

    def __init__(self):
        self.logo = [
            "██████╗ ██╗      ██████╗  ██████╗██╗  ██╗    ██████╗ ██╗   ██╗██████╗ ███████╗\n",
            "██╔══██╗██║     ██╔═══██╗██╔════╝██║ ██╔╝    ██╔══██╗██║   ██║██╔══██╗██╔════╝\n",
            "██████╔╝██║     ██║   ██║██║     █████╔╝     ██║  ██║██║   ██║██║  ██║█████╗  \n",
            "██╔══██╗██║     ██║   ██║██║     ██╔═██╗     ██║  ██║██║   ██║██║  ██║██╔══╝  \n",
            "██████╔╝███████╗╚██████╔╝╚██████╗██║  ██╗    ██████╔╝╚██████╔╝██████╔╝███████╗\n",
            "╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝    ╚═════╝  ╚═════╝ ╚═════╝ ╚══════╝\n",
        ]
        self.menu = ["NEW", "PASSWORD", "ABOUT", "EXIT"]
        self.term = Terminal()
        self.selection = 0

    def display_logo(self):
        print(self.term.clear() + self.term.normal + ''.join(self.logo))

    def display_menu(self):
        for v in range(len(self.menu)):
            if v == self.selection:
                print(f'{self.term.bold_red_reverse}{self.menu[v]}')
            else:
                print(f'{self.term.normal}{self.menu[v]}')

    def run_selection(self, selection) -> str:
        """Navigation logic"""
        if selection == 0:
            return "level-1"
        if selection == 1:
            print(self.term.clear())
            self.display_logo()
            level_code = input(f"{self.term.white_on_black + self.term.move_xy(0, 6)}Enter level code: ")
            try:
                return level_code
            except OSError as e:
                self.title()
        if selection == 2:
            with self.term.cbreak():
                while True:
                    print(self.term.clear())
                    self.display_logo()
                    print(f"{self.term.white_on_black}PythonDiscord Summer Code Jame 2021"
                          f"\nTeam: Poetic Pumas"
                          f"\n - PhiEuler (Thomas)"
                          f"\n - Crec0 (Bawan)"
                          f"\n - Jaavv (Marc)"
                          f"\n - Darkbiscuti (Robert)"
                          f"\n - Mezzo_forte (Mike)"
                          f"\n - Castform (Brady)"
                          f"\n"
                          f"\n press enter to return to menu")
                    about_key = self.term.inkey()
                    if about_key.name == 'KEY_ENTER':
                        os.system('py blockdude.py')
        if selection == 3:
            sys.exit()

    def title(self):
        """Main navigation loop"""
        self.selection = 0
        with self.term.fullscreen():
            self.display_logo()
            self.display_menu()
            selection_in_progress = True
            with self.term.cbreak():
                while selection_in_progress:
                    keystroke = self.term.inkey()
                    if self.selection < 0:
                        self.selection = 0
                    if keystroke.is_sequence:
                        if self.selection < 3:
                            if keystroke.name == u'KEY_DOWN':
                                self.selection += 1
                            if keystroke.name == u'KEY_UP':
                                self.selection -= 1
                            if keystroke.name == u'KEY_ENTER':
                                selection_in_progress = False
                        elif self.selection == 3 and keystroke.name == u'KEY_DOWN':
                            self.selection = 0
                        elif self.selection == 3 and keystroke.name == u'KEY_ENTER':
                            selection_in_progress = False
                        elif self.selection == 3 and keystroke.name == u'KEY_UP':
                            self.selection -= 1
                    self.display_logo()
                    self.display_menu()
        return self.run_selection(self.selection)
