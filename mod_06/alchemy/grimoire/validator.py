def validate_ingredients(ingredients: str) -> str:
    t_f = "INVALID"
    for material in ingredients.split():
        if material in ("fire", "water", "earth", "air"):
            t_f = "VALID"
            break
    return f"{ingredients} - {t_f}"
