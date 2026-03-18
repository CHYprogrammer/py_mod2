from abc import ABC, abstractmethod
from typing import Dict


class Card(ABC):
    def __init__(self, name: str, cost: int, rarity: str) -> None:
        self._name = name
        self._cost = cost
        self._rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        pass

    def get_card_info(self) -> Dict:
        return {
            'name': self._name,
            'cost': self._cost,
            'rarity': self._rarity,
        }

    def is_playable(self, available_mana: int) -> bool:
        return available_mana >= self._cost
