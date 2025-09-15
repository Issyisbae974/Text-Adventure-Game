from shortcuts import Color, clear_screen, backspace, enter, selected, backkey
import time
import readchar




class Item():
    def __init__(self, item_name):
        self.name = item_name
        self.description = None
        self.hint = None

    def to_dict(self):
        return {"name": self.name, "description": self.description, "hint": self.hint}

    def from_dict(self, data):
        self.description = data.get("description", "")
        self.hint = data.get("hint", None)

    def set_description(self, item_description):
        self.description = item_description

    def get_description(self):
        return self.description
    
    def set_hint(self, item_hint):
        self.hint = item_hint
    
    def get_hint(self):
        return self.hint
        

    def inventory_add(self, inventory):
        inventory.append(self) 

    def classcolor(self):
        return Color.bright_cyan_shortcut

class Combat(Item):

    def __init__(self, item_name):
        super().__init__(item_name)

    def classcolor(self):
        return Color.bright_red_shortcut

class Food(Item):

    def classcolor(self):
        return Color.bright_magenta_shortcut

    def __init__(self, item_name):
        super().__init__(item_name)

class Misc(Item):
    def __init__(self, item_name):
        super().__init__(item_name)

class Heart(Item):
    def __init__(self, item_name):
        super().__init__(item_name)

    def classcolor(self):
        return Color.bright_white_shortcut



def open_inventory(player_inventory):
    player_inventory.sort(key=lambda item: (item.__class__.__name__, item.name))
    selectedindex = 0
    while True:
        if len(player_inventory) > 0:

            clear_screen()
            Color.bright_green("YOUR INVENTORY:")
            print("-" * 20)
        
            
            for n, item in enumerate(player_inventory):
                    if n == selectedindex:
                       selected_text = selected(Color.bright_green_shortcut(f"[{n + 1}] {player_inventory[n].classcolor()(player_inventory[n].name)}"))
                       print(selected_text)
                    else:
                        Color.green(f" [{n + 1}] {player_inventory[n].classcolor()(player_inventory[n].name)}")
            print(f"\nUse arrow keys or numbers to navigate \nPress {enter()} to select an item or {Color.bright_green_shortcut("'I'")} to go back. . .")

            key = readchar.readkey()
            if key == readchar.key.UP:
                selectedindex = (selectedindex - 1) % len(player_inventory)
            elif key == readchar.key.DOWN:
                selectedindex = (selectedindex + 1) % len(player_inventory)
            elif key == readchar.key.ENTER:
                clear_screen()
                print(f"{player_inventory[selectedindex].classcolor()(player_inventory[selectedindex].name)} is a {player_inventory[selectedindex].classcolor()(player_inventory[selectedindex].__class__.__name__).lower()} item.\n")
                print(f"~ {player_inventory[selectedindex].get_description()}\n")
                print(f"Press {enter()} to go back. . .")
                while True:
                    key = readchar.readkey()
                    if key == readchar.key.ENTER:
                        break
                    else:
                        continue
            elif key == "i":
                clear_screen()
                break
            elif key.isdigit() and int(key) in range(1, len(player_inventory) + 1):
                selectedindex = int(key) - 1
            else:
                continue
            

        else:
            clear_screen()
            Color.bright_red("Your inventory is empty!")
            time.sleep(1)
            break