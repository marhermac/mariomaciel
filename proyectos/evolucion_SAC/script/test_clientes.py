import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))


from app.gestor_db import (
    agregar_cliente,
    obtener_clientes
)

agregar_cliente(
    "Quefrio",
    "mario.maciel5@gmail.com"
)

agregar_cliente(
    "Arrocera Villaguay",
    "mhm639@hotmail.com"
)

print(
    obtener_clientes()
)