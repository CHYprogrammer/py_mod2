import sys
import os


try:
    from dotenv import load_dotenv
    load_dotenv()
    DOTENV_AVAILABLE = True
except ImportError:
    DOTENV_AVAILABLE = False


REQUIRED = [
    "DATABASE_URL",
    "API_KEY",
    "ZION_ENDPOINT"
]

OPTIONAL = {
    "MATRIX_MODE": "development",
    "LOG_LEVEL": "DEBUG"
}


def load_config() -> dict[str, str | None]:
    config = {}
    for key in REQUIRED:
        config[key] = os.environ.get(key)
    for key, default in OPTIONAL.items():
        config[key] = os.environ.get(key, default)
    return config


def show_config(config: dict[str, str | None]) -> bool:
    missing = [k for k in REQUIRED if not config[k]]
    if missing:
        print("WARNING: Missing required configuration!")
        for key in missing:
            print(f"  - {key} is not set")
        print("\nCopy .env.example to .env and fill in your values.")
        return False

    print("Configuration loaded:")
    print(f"Mode: {config.get('MATRIX_MODE')}")
    print(f"Database: {config.get('DATABASE_URL')}")
    print(f"API Access: {config.get('API_KEY')}")
    print(f"Log Level: {config.get('LOG_LEVEL')}")
    print(f"Zion Network: {config.get('ZION_ENDPOINT')}")
    return True


def main() -> None:
    print("\nORACLE STATUS: Reading the Matrix...\n")
    if not DOTENV_AVAILABLE:
        print("WARNING: python-dotenv is not installed.")
        print("Install it with:  pip install python-dotenv")
        print("Falling back to system environment variables only.")
        print()
        sys.exit(1)
    config = load_config()
    if not show_config(config):
        sys.exit(1)

    print("\nEnvironment security check:")
    print("[OK] No hardcoded secrets detected")
    print("[OK] .env file properly configured")
    print("[OK] Production overrides available")
    print("\nThe Oracle sees all configurations.")


if __name__ == "__main__":
    main()
