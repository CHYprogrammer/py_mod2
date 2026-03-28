import sys
import os
import site


class MatrixError(Exception):
    pass


def get_site_packages_path() -> str:
    try:
        packages = site.getsitepackages()
        return packages[0] if packages else "Unknown"
    except AttributeError:
        return site.getusersitepackages()


def detect_venv() -> None:
    in_v = sys.prefix != sys.base_prefix
    status = "Welcome to the construct" if in_v else "You're still plugged in"
    print(f"\nMATRIX STATUS: {status}\n")
    print(f"Current Python: {sys.executable}")
    venv_path = os.environ.get("VIRTUAL_ENV")
    if venv_path is None:
        raise MatrixError
    venv_name = os.path.basename(venv_path)
    print(f"Virtual Environment: {venv_name}")
    print(f"Environment Path: {venv_path}")
    print("\nSUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.\n")

    package_path = get_site_packages_path()
    print(f"Package installation path:\n{package_path}")


def main() -> None:
    try:
        detect_venv()
    except MatrixError:
        print("WARNING: You're in the global environment!")
        print("The machines can see everything you install.")

        print("\nTo enter the construct, run:")
        print("python -m venv matrix_env")
        print("source matrix_env/bin/activate  # On Unix")
        print("matrix_env")
        print("Scripts")
        print("activate     # On Windows")

        print("\nThen run this program again.")


if __name__ == "__main__":
    main()
