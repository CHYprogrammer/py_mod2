from typing import Callable, Any


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    return lambda *args, **kwargs: (spell1(*args, **kwargs),
                                    spell2(*args, **kwargs))


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    return lambda *args, **kwargs: base_spell(*args, **kwargs) * multiplier


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def cast(*args: Any, **kwargs: Any) -> Callable | str:
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return cast


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(*args: Any, **kwargs: Any) -> list:
        return [spell(*args, **kwargs) for spell in spells]
    return sequence


if __name__ == "__main__":
    def fireball(target: str) -> str:
        return f"Fireball hits {target}"

    def heal(target: str) -> str:
        return f"Heals {target}"

    def damage(power: int) -> int:
        return power

    def is_dragon(target: str) -> bool:
        return target == "dragon"

    print("\nTesting spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon")
    print(f"Combined spell result: {result[0]}, {result[1]}")

    print("\nTesting power amplifier...")
    mega = power_amplifier(damage, 3)
    print(f"Original: {damage(10)}, Amplified: {mega(10)}")

    print("\nTesting conditional caster...")
    dragon_only = conditional_caster(is_dragon, fireball)
    print("dragon: " + dragon_only("dragon"))
    print("goblin: " + dragon_only("goblin"))

    print("\nTesting spell sequence...")
    sequence = spell_sequence([fireball, heal])
    print(sequence('dragon'))
