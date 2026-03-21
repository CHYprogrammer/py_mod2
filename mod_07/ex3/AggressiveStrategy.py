from ex3.GameStrategy import GameStrategy
from ex0.Card import Card
from ex0.CreatureCard import CreatureCard


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list[Card], battlefield: list) -> dict:
        available_mana = 10
        cards_played = []
        mana_used = 0
        targets_attacked = []
        damage_dealt = 0
        sorted_hand = sorted(hand, key=lambda c: c.cost)

        for card in sorted_hand:
            if card.is_playable(available_mana - mana_used):
                game_state = {'turn': 1, 'mana': available_mana - mana_used}
                card.play(game_state)
                cards_played.append(card.name)
                mana_used += card.cost

                if isinstance(card, CreatureCard):
                    target = 'Enemy Player'
                    targets_attacked.append(target)
                    damage_dealt += card.attack

        return {
            'cards_played': cards_played,
            'mana_used': mana_used,
            'targets_attacked': targets_attacked,
            'damage_dealt': damage_dealt,
        }

    def get_strategy_name(self) -> str:
        return 'AggressiveStrategy'

    def prioritize_targets(self, available_targets: list) -> list:
        player_targets = [
            t for t in available_targets if 'Player' in str(t)
        ]
        other_targets = [
            t for t in available_targets if 'Player' not in str(t)
        ]
        return player_targets + other_targets
