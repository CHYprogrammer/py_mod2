import functools
import operator
from typing import Callable


def spell_reducer(spells: list[int], operation: str) -> int:
    ops = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": lambda a, b: a if a > b else b,
        "min": lambda a, b: a if a < b else b
    }
    return functools.reduce(ops[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    return {
        "fire_enchant": functools.partial(
            base_enchantment, power=50, element="fire"),
        "ice_enchant": functools.partial(
            base_enchantment, power=50, element="ice"),
        "lightning_enchant": functools.partial(
            base_enchantment, power=50, element="lightning")
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:  # typo in docment??
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable:
    @functools.singledispatch
    def dispatch(spell) -> str:
        return f"Unknown spell type: {spell}"

    @dispatch.register(int)
    def _(spell: int) -> str:
        return f"Damage spell: {spell} damage dealt"

    @dispatch.register(str)
    def _(spell: str) -> str:
        return f"Enchantment: {spell} applied"

    @dispatch.register(list)
    def _(spell: list) -> str:
        return f"Multi-cast {len(spell)} spells cast"

    return dispatch


if __name__ == "__main__":
    spells = [10, 20, 30, 40]
    print("\nTesting spell reducer...")
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("\nTesting memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell dispatcher...")
    dispatch = spell_dispatcher()
    print(dispatch(42))
    print(dispatch("fireball"))
    print(dispatch(["fire", "ice", "lightning"]))
