from blessed import Terminal
from src.main import main
from src.title import Title

if __name__ == "__main__":
    intro_title = Title()
    level_code = intro_title.title()
    main(Terminal(), level_code)
