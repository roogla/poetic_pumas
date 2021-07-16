from blessed import Terminal


class Title():

    def __init__(self):
        self.logo = """
██████╗ ██╗      ██████╗  ██████╗██╗  ██╗    ██████╗ ██╗   ██╗██████╗ ███████╗
██╔══██╗██║     ██╔═══██╗██╔════╝██║ ██╔╝    ██╔══██╗██║   ██║██╔══██╗██╔════╝
██████╔╝██║     ██║   ██║██║     █████╔╝     ██║  ██║██║   ██║██║  ██║█████╗  
██╔══██╗██║     ██║   ██║██║     ██╔═██╗     ██║  ██║██║   ██║██║  ██║██╔══╝  
██████╔╝███████╗╚██████╔╝╚██████╗██║  ██╗    ██████╔╝╚██████╔╝██████╔╝███████╗
╚═════╝ ╚══════╝ ╚═════╝  ╚═════╝╚═╝  ╚═╝    ╚═════╝  ╚═════╝ ╚═════╝ ╚══════╝
"""
        self.menu = [["NEW"], ["PASSWORD"], ["ABOUT"], ["EXIT"]]
        self.term = Terminal()
        self.selection = 0

    def display_screen(self, selection):
        print(self.term.clear())
        print(self.logo)
        for k, v in enumerate(self.menu):
            if k == selection:
                print(f'{self.term.bold_red_reverse}{v[0]}')
            else:
                print(f'{self.term.normal}{v[0]}')

    def run_selection(self, selection) -> str:
        if selection == 0:
            return "level-1"
        if selection == 1:
            print(self.term.clear())
            print(self.logo)
            level_code = input(f"{self.term.white_on_black + self.term.move_xy(0, 10)}Enter level code: ")
            return level_code
        if selection == 2:
            with self.term.cbreak():
                while True:
                    print(self.term.clear())
                    print(self.logo)
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
                        print(self.term.clear())
                        self.title()
        if selection == 3:
            quit()

    def title(self):
        self.selection = 0
        with self.term.fullscreen():
            self.display_screen(self.selection)
            selection_in_progress = True
            with self.term.cbreak():
                while selection_in_progress:
                    key = self.term.inkey()
                    if key.is_sequence:
                        if key.name == 'KEY_DOWN':
                            self.selection += 1
                        if key.name == 'KEY_UP':
                            self.selection -= 1
                        if key.name == 'KEY_ENTER':
                            selection_in_progress = False
                    elif key:
                        print(f'Got {key}')

                    self.display_screen(self.selection)
        return self.run_selection(self.selection)