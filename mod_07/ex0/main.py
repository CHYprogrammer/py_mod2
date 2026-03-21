from ex0.CreatureCard import CreatureCard


def main() -> None:
    print("\n=== DataDeck Card Foundation ===")
    print()
    print("Testing Abstract Base Class Design:")
    print()

    dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    print("CreatureCard Info:")
    print(dragon.get_card_info())
    print()

    game_state = {'turn': 1, 'player': 'Alice'}
    mana = 6
    print(f"Playing {dragon.name} with {mana} mana available:")
    print(f"Playable: {dragon.is_playable(mana)}")
    print(f"Play result: {dragon.play(game_state)}")
    print()

    print(f"{dragon.name} attacks Goblin Warrior:")
    print(f"Attack result: {dragon.attack_target('Goblin Warrior')}")
    print()

    print("Testing insufficient mana (3 available):")
    print(f"Playable: {dragon.is_playable(3)}")
    print()
    print("Abstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
