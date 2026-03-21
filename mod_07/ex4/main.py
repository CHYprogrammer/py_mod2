from ex4.TournamentCard import TournamentCard
from ex4.TournamentPlatform import TournamentPlatform


def main() -> None:
    print("\n=== DataDeck Tournament Platform ===")
    print()

    platform = TournamentPlatform()

    dragon = TournamentCard("Fire Dragon", 5, "Legendary", 7, 4)
    wizard = TournamentCard("Ice Wizard", 4, "Epic", 5, 6)

    print("Registering Tournament Cards...\n")
    dragon_id = platform.register_card(dragon)
    wizard_id = platform.register_card(wizard)

    for card_id, card in [(dragon_id, dragon), (wizard_id, wizard)]:
        info = card.get_rank_info()
        print(f"{card.name} (ID: {card_id}):")
        print(f"- Interfaces: {['Card', 'Combatable', 'Rankable']}")
        print(f"- Rating: {info['rating']}")
        print(f"- Record: {info['record']}")
        print()

    print("Creating tournament match...")
    result = platform.create_match(dragon_id, wizard_id)
    print(f"Match result: {result}")
    print()

    print("Tournament Leaderboard:")
    for rank, entry in enumerate(platform.get_leaderboard(), start=1):
        print(
            f"{rank}. {entry['name']} - "
            f"Rating: {entry['rating']} "
            f"({entry['record']})"
        )
    print()

    print("Platform Report:")
    print(platform.generate_tournament_report())
    print()
    print("=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()