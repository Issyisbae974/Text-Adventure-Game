from item import Misc, Food, Combat, Heart

items = {
    # Food Items
    "steak": Food("steak"),
    "jam" : Food("Jam"),
    "fish food" : Food("Fish Food"),

    # Combat Items
    "sword": Combat("Sword"),

    # Misc Items
    "non-important key": Misc("Gate Key"),
    "metal polish" : Misc("Metal Polish"),
    "hedge trimmers" : Misc("Hedge Trimmers"),


    # Keys
    "poison heart" : Heart("Poison Heart"),
    "skeleton heart" : Heart("Skeleton Heart"),
    "fish heart" : Heart("Fish Heart"),
    "celestial key" : Heart("Celestial Key"),

    }

def build_inventory():

    player_inventory = []

    #Food Items
    items["jam"].set_description("A sealed jar with a purple substance inside.")
    items["jam"].set_hint("Something purple sits on the counter.")

    items["fish food"].set_description("Fishy flakes in a little container.")
    items["fish food"].set_hint("A fishy smell overpowers you.")

    #Combat Items
    items["sword"].set_description("A sharp blade for close combat.")
    items["sword"].set_hint("You see a glint of light in the corner of the room.")

    #Misc Items
    items["non-important key"].set_description("A shiny iron key, it looks oddly new.")
    items["non-important key"].set_hint("You notice something shiny lodged under a rock.")
    items["metal polish"].set_description("A sealed container of high quality paste.")

    items["hedge trimmers"].set_description("A rusty pair of hedge trimmers.")
    items["hedge trimmers"].set_hint("A rusty blade pokes out of the ground")

    #Keys
    items["poison heart"].set_description("A radiant and sickly green heart.")
    items["skeleton heart"].set_description("A heart which fell out of the mouth of a hungry skeleton.")
    items["fish heart"].set_description("A fishy heart.")

    return player_inventory
