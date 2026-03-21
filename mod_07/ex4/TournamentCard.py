from typing import Dict
from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    _BASE_RATING = 1200
    _K_FACTOR = 32

    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        attack: int,
        defense: int,
    ) -> None:
        Card.__init__(self, name, cost, rarity)
        self.atk = attack
        self.defense = defense
        self._wins = 0
        self._losses = 0
        self._rating = self._BASE_RATING + (attack - defense) * 10

    def play(self, game_state: dict) -> dict:
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Tournament card deployed',
        }

    def get_card_info(self) -> Dict:
        info = super().get_card_info()
        info['type'] = 'Tournament'
        info['attack'] = self.atk
        info['defense'] = self.defense
        return info

    def attack(self, target) -> dict:
        target_name = target if isinstance(target, str) else target.name
        return {
            'attacker': self.name,
            'target': target_name,
            'damage': self.atk,
        }

    def defend(self, incoming_damage: int) -> dict:
        blocked = min(incoming_damage, self.defense)
        taken = incoming_damage - blocked
        return {
            'defender': self.name,
            'damage_taken': taken,
            'damage_blocked': blocked,
            'still_alive': taken < 20,
        }

    def get_combat_stats(self) -> Dict:
        return {'attack': self.atk, 'defense': self.defense}

    def calculate_rating(self) -> int:
        return self._rating

    def update_wins(self, wins: int) -> None:
        self._wins += wins
        self._rating += int(self._K_FACTOR * wins * 0.5)

    def update_losses(self, losses: int) -> None:
        self._losses += losses
        self._rating = max(
            100, self._rating - int(self._K_FACTOR * losses * 0.5)
        )

    def get_rank_info(self) -> Dict:
        return {
            'name': self.name,
            'rating': self._rating,
            'wins': self._wins,
            'losses': self._losses,
            'record': f"{self._wins}-{self._losses}",
        }

    def get_tournament_stats(self) -> Dict:
        stats = self.get_card_info()
        stats.update(self.get_rank_info())
        stats['interfaces'] = ['Card', 'Combatable', 'Rankable']
        return stats