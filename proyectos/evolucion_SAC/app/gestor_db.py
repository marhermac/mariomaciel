import sqlite3
from datetime import datetime

from app.config import DB_FILE

DB_NAME = str(DB_FILE)

import pandas as pd

def importar_clientes_csv(archivo):

    df = pd.read_csv(archivo)

    for _, fila in df.iterrows():

        agregar_cliente(
            fila["cliente_logistica"],
            fila["email"]
        )

    return len(df)

def crear_base_de_datos():

    conexion = sqlite3.connect(DB_FILE)
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reclamos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            fecha_registro TEXT,
            email_cliente TEXT,
            cliente_logistica TEXT,
            pedido TEXT,
            categoria TEXT,
            texto_mensaje TEXT
        )
    """)

    conexion.commit()
    conexion.close()

    print("Base de datos configurada correctamente.")


def crear_tabla_clientes():

    conexion = sqlite3.connect(DB_FILE)
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clientes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cliente_logistica TEXT NOT NULL,
            email TEXT NOT NULL UNIQUE
        )
    """)

    conexion.commit()
    conexion.close()

    print("Tabla clientes configurada correctamente.")


def guardar_reclamo(
    email_cliente,
    cliente_logistica,
    pedido,
    categoria,
    texto_mensaje
):

    conexion = sqlite3.connect(DB_FILE)
    cursor = conexion.cursor()

    fecha_actual = datetime.now().strftime(
        "%Y-%m-%d %H:%M:%S"
    )

    cursor.execute("""
        INSERT INTO reclamos (
            fecha_registro,
            email_cliente,
            cliente_logistica,
            pedido,
            categoria,
            texto_mensaje
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """,
    (
        fecha_actual,
        email_cliente,
        cliente_logistica,
        pedido,
        categoria,
        texto_mensaje
    ))

    conexion.commit()
    conexion.close()

    print(
        f"Reclamo guardado: "
        f"{cliente_logistica} - "
        f"{categoria}"
    )


def obtener_todos_los_datos():

    conexion = sqlite3.connect(DB_FILE)
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT *
        FROM reclamos
    """)

    datos = cursor.fetchall()

    conexion.close()

    return datos


def agregar_cliente(
    cliente_logistica,
    email
):

    conexion = sqlite3.connect(
        DB_FILE
    )

    cursor = conexion.cursor()

    try:

        cursor.execute("""
        INSERT INTO clientes
        (
            cliente_logistica,
            email
        )
        VALUES (?,?)
        """,
        (
            cliente_logistica,
            email
        ))

        conexion.commit()

    except sqlite3.IntegrityError:

        print(
            f"Cliente ya existe: {email}"
        )

    finally:

        conexion.close()

def obtener_clientes():

    conexion = sqlite3.connect(DB_FILE)
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT *
        FROM clientes
        ORDER BY cliente_logistica
    """)

    datos = cursor.fetchall()

    conexion.close()

    return datos


def eliminar_cliente(id_cliente):

    conexion = sqlite3.connect(DB_FILE)
    cursor = conexion.cursor()

    cursor.execute("""
        DELETE FROM clientes
        WHERE id = ?
    """,
    (
        id_cliente,
    ))

    conexion.commit()
    conexion.close()

def buscar_cliente_por_email(email):

    conexion = sqlite3.connect(DB_FILE)

    cursor = conexion.cursor()

    cursor.execute(
        """
        SELECT cliente_logistica
        FROM clientes
        WHERE LOWER(email) = LOWER(?)
        """,
        (email,)
    )

    resultado = cursor.fetchone()

    conexion.close()

    if resultado:

        return resultado[0]

    return "CLIENTE_DESCONOCIDO"  
def crear_tabla_correos_procesados():

    conexion = sqlite3.connect(DB_FILE)

    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS correos_procesados (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            gmail_id TEXT UNIQUE

        )
    """)

    conexion.commit()

    conexion.close()

    print(
        "Tabla correos_procesados creada."
    )
def correo_ya_procesado(
    gmail_id
):

    conexion = sqlite3.connect(
        DB_FILE
    )

    cursor = conexion.cursor()

    cursor.execute("""
        SELECT gmail_id
        FROM correos_procesados
        WHERE gmail_id = ?
    """,
    (
        gmail_id,
    ))

    resultado = cursor.fetchone()

    conexion.close()

    return resultado is not None
def guardar_correo_procesado(
    gmail_id
):

    conexion = sqlite3.connect(
        DB_FILE
    )

    cursor = conexion.cursor()

    cursor.execute("""
        INSERT INTO correos_procesados
        (
            gmail_id
        )
        VALUES (?)
    """,
    (
        gmail_id,
    ))

    conexion.commit()

    conexion.close()              