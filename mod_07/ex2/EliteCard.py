from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(
            self,
            name: str,
            cost: int,
            rarity: str,
            attack: int,
            defense: int,
            mana_pool: int
    ) -> None:
        Card.__init__(self, name, cost, rarity)
        self.atk = attack
        self.defense = defense
        self.mana_pool = mana_pool
        self.channeled_mana = 0

    def play(self) -> dict:
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': 'Elite card deployed with combat and magic abilities'
        }

    def get_card_info(self) -> dict:
        info = super().get_card_info()
        info['type'] = 'Elite'
        info['attack'] = self.atk
        info['defense'] = self.defense
        info['mana_pool'] = self.mana_pool
        return info

    def attack(self, target: str | Card) -> dict:
        target_name = target if isinstance(target, str) else target.name
        return {
            'attacker': self.name,
            'target': target_name,
            'damage': self.atk,
            'combat_type': 'melee',
        }

    def defend(self, incoming_damage: int) -> dict:
        blocked = min(incoming_damage, self.defense)
        taken = incoming_damage - blocked
        return {
            'defender': self.name,
            'damage_taken': taken,
            'damage_blocked': blocked,
            'still_alive': True,
        }

    def get_combat_stats(self) -> dict:
        return {
            'attack': self.atk,
            'defense': self.defense,
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        mana_cost = len(targets) * 2
        self.mana_pool -= mana_cost
        return {
            'caster': self.name,
            'spell': spell_name,
            'targets': targets,
            'mana_used': mana_cost,
        }

    def channel_mana(self, amount: int) -> dict:
        self.channeled_mana += amount
        self.mana_pool += amount
        return {
            'channeled': amount,
            'total_mana': self.mana_pool,
        }

    def get_magic_stats(self) -> dict:
        return {
            'mana_pool': self.mana_pool,
            'channeled_mana': self.channeled_mana,
        }
