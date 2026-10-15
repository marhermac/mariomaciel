# app/investigacion/gestor_investigacion.py

import sqlite3

from app.config import DB_FILE

from app.investigacion.modelos import (
    TABLA_INVESTIGACIONES,
    TABLA_WMS,
    TABLA_TMS,
    TABLA_ENTREVISTAS,
    TABLA_ANALISIS
)


def crear_tablas_investigacion():

    conexion = sqlite3.connect(DB_FILE)

    cursor = conexion.cursor()

    cursor.execute(
        TABLA_INVESTIGACIONES
    )

    cursor.execute(
        TABLA_WMS
    )

    cursor.execute(
        TABLA_TMS
    )

    cursor.execute(
    TABLA_ENTREVISTAS
    )

    cursor.execute(
    TABLA_ANALISIS
    )

    conexion.commit()

    conexion.close()

    print(
        "Tablas de investigación creadas."
    )

def crear_investigacion(
    reclamo_id,
    responsable="Analista"
):

    conexion = sqlite3.connect(
        DB_FILE
    )

    cursor = conexion.cursor()

    cursor.execute(
        """
        INSERT INTO investigaciones
        (
            reclamo_id,
            fecha_inicio,
            estado,
            responsable
        )
        VALUES
        (
            ?,
            datetime('now'),
            'ABIERTA',
            ?
        )
        """,
        (
            reclamo_id,
            responsable
        )
    )

    conexion.commit()

    investigacion_id = cursor.lastrowid

    conexion.close()

    return investigacion_id   

def obtener_investigaciones():

    conexion = sqlite3.connect(
        DB_FILE
    )

    cursor = conexion.cursor()

    cursor.execute(
        """
        SELECT *
        FROM investigaciones
        ORDER BY id DESC
        """
    )

    datos = cursor.fetchall()

    conexion.close()

    return datos
def guardar_wms(
    investigacion_id,
    pedido_preparado,
    pedido_completo,
    stock_correcto,
    embalaje_correcto,
    sin_incidencias,
    turno,
    operador,
    supervisor,
    observaciones
):

    conexion = sqlite3.connect(
        DB_FILE
    )

    cursor = conexion.cursor()

    cursor.execute(
        """
        INSERT INTO investigacion_wms
        (
            investigacion_id,
            pedido_preparado,
            pedido_completo,
            stock_correcto,
            embalaje_correcto,
            sin_incidencias,
            turno,
            operador,
            supervisor,
            observaciones
        )
        VALUES
        (
            ?,?,?,?,?,?,?,?,?,?
        )
        """,
        (
            investigacion_id,
            pedido_preparado,
            pedido_completo,
            stock_correcto,
            embalaje_correcto,
            sin_incidencias,
            turno,
            operador,
            supervisor,
            observaciones
        )
    )

    conexion.commit()

    conexion.close()

def obtener_wms(
    investigacion_id
):

    conexion = sqlite3.connect(
        DB_FILE
    )

    cursor = conexion.cursor()

    cursor.execute(
        """
        SELECT *
        FROM investigacion_wms
        WHERE investigacion_id = ?
        """,
        (
            investigacion_id,
        )
    )

    datos = cursor.fetchone()

    conexion.close()

    return datos

def guardar_entrevista(
    investigacion_id,
    tipo_persona,
    nombre,
    comentarios,
    acciones
):

    conexion = sqlite3.connect(
        DB_FILE
    )

    cursor = conexion.cursor()

    cursor.execute(
        """
        INSERT INTO entrevistas
        (
            investigacion_id,
            tipo_persona,
            nombre,
            comentarios,
            acciones
        )
        VALUES
        (
            ?,?,?,?,?
        )
        """,
        (
            investigacion_id,
            tipo_persona,
            nombre,
            comentarios,
            acciones
        )
    )

    conexion.commit()

    conexion.close()


def obtener_entrevistas(
    investigacion_id
):

    conexion = sqlite3.connect(
        DB_FILE
    )

    cursor = conexion.cursor()

    cursor.execute(
        """
        SELECT *
        FROM entrevistas
        WHERE investigacion_id = ?
        """,
        (
            investigacion_id,
        )
    )

    datos = cursor.fetchall()

    conexion.close()

    return datos


def guardar_tms(
    investigacion_id,
    viaje,
    transportista,
    ruta,
    salida_horario,
    sin_reprogramacion,
    sin_rechazo,
    entrega_ventana,
    observaciones
):

    conexion = sqlite3.connect(
        DB_FILE
    )

    cursor = conexion.cursor()

    cursor.execute(
        """
        INSERT INTO investigacion_tms
        (
            investigacion_id,
            viaje,
            transportista,
            ruta,
            salida_horario,
            sin_reprogramacion,
            sin_rechazo,
            entrega_ventana,
            observaciones
        )
        VALUES
        (
            ?,?,?,?,?,?,?,?,?
        )
        """,
        (
            investigacion_id,
            viaje,
            transportista,
            ruta,
            salida_horario,
            sin_reprogramacion,
            sin_rechazo,
            entrega_ventana,
            observaciones
        )
    )
   
   
    conexion.commit()

    conexion.close()

def obtener_tms(
    investigacion_id
):

    conexion = sqlite3.connect(
        DB_FILE
    )

    cursor = conexion.cursor()

    cursor.execute(
        """
        SELECT *
        FROM investigacion_tms
        WHERE investigacion_id = ?
        """,
        (
            investigacion_id,
        )
    )

    datos = cursor.fetchone()

    conexion.close()

    return datos


def guardar_analisis_causa_raiz(
    investigacion_id,
    causa_raiz,
    origen_problema,
    accion_correctiva,
    accion_preventiva,
    conclusion_final,
    problema_analizar,
    why1,
    why2,
    why3,
    why4,
    why5
):

    conexion = sqlite3.connect(
        DB_FILE
    )

    cursor = conexion.cursor()

    cursor.execute(
        """
        INSERT INTO analisis
        (
            investigacion_id,
            causa_raiz,
            origen_problema,
            accion_correctiva,
            accion_preventiva,
            conclusion_final,
            problema_analizar,
            why1,
            why2,
            why3,
            why4,
            why5
        )
        VALUES
        (
            ?,?,?,?,?,?,?,?,?,?,?,?
        )
        """,
        (
            investigacion_id,
            causa_raiz,
            origen_problema,
            accion_correctiva,
            accion_preventiva,
            conclusion_final,
            problema_analizar,
            why1,
            why2,
            why3,
            why4,
            why5
        )
    )
    
    conexion.commit()

    conexion.close()
    
    