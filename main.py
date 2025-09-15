from menu import main_menu
from shortcuts import type_text, clear_screen, enter
import time
from Map_Characters import characters
from shortcuts import Color

if __name__ == "__main__":
    clear_screen()
    intro = "Welcome to Isaac's text advenutre game, here are the basic controls"\
    "\n\nThis game relies on movement between rooms by typing the compass directions or the first letter of them n, e, s, w" \
    "\n\nTo use keys, simply travel to the room which was previously locked, with the correct key in your inventory, it will open."\
    "\n\nSome items will show hints in the menu, whilst others have more cryptic clues from characters and require a search to find" \
    "\n\nYour main objective is to find all three hearts"\
    "\n\nGood luck!"
    type_text(intro, delay=0.05, color_func=Color.bright_cyan_shortcut)
    time.sleep(1)
    input(f"\nPress {enter()} to continue. . .")
    start = True
    main_menu()


            
