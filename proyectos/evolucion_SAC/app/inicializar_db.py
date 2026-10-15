# inicializar_db.py

from app.gestor_db import (
    crear_base_de_datos,
    crear_tabla_clientes,
    crear_tabla_correos_procesados
)

from app.investigacion.gestor_investigacion import (
    crear_tablas_investigacion,
    crear_tabla_analisis
)


crear_base_de_datos()
crear_tabla_clientes()
crear_tabla_correos_procesados()

crear_tablas_investigacion()
crear_tabla_analisis
print("Base completa creada.")