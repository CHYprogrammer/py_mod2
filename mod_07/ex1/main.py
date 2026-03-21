from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck


def main() -> None:
    print("\n=== DataDeck Deck Builder ===")
    print()
    print("Building deck with different card types...")

    deck = Deck()
    dragon = CreatureCard("Fire Dragon", 5, "Rare", 7, 5)
    bolt = SpellCard("Lightning Bolt", 3, "Common", "damage")
    crystal = ArtifactCard("Mana Crystal", 2, "Uncommon",
                           5, "+1 mana per turn")

    deck.add_card(dragon)
    deck.add_card(bolt)
    deck.add_card(crystal)

    print(f"Deck stats: {deck.get_deck_stats()}")
    print()
    print("Drawing and playing cards:")

    game_state = {'turn': 1}

    card = deck.draw_card()
    card_type = type(card).__name__.replace('Card', '')
    print(f"Drew: {card.name} ({card_type})")
    print(f"Play result: {card.play(game_state)}")
    print()

    card = deck.draw_card()
    card_type = type(card).__name__.replace('Card', '')
    print(f"Drew: {card.name} ({card_type})")
    print(f"Play result: {card.play(game_state)}")
    print()

    card = deck.draw_card()
    card_type = type(card).__name__.replace('Card', '')
    print(f"Drew: {card.name} ({card_type})")
    print(f"Play result: {card.play(game_state)}")
    print()

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
