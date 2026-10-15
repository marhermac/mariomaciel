import re

from app.gestor_db import (
    buscar_cliente_por_email
)


def extraer_pedido(texto):

    texto = texto.lower()

    patrones = [

        r'pedido\s*n[°ºo]?\s*(\d+)',
        r'pedido\s*nro\.?\s*(\d+)',
        r'pedido\s*#\s*(\d+)',
        r'pedido\s*(\d+)'

    ]

    for patron in patrones:

        resultado = re.search(
            patron,
            texto
        )

        if resultado:

            return resultado.group(1)

    return "SIN_PEDIDO"


def extraer_cliente(remitente):

    email = re.search(
        r'[\w\.-]+@[\w\.-]+',
        remitente
    )

    if email:

        return buscar_cliente_por_email(
            email.group(0)
        )

    return "CLIENTE_DESCONOCIDO"