import sys
import os
import site


def get_python_executable() -> str:
    return sys.executable


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
    python_path = get_python_executable()
    is_in_venv, venv_name, venv_path = detect_virtual_env()

    if is_in_venv:
        packages_path = get_site_packages_path()
        display_inside_venv(python_path, venv_name, venv_path, packages_path)
    else:
        display_outside_venv(python_path)


if __name__ == "__main__":
    main()
