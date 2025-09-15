from room import show_directions, search_room, show_hint, lock_check, show_characters
from item import open_inventory
import time
from Map_Rooms import build_map
from Map_Items import build_inventory, items
from character import fight_check, open_actions
from shortcuts import Color, clear_screen, type_text, enter
from colorama import Fore, Style
from rpginfo import introduction
from Map_Characters import characters

def keycheck(player_inventory):
    required_keys = [
        items["skeleton heart"],
        items["fish heart"],
        items["poison heart"]
    ]
    # returns True only if every key is in the inventory
    return all(key in player_inventory for key in required_keys)


def main_menu():

    clear_screen()
    current_room = build_map()
    player_inventory = build_inventory()


    while True:
        clear_screen()
        current_room.describe()
        direction_lookup = show_directions(current_room)
        show_hint(current_room)
        show_characters(current_room)

        print("\n")
        direction = input(f"Which direction would you like to go? \nType {Color.bright_green_shortcut("'I'")} for inventory, {Color.bright_yellow_shortcut("'Q'")} for search room, {Color.bright_white_shortcut("'T'")} to interact with a character or {Color.bright_red_shortcut("'exit'")} to quit.\n>> ").strip().lower()
        
        if direction.lower() == "exit":
            print("Exiting game. . .")
            time.sleep(1)
            clear_screen()
            break
        if direction in current_room.linked_rooms:
            current_room = lock_check(current_room, direction, player_inventory)
            clear_screen()
        elif direction in direction_lookup:
            mapped_dir = direction_lookup[direction]
            current_room = lock_check(current_room, mapped_dir, player_inventory)
            clear_screen()
        elif direction == "i":
            open_inventory(player_inventory)
        elif direction == "q":
            search_room(current_room, player_inventory)
        elif direction == "t":
            if current_room.searchable_characters:
                for char in current_room.searchable_characters:
                    open_actions(char, current_room, player_inventory)
            else:
                clear_screen()
                Color.bright_red("There are no characters here to interact with!")
                time.sleep(1)
                input(f"\nPress {enter()} to continue. . .")
        else: 
            clear_screen()
            Color.bright_red("Invalid direction! Please try again.")
            time.sleep(1)
            clear_screen()

        if keycheck(player_inventory) == True:
            Color.bright_green("You beat the game!")
            time.sleep(5)
            break

if __name__ == "__main__":
    main_menu()
