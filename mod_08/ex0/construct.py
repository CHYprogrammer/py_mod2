import sys
import os
import site


class MatrixError(Exception):
    pass


def detect_virtual_env() -> tuple[bool, str | None, str | None]:
    virtual_env_path = os.environ.get("VIRTUAL_ENV")
    in_venv = (
        virtual_env_path is not None
        or sys.prefix != sys.base_prefix
    )
    if in_venv:
        venv_path = virtual_env_path or sys.prefix
        venv_name = os.path.basename(venv_path)
        return True, venv_name, venv_path
    return False, None, None


def get_site_packages_path() -> str:
    try:
        packages = site.getsitepackages()
        return packages[0] if packages else "Unknown"
    except AttributeError:
        return site.getusersitepackages()


def display_outside_venv(python_path: str) -> None:
    print("MATRIX STATUS: You're still plugged in\n")

    print(f"Current Python: {python_path}")
    print("Virtual Environment: None detected\n")

    print("WARNING: You're in the global environment!")
    print("The machines can see everything you install.\n")

    print("To enter the construct, run:")
    print("python -m venv matrix_env")
    print("source matrix_env/bin/activate  # On Unix")
    print("matrix_env")
    print("Scripts")
    print("activate     # On Windows\n")

    print("Then run this program again.")


def display_inside_venv(
    python_path: str,
    venv_name: str,
    venv_path: str,
    packages_path: str
) -> None:
    print("MATRIX STATUS: Welcome to the construct\n")

    print(f"Current Python:     {python_path}")
    print(f"Virtual Environment: {venv_name}")
    print(f"Environment Path:    {venv_path}\n")

    print("SUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.\n")

    print("Package installation path:")
    print(f"  {packages_path}")


def main() -> None:
    in_v = sys.prefix == sys.base_prefix
    status = "You're still plugged in" if in_v else "Welcome to the construct"
    print(f"\nMATRIX STATUS: {status}\n")
    print(f"Current Python: {sys.executable}")
    env_path = os.environ.get("VIRTUAL_ENV")
    print(f"Virtual Environment: {env_path}")
    if env_path is None:
        raise MatrixError
    print(f"Environment Path: {env_path}")
    print("\nSUCCESS: You're in an isolated environment!")
    print("Safe to install packages without affecting")
    print("the global system.\n")

    package_path = sys.executable
    print(f"Package installation path: {package_path}")


if __name__ == "__main__":
    try:
        main()
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
