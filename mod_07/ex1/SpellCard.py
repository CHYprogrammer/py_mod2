from ex0.Card import Card


class SpellCard(Card):
    EFFECT_TYPES = {'damage', 'heal', 'buff', 'debuff'}

    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            effect_type: str
            ) -> None:
        super().__init__(name, cost, rarity)
        if effect_type not in self.EFFECT_TYPES:
            raise ValueError(f"effect_type must be one of {self.EFFECT_TYPES}")
        self.effect_type = effect_type
        self.used = False

    def play(self, game_state: dict) -> dict:
        self.used = True
        effect_desc = {
            'damage': f'Deal {self.cost} damage to target',
            'heal': f'Restore {self.cost} health',
            'buff': f'Buff target by {self.cost}',
            'debuff': f'Debuff target by {self.cost}'
        }.get(self.effect_type, 'Spell effect applied')
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': effect_desc
        }

    def get_card_info(self):
        info = super().get_card_info()
        info['type'] = 'Spell'
        info['effect_type'] = self.effect_type
        return info

    def resolve_effect(self, targets: list) -> dict:
        return {
            'spell': self.name,
            'effect_type': self.effect_type,
            'targets': targets,
            'resolved': True
        }
