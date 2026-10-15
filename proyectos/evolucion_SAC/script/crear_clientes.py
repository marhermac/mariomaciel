# crear_clientes.py
from app.gestor_db import (
    crear_tabla_clientes,
    crear_tabla_correos_procesados
)

crear_tabla_clientes()
crear_tabla_correos_procesados()

print("Tablas creadas.")
