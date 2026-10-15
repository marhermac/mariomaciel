import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))

from app.investigacion.gestor_investigacion import (
    guardar_wms,
    obtener_wms
)

guardar_wms(
    investigacion_id=1,
    pedido_preparado=1,
    pedido_completo=1,
    stock_correcto=1,
    embalaje_correcto=1,
    sin_incidencias=0,
    turno="Noche",
    operador="Juan",
    supervisor="Carlos",
    observaciones="Faltó una caja"
)

print(
    obtener_wms(1)
)