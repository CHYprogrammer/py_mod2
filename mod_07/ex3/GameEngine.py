from ex3.CardFactory import CardFactory
from ex3.GameStrategy import GameStrategy
from typing import Optional


class GameEngine:
    def __init__(self) -> None:
        self._factory: Optional[CardFactory] = None
        self._strategy: Optional[GameStrategy] = None
        self._hand: list = []
        self._battlefield: list = []
        self._turns_simulated: int = 0
        self._total_damage: int = 0
        self._cards_created: int = 0

    def configure_engine(
        self, factory: CardFactory, strategy: GameStrategy
    ) -> None:
        self._factory = factory
        self._strategy = strategy
        # Generate initial hand of 3 cards
        self._hand = [
            self._factory.create_creature(),
            self._factory.create_spell(),
            self._factory.create_creature(),
        ]
        self._cards_created = len(self._hand)

    def simulate_turn(self) -> dict:
        if self._factory is None or self._strategy is None:
            raise RuntimeError(
                "Engine not configured. Call configure_engine() first."
            )

        hand_summary = ', '.join(
            f"{c.name} ({c.cost})" for c in self._hand
        )

        actions = self._strategy.execute_turn(self._hand, self._battlefield)

        played_names = set(actions.get('cards_played', []))
        self._hand = [c for c in self._hand if c.name not in played_names]

        self._turns_simulated += 1
        self._total_damage += actions.get('damage_dealt', 0)

        return {
            'hand': hand_summary,
            'strategy': self._strategy.get_strategy_name(),
            'actions': actions,
        }

    def get_engine_status(self) -> dict:
        strategy_name = (
            self._strategy.get_strategy_name()
            if self._strategy else 'None'
        )
        return {
            'turns_simulated': self._turns_simulated,
            'strategy_used': strategy_name,
            'total_damage': self._total_damage,
            'cards_created': self._cards_created,
        }
