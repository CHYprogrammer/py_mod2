from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(
        self,
        name: str,
        cost: int,
        rarity: str,
        durability: int,
        effect: str
    ) -> None:
        super().__init__(name, cost, rarity)
        if not isinstance(durability, int) or durability <= 0:
            raise ValueError("Durability must be a positive integer.")
        self.durability = durability
        self.effect = effect
        self._in_play = False

    def play(self, game_state) -> dict:
        self._in_play = True
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': f'Permanent: {self.effect}'
        }

    def get_card_info(self) -> dict:
        """Return artifact card information."""
        info = super().get_card_info()
        info['type'] = 'Artifact'
        info['durability'] = self.durability
        info['effect'] = self.effect
        return info

    def activate_ability(self) -> dict:
        return {
            'artifact': self.name,
            'ability': self.effect,
            'durability_remaining': self.durability,
            'activated': True,
        }
