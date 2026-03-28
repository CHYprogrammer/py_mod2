import sys
import importlib


REQUIRED = [
    ("pandas", "Data manipulation"),
    ("numpy", "Numerical computations"),
    ("matplotlib", "Visualization"),
]


def check_dependency(package_name: str) -> tuple[bool, str]:
    try:
        module = importlib.import_module(package_name)
        version = getattr(module, "__version__", "unknown")
        return True, version
    except ImportError:
        return False, "not installed"


def show_versions() -> bool:
    print("Checking dependencies:")
    missing = []
    for package_name, label in REQUIRED:
        ok, version = check_dependency(package_name)
        status = "OK" if ok else "MISSING"
        print(f"  [{status}] {package_name} ({version}) - {label}")
        if not ok:
            missing.append(package_name)

    if missing:
        print(f"\nMissing: {', '.join(missing)}")
        print("  pip:    pip install -r requirements.txt")
        print("  poetry: poetry install")
        return False
    return True


def analyze() -> None:
    import numpy as np  # noqa:PLC0415
    import pandas as pd  # noqa:PLC0415
    import matplotlib  # noqa:PLC0415
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt  # noqa:PLC0415

    # Matrix data simulation
    time = np.linspace(0, 10, 1000)
    signal = np.sin(time)
    df = pd.DataFrame({"time": time, "signal": signal})

    # Simple visualization
    df.plot(x="time", y="signal")
    plt.title("Matrix Signal")
    plt.savefig("matrix_analysis.png")
    plt.close()


def main() -> None:
    print("LOADING STATUS: Loading programs...\n")

    if not show_versions():
        sys.exit(1)

    print("\nAnalyzing Matrix data...")
    print("Processing 1000 data points...")
    print("Generating visualization...")
    analyze()
    print("\nAnalysis complete!")
    print("Results saved to: matrix_analysis.png")


if __name__ == "__main__":
    main()
