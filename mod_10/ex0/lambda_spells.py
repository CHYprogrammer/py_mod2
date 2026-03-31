def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda a: a["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda m: m["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    if not mages:
        return {"max_power": 0, "min_power": 0, "avg_power": 0.0}
    powers = list(map(lambda m: m["power"], mages))
    return {
        "max_power": max(powers),
        "min_power": min(powers),
        "avg_power": round(sum(powers) / len(powers), 2)
    }


if __name__ == "__main__":
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'orb'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'staff'},
        {'name': 'Shadow Blade', 'power': 78, 'type': 'blade'}
    ]

    print("\nTesting artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts[:2])
    print(
        f"{sorted_artifacts[0]['name']} ({sorted_artifacts[0]['power']} power)"
        + " comes before "
        f"{sorted_artifacts[1]['name']} ({sorted_artifacts[1]['power']} power)"
    )

    print("\nTesting spell transformer...")
    spells = ["fireball", "heal", "shield"]
    print(' '.join(spell_transformer(spells)))

    print("\nTesting power filter...")
    print([f"{x['name']}: {x['power']}" for x in power_filter(artifacts, 80)])

    print("\nTesting mage stats...")
    print(mage_stats(artifacts))
