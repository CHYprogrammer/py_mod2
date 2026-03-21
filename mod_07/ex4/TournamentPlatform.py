import random
from ex4.TournamentCard import TournamentCard


class TournamentPlatform:
    def __init__(self) -> None:
        self._cards: dict[str, TournamentCard] = {}
        self._matches_played: int = 0

    def register_card(self, card: TournamentCard) -> str:
        if not isinstance(card, TournamentCard):
            raise TypeError("Only TournamentCard instances can be registered.")
        card_id = f"{card.name.lower().replace(' ', '_')}_001"
        base_id = card_id[:-4]
        counter = 1
        while card_id in self._cards:
            counter += 1
            card_id = f"{base_id}_{counter:03d}"
        self._cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        if card1_id not in self._cards:
            raise ValueError(f"Card ID '{card1_id}' not registered.")
        if card2_id not in self._cards:
            raise ValueError(f"Card ID '{card2_id}' not registered.")

        c1 = self._cards[card1_id]
        c2 = self._cards[card2_id]

        score1 = c1.atk + random.uniform(0, 1)
        score2 = c2.atk + random.uniform(0, 1)

        if score1 >= score2:
            winner_id, loser_id = card1_id, card2_id
            winner, loser = c1, c2
        else:
            winner_id, loser_id = card2_id, card1_id
            winner, loser = c2, c1

        winner.update_wins(1)
        loser.update_losses(1)
        self._matches_played += 1

        return {
            'winner': winner_id,
            'loser': loser_id,
            'winner_rating': winner.calculate_rating(),
            'loser_rating': loser.calculate_rating(),
        }

    def get_leaderboard(self) -> list[dict]:
        entries = []
        for card_id, card in self._cards.items():
            info = card.get_rank_info()
            info['id'] = card_id
            entries.append(info)
        return sorted(entries, key=lambda e: e['rating'], reverse=True)

    def generate_tournament_report(self) -> dict:
        total = len(self._cards)
        avg_rating = (
            sum(c.calculate_rating() for c in self._cards.values()) // total
            if total > 0 else 0
        )
        return {
            'total_cards': total,
            'matches_played': self._matches_played,
            'avg_rating': avg_rating,
            'platform_status': 'active',
        }
