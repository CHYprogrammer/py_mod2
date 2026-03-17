def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients as validate
    validation = validate(ingredients)
    if validation.split()[-1] == "VALID":
        rec_rej = "recorded"
    else:
        rec_rej = "rejected"
    return f"Spell {rec_rej}: {spell_name} ({validate(ingredients)})"
