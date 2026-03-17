from alchemy import transmutation
import alchemy


if __name__ == "__main__":
    print("\n=== Pathway Debate Mastery ===")

    try:
        print("\nTesting Absolute Imports (from basic.py):")
        print(f"lead_to_gold(): {transmutation.lead_to_gold()}")
        print(f"stone_to_gem(): {transmutation.stone_to_gem()}")
        abs_flag = True
    except Exception as e:
        abs_flag = False
        print(f"\n******Error: {e}\n")

    try:
        print("\nTesting Relative Imports (from advanced.py):")
        print(f"philosophers_stone(): {transmutation.philosophers_stone()}")
        print(f"elixir_of_life(): {transmutation.elixir_of_life()}")
        rel_flag = True
    except Exception as e:
        rel_flag = False
        print(f"\n******Error: {e}\n")

    try:
        print("\nTesting Package Access:")
        print("alchemy.transmutation.lead_to_gold(): "
              f"{alchemy.transmutation.lead_to_gold()}")
        print("alchemy.transmutation.philosophers_stone(): "
              f"{alchemy.transmutation.philosophers_stone()}")
    except Exception as e:
        print(f"\n******Error: {e}\n")

    abs = "clear"
    rel = "concise"
    if abs_flag and rel_flag:
        print(f"\nBoth pathways work! Absolute: {abs}, Relative: {rel}")
    else:
        if not abs_flag:
            abs = "ERROR"
        if not rel_flag:
            rel = "ERROR"
        print(f"\nPathways could not work... Absolute: {abs}, Relative: {rel}")
