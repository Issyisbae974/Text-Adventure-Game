from shortcuts import Color, clear_screen, backkey, enter
from shortcuts import selected
import time
import readchar
from item import Item

class Room():
    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.searchable_items = []
        self.searchable_characters = []
        self.locked = False
        self.key_item = None
    
    def to_dict(self):
        return {
            "locked": self.locked,
            "items": [item.name for item in self.items],
            "characters": [char.name for char in self.characters]
        }
    
    def from_dict(self, data, items, characters):
        self.locked = data.get("locked", False)
        self.items = [items[name] for name in data.get("items", []) if name in items]
        self.characters = [characters[name] for name in data.get("characters", []) if name in characters]

    def add_item(self, item):
        self.searchable_items.append(item)
    
    def remove_item(self, item):
        self.searchable_items.remove(item)

    def add_char(self, char):
        self.searchable_characters.append(char)
    
    def remove_(self, char):
        self.searchable_characters.remove(char)

    def set_description(self, room_description):
         self.description = room_description
         
    def get_description(self):
        return self.description
    
    def link_room(self, room_to_link, direction):
        compliment = {
            "north": "south",
            "south": "north",
            "east": "west",
            "west": "east",
        }
        room_to_link.linked_rooms[compliment[direction]] = self
        self.linked_rooms[direction] = room_to_link

    def describe(self):
        Color.bright_magenta(f'{self.name.upper()}:')
        print("-" * 20)
        Color.magenta(self.description)
        print("\n")

    def move(self, direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way.")
            return self
    
    def required_key(self, key_item):
        self.key_item = key_item

def show_directions(current_room):
    Color.bright_blue("AVAILABLE DIRECTIONS:")
    print('-' * 20)
    direction_order = ["north", "east", "south", "west"]
    direction_lookup = {}
    for direction_name in direction_order:
        if direction_name in current_room.linked_rooms:
            Color.blue(f"{direction_name.capitalize()} - {current_room.linked_rooms[direction_name].name}")
            direction_lookup[direction_name[0].lower()] = direction_name.lower()
    return direction_lookup

def show_hint(current_room):
    for item in current_room.searchable_items:
        if item.get_hint() is None:
            pass
        else:
            print("\n")
            print(f"* {item.classcolor()(item.get_hint())} *")
            break
 

def search_room(current_room, player_inventory):
    if not current_room.searchable_items:
        clear_screen()
        Color.yellow("Nothing useful here. . .")
        time.sleep(1)
        input(f"\nPress {enter()} to continue. . .")
        clear_screen()
        return
    selectedindex = 0

    while True:
        if current_room.searchable_items:
            clear_screen()
            Color.bright_yellow("YOU FOUND:")
            print("-" * 20)
            for n, item in enumerate (current_room.searchable_items):
                if n == selectedindex:
                    selected_text = selected(Color.bright_yellow_shortcut(f"[{n + 1}] {item.classcolor()(item.name)} ~ {item.get_description()}"))
                    print(selected_text)
                else:
                    Color.yellow(f"[{n+1}] {item.classcolor()(item.name)} ~ {item.get_description()}")
            print(f"\nUse arrow keys or numbers to navigate, and press {enter()} to pick up an item\nPress {Color.bright_yellow_shortcut("'Q'")} to go back. . .")

            key = readchar.readkey()
            if key == readchar.key.UP:
                selectedindex = (selectedindex - 1) % len(current_room.searchable_items)
            elif key == readchar.key.DOWN:
                selectedindex = (selectedindex + 1) % len(current_room.searchable_items)
            elif key.isdigit() and int(key) in range(1, len(current_room.searchable_items) + 1):
                selectedindex = int(key) - 1
            elif key == readchar.key.ENTER:
                clear_screen()
                print(f"You picked up {current_room.searchable_items[selectedindex].classcolor()(current_room.searchable_items[selectedindex].name)}.\n")
                player_inventory.append(current_room.searchable_items[selectedindex])
                current_room.remove_item(current_room.searchable_items[selectedindex])
                selectedindex = 0
                input(f"Press {enter()} to return. . .")
            elif key == 'q':
                clear_screen()
                break
        else:
            if not current_room.searchable_items:
                clear_screen()
                break




def add_items_to_room(room, item_names, items_dict):
    room.searchable_items.extend([items_dict[name] for name in item_names])

def add_characters_to_room(room, character_names, character_dict):
    room.searchable_characters.extend([character_dict[name] for name in character_names])

def lock_room(room):
    room.locked = True

def unlock_room(room):
    room.locked = False

def room_key(room, key_item, player_inventory):
    if key_item in player_inventory:
        unlock_room(room)
        player_inventory.remove(key_item)
        return True
    else:
        return False

def lock_check(current_room, direction, player_inventory):
        next_room = current_room.linked_rooms.get(direction)
        if next_room is None:
            Color.bright_red("You can't go that way.")
            return current_room

        if next_room.locked:
            if room_key(next_room, next_room.required_key, player_inventory) == True:
                    clear_screen()
                    Color.bright_green("You unlocked the door with the correct key!")
                    time.sleep(1)
                    current_room.linked_rooms[direction].locked = False
                    return next_room
            else:
                clear_screen()
                Color.bright_red("This room is locked. Try looking around for items that might help.")
                time.sleep(1)
                input(f"\nPress {enter()} to return. . .")
                return current_room
        else:
            return next_room

def show_characters(current_room):
    if current_room.searchable_characters:
        for char in current_room.searchable_characters:
            if char.dead == True:
                print('\n\n* ' + f"There is a dead {char.classcolor()(char.name).lower()} in the room!" + ' *')
            elif char.traded == True:
                print('\n\n* ' + f"There is a happy {char.classcolor()(char.name).lower()} in the room!" + ' *')
            else:
                print('\n\n* ' + f"There is a {char.classcolor()(char.name).lower()} in the room!" + ' *')

if __name__ == "__main__":
    kitchen = Room("Kitchen")
    kitchen.set_description("A place to cook and eat.")

    dining = Room("Dining Room")
    dining.set_description("A room with a large table.")

    kitchen.link_room(dining, "east")

    current_room = kitchen

