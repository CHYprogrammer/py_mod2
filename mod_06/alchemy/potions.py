from alchemy.elements import create_fire, create_water


def healing_potion() -> str:
    return ("Healing potion brewed with "
            f"{create_fire()} and {create_water()}")


def strength_potion() -> str:
    return ("Strength potion brewed with "
            f"{create_fire()} and {create_water()}")


def invisibility_potion() -> str:
    return ("Invisibility potion brewed with "
            f"{create_fire()} and {create_water()}")


def wisdom_potion() -> str:
    return ("Wisdom potion brewed with "
            f"{create_fire()} and {create_water()}")
