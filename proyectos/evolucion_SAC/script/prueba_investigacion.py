import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))

from app.investigacion.gestor_investigacion import (
    crear_investigacion,
    obtener_investigaciones
)

id_nuevo = crear_investigacion(
    reclamo_id=1,
    responsable="Mario"
)

print(
    f"Investigación creada: {id_nuevo}"
)

print(
    obtener_investigaciones()
)