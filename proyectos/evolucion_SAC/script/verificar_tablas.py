# verificar_tablas.py

import sqlite3
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))

from app.config import DB_FILE

conexion = sqlite3.connect(
    DB_FILE
)

cursor = conexion.cursor()

cursor.execute("""
SELECT name
FROM sqlite_master
WHERE type='table'
""")

for tabla in cursor.fetchall():
    print(tabla)

conexion.close()