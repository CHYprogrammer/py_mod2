from typing import Callable, Any


def mage_counter() -> Callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> Callable:
    total = initial_power

    def accumulate(amount: int) -> int:
        nonlocal total
        total += amount
        return total

    return accumulate


def enchantment_factory(enchantment_type: str) -> Callable:

    def enchant(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchant


def memory_vault() -> dict[str, Callable]:
    storage = {}

    def store(key: str, value: Any) -> None:
        storage[key] = value

    def recall(key: str) -> str:
        return storage.get(key, "Memory not found")

    return {"store": store, "recall": recall}


if __name__ == "__main__":
    print("\nTesting mage counter...")
    counter = mage_counter()
    for i in range(1, 4):
        print(f"Call {i}, {counter()}")

    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Sheild"))

    print("\nTesting spell accumulator...")
    accumulate = spell_accumulator(100)
    print("Initial: 100")
    print(f"Add 50: {accumulate(50)}")
    print(f"Add 30: {accumulate(30)}")

    print("\nTesting memory vault")
    vault = memory_vault()
    vault['store']('hero', 'Merlin')
    print(vault['recall']('hero'))
    print(vault['recall']('unknown'))
