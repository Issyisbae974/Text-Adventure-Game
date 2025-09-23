from character import Char, Enemy
from Map_Items import build_inventory, items

characters = {
    "knight" : Char("Knight", trade_item=items["metal polish"], give_item=items["sword"]),
    "spider" : Enemy("Spider", key_weapon=items["sword"], drop=items["poison heart"]),
    "skeleton king" : Char("Skeleton King", trade_item=items["jam"], give_item=items["skeleton heart"]),
    "fish" : Char("Fish", trade_item=items["fish food"], give_item=items["fish heart"]),
    "spirit" : Char("Spirit", trade_item=[items["fish heart"], items["skeleton heart"], items["poison heart"]], give_item=items["celestial key"])
}

knight = characters["knight"]
knight.set_dialogue("I'd love some shiny armour, I recall dropping my polish somewhere back there. . .")
knight.trade_dialogue("My armour has never looked better!")

spider = characters["spider"]
spider.set_dialogue("Hiss hiss. . .")
spider.dead_dialogue("The spider lays on its back with its legs curled. . .")

skeleton_king = characters["skeleton king"]
skeleton_king.set_dialogue("The king sits with a butter knife and a mouldy piece of bread with peanut butter in front of him. . .")
skeleton_king.trade_dialogue("The skeleton king looks oddly satisified.")

fish = characters["fish"]
fish.set_dialogue("Blub blub. . .")
fish.trade_dialogue("Blub blub. . .")

spirit = characters["spirit"]
spirit.set_dialogue("At last, my long awaited hearts")

