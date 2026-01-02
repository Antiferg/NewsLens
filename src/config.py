import os
from dotenv import load_dotenv

load_dotenv()

def _require_env(name: str) -> str:
    value = os.getenv(name)
    if not value:
        raise RuntimeError(f"Missing environment variable: {name}")
    return value

ENV = os.getenv("ENV", "Development")
DEBUG = ENV != "production"

DB_URL = _require_env("DATABASE_URL")