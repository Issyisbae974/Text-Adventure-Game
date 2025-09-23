from room import Room, add_items_to_room, lock_room, add_characters_to_room
from Map_Items import build_inventory, items
from Map_Characters import characters

def build_map():
    player_inventory = build_inventory()

    path = Room("Path")
    path.set_description("A dirt path leading to a large estate.")
    add_items_to_room(path, ["non-important key"], items)

    gate = Room("Front Gate")
    gate.set_description("A tall and twsited iron gate, it looks old but sturdy.")
    add_items_to_room(gate, ["metal polish"], items)

    hallway = Room("Hallway")
    hallway.set_description("A dark and candlelit entrance.")
    add_characters_to_room(hallway, ["knight"], characters)
    hallway.required_key = items["non-important key"]
    hallway.locked = True

    kitchen = Room("Kitchen")
    kitchen.set_description("An old and cobweb ridden kitchen.")
    add_characters_to_room(kitchen, ["spider"], characters)
    add_items_to_room(kitchen, ["jam"], items)

    dining_room = Room("Dining Room")
    dining_room.set_description("A dark room with a table, skeletons are on each seat.")
    add_characters_to_room(dining_room, ["skeleton king"], characters)

    backyard = Room("Backyard")
    backyard.set_description("An overgrown and deserted lawn")

    shed = Room("Shed")
    shed.set_description("A pitch black shed.")
    shed.required_key = items["hedge trimmers"]
    add_items_to_room(shed, ["fish food"], items)
    shed.locked = True

    fountain = Room("Fountain")
    fountain.set_description("An ornate iron fountain")
    add_characters_to_room(fountain, ["fish"], characters)
    add_items_to_room(fountain, ["hedge trimmers"], items)

    final_corridor = Room("Final Corridor")
    final_corridor.set_description("An etheral and glowing white room")
    add_characters_to_room(final_corridor, ["spirit"], characters)

    #build the map area
    path.link_room(gate, "north")

    gate.link_room(hallway, "north")

    hallway.link_room(kitchen, "west")

    kitchen.link_room(dining_room, "north")

    hallway.link_room(backyard, "north")

    dining_room.link_room(backyard, "east")
    
    backyard.link_room(shed, "north")

    backyard.link_room(fountain, "east")

    #dict
    rooms = {
        "path": path,
        "gate": gate,
        "hallway": hallway,
        "kitchen": kitchen,
        "dining_room": dining_room,
        "backyard": backyard,
        "shed": shed,
        "fountain": fountain,
        "final corridor": final_corridor
    }
    return path, rooms
