from shortcuts import Color, enter, selected, clear_screen, type_text
from item import Item, Combat, Misc, Food
import time
import readchar
class Char():
    def __init__(self, char_name, trade_item=None, give_item=None):
        self.name = char_name
        self.description = None
        self.text = None
        self.killitem = None
        self.dead = False
        self.key_weapon = None
        self.drop = None
        self.actions = {"speak": self.speak}
        if trade_item and give_item:
            self.tradeitem = trade_item
            self.giveitem = give_item
            self.actions["trade"] = self.trade

        self.dialogue = None
        self.deaddialogue = None
        self.tradedialogue = None
        self.tradeitem = trade_item
        self.traded = False

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "dead": self.dead,
            "key_weapon": self.key_weapon.name if self.key_weapon else None
        }

    def from_dict(self, data, items):
        self.description = data.get("description", "")
        self.dead = data.get("dead", False)
        weapon_name = data.get("key_weapon", None)
        if weapon_name and weapon_name in items:
            self.key_weapon = items[weapon_name]
    
    def classcolor(self):
        return Color.bright_cyan_shortcut
    
    def set_dialogue(self, dialogue):
        self.dialogue = dialogue
    
    def dead_dialogue(self, dialogue):
        self.deaddialogue = dialogue
    
    def trade_dialogue(self, dialogue):
        self.tradedialogue = dialogue

    def speak(self):
        if self.traded == True:
            clear_screen()
            type_text(self.tradedialogue, delay=0.05, color_func=self.classcolor())
        elif self.dead == True:
            clear_screen()
            type_text(self.deaddialogue, delay=0.05, color_func=self.classcolor())
        else:
            clear_screen()
            type_text(self.dialogue, delay=0.05, color_func=self.classcolor())


    def trade_item(self, trade_item):
        self.tradeitem = trade_item
    
    def give_item(self, give_item):
        self.giveitem = give_item

    def trade(self, player_inventory):
    # Ensure tradeitem is always a list
        trade_items = self.tradeitem
        if not isinstance(trade_items, list):
            trade_items = [trade_items]

        if trade_action(self, player_inventory):
            traded_names = ", ".join(item.classcolor()(item.name) for item in trade_items)
            print(f"You traded your {traded_names} for a {self.giveitem.classcolor()(self.giveitem.name)}!")
            self.traded = True
            time.sleep(1)
        else:
            Color.bright_red(f"Looks like you don't have the required item/s to trade with {self.name}.")
            time.sleep(1)

    def actions(self):
        return {
            "speak": self.speak,
            "trade": self.trade
        }

class Enemy(Char):
    def __init__(self, char_name, key_weapon=None, drop=None):
        super().__init__(char_name)
        self.key_weapon = key_weapon
        self.drop = drop
        self.actions["fight"] = self.fight
        self.actions.pop("trade", None)

    def set_key_weapon(self, weapon):
        self.key_weapon = weapon

    def classcolor(self):
        return Color.bright_red_shortcut
    
    def fight(self, current_room, player_inventory):
        fight_check(self, current_room, player_inventory)
        
def kill(enemy):
    enemy.dead = True

def fight_key(enemy, key_weapon, player_inventory):
    if key_weapon in player_inventory:
        kill(enemy)
        player_inventory.remove(key_weapon)
        return True
    return False
    
def weapon_search(current_room):
        for char in current_room.searchable_characters:
            if hasattr(char, "key_weapon") and char.key_weapon is not None:
                return char.key_weapon.name
            return None

def trade_action(character, player_inventory):
    trade_items = character.tradeitem
    if not isinstance(trade_items, list):
        trade_items = [trade_items]

    if all(item in player_inventory for item in trade_items):
        for item in trade_items:
            player_inventory.remove(item)
        player_inventory.append(character.giveitem)
        return True
    return False

        
def fight_check(enemy, current_room, player_inventory):
    if isinstance(enemy, Enemy):
        clear_screen()
        if enemy.key_weapon in player_inventory:
            Color.bright_green(
                f"You killed the {enemy.name} with your {enemy.key_weapon.name}!"
            )
            time.sleep(1)
            print(f"\nYou got a {enemy.drop.classcolor()(enemy.drop.name)}!")
            player_inventory.remove(enemy.key_weapon)
            time.sleep(1)
            kill(enemy)
            player_inventory.append(enemy.drop)
        elif enemy.key_weapon == None:
            Color.bright_green(
                f"You killed the {enemy.name} with your bare fists!"
            )
            time.sleep(1)
            print(f"\nYou got a {enemy.drop.classcolor()(enemy.drop.name)}!")
            time.sleep(1)
            kill(enemy)
            player_inventory.append(enemy.drop)
        else:
            weapon_name = enemy.key_weapon if enemy.key_weapon else "weapon"
            Color.bright_red(
                f"You were defeated in battle. Try to find a weapon to fight the {enemy.name}")
            time.sleep(1)
            return "lose"


def open_actions(character, current_room, player_inventory):
    actions = list(character.actions.keys())
    selectedindex = 0
    
    while True:
        if actions:
            clear_screen()
            Color.bright_white(f"{character.name}:")
            print("-" * 20)

            for n, action in enumerate(actions):
                if n == selectedindex:
                    selected_text = selected(Color.bright_white_shortcut(f"[{n + 1}] {Color.green_shortcut(action.capitalize())}"))
                    print(selected_text)
                else:
                    Color.white(f"[{n + 1}] {Color.green_shortcut(action.capitalize())}")

            print(f"\nUse arrow keys or numbers to navigate \nPress {enter()} to select an interaction or {Color.bright_green_shortcut("'T'")} to go back. . .")

            key = readchar.readkey()
            if key == readchar.key.UP:
                selectedindex = (selectedindex - 1) % len(actions)
            elif key == readchar.key.DOWN:
                selectedindex = (selectedindex + 1) % len(actions)
            elif key == readchar.key.ENTER:
                action_name = actions[selectedindex]
                clear_screen()
                if action_name == "fight":
                    character.actions[action_name](current_room, player_inventory)
                    if character.dead:
                            character.actions.pop("fight", None)
                    actions = list(character.actions.keys())
                    selectedindex %= len(actions)
                elif action_name == "trade":
                    character.actions[action_name](player_inventory)
                    if character.traded:
                        character.actions.pop("trade", None)
                    actions = list(character.actions.keys())
                    selectedindex %= len(actions)
                else:
                    character.actions[action_name]() 
                print(f"\nPress {enter()} to return to actions. . .")
                while True:
                    key = readchar.readkey()
                    if key == readchar.key.ENTER:
                        break

            elif key.lower() == "t":
                clear_screen()
                break
            elif key.isdigit() and int(key) in range(1, len(actions) + 1):
                selectedindex = int(key) - 1
            else:
                continue
        else:
            clear_screen()
            Color.bright_red(f"{character.name} has no actions available!")
            time.sleep(1)
            break