# app/investigacion/modelos.py

TABLA_INVESTIGACIONES = """
CREATE TABLE IF NOT EXISTS investigaciones (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    reclamo_id INTEGER,

    fecha_inicio TEXT,

    estado TEXT,

    responsable TEXT
)
"""

TABLA_WMS = """
CREATE TABLE IF NOT EXISTS investigacion_wms (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    investigacion_id INTEGER,

    pedido_preparado INTEGER,

    pedido_completo INTEGER,

    stock_correcto INTEGER,

    embalaje_correcto INTEGER,

    sin_incidencias INTEGER,

    turno TEXT,

    operador TEXT,

    supervisor TEXT,

    observaciones TEXT
)
"""

TABLA_TMS = """
CREATE TABLE IF NOT EXISTS investigacion_tms (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    investigacion_id INTEGER,

    viaje TEXT,

    transportista TEXT,

    ruta TEXT,

    salida_horario INTEGER,

    sin_reprogramacion INTEGER,

    sin_rechazo INTEGER,

    entrega_ventana INTEGER,

    observaciones TEXT
)
"""
TABLA_ENTREVISTAS = """
CREATE TABLE IF NOT EXISTS entrevistas (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    investigacion_id INTEGER,

    tipo_persona TEXT,

    nombre TEXT,

    comentarios TEXT,

    acciones TEXT
)
"""
TABLA_ANALISIS = """
CREATE TABLE IF NOT EXISTS analisis (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    investigacion_id INTEGER,

    causa_raiz TEXT,

    origen_problema TEXT,

    accion_correctiva TEXT,

    accion_preventiva TEXT,

    conclusion_final TEXT,

    problema_analizar TEXT,

    why1 TEXT,

    why2 TEXT,

    why3 TEXT,

    why4 TEXT,

    why5 TEXT
)
"""

