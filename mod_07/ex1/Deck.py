from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
import random
from typing import Optional


class Deck:
    def __init__(self) -> None:
        self._cards = []

    def add_card(self, card: Card) -> None:
        if not isinstance(card, Card):
            raise TypeError("Only Card instances can be added to the deck.")
        self._cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        for i, card in enumerate(self._cards):
            if card.name == card_name:
                self._cards.pop(i)
                return True
        return False

    def shuffle(self) -> None:
        random.shuffle(self._cards)

    def draw_card(self) -> Optional[Card]:
        if not self._cards:
            return None
        return self._cards.pop(0)

    def get_deck_stats(self) -> dict:
        creatures = [1 for c in self._cards if isinstance(c, CreatureCard)]
        spells = [1 for c in self._cards if isinstance(c, SpellCard)]
        artifacts = [1 for c in self._cards if isinstance(c, ArtifactCard)]
        total = len(self._cards)
        avg_cost = sum(c.cost for c in self._cards) / total if total > 0 else 0.0
        return {
            'total_cards': total,
            'creatures': len(creatures),
            'spells': len(spells),
            'artifacts': len(artifacts),
            'avg_cost': round(avg_cost, 1)
        }
