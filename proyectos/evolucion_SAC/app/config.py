from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

DB_FILE = BASE_DIR / "data" / "sistema_logistica.db"

CLIENTES_FILE = BASE_DIR / "data" / "clientes.csv"

TOKEN_FILE = BASE_DIR / "config" / "token.json"

CREDENTIALS_FILE = BASE_DIR / "config" / "credentials.json"