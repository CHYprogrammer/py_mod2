from alchemy import grimoire


print("=== Circular Curse Breaking ===")

print("Testing ingredient validation:")
print("validate_ingredients(\"fire air\"): "
      f"{grimoire.validate_ingredients('fire air')}")
print("validate_ingredients(\"dragon scales\"): "
      f"{grimoire.validate_ingredients('dragon scales')}")

print("\nTesting spell recording with validation:")
print("record_spell(\"Fireball\", \"fire air\"): "
      f"{grimoire.record_spell('Fireball', 'fire_air')}")
print("record_spell(\"Dark Magic\", \"shadow\"): "
      f"{grimoire.record_spell('Dark Magid', 'shadow')}")

print("\nTesting late import technique:")
print("record_spell(\"Lighning\", \"air\"): "
      f"{grimoire.record_spell('Lightnng', 'air')}")

print("\nCircular dependency curse avoided using late imports!")
print("All spells processed safely!")
