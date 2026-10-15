def clasificar_mensaje_con_ia(texto):

    texto = texto.lower()

    # FALTANTE

    if any(
        palabra in texto
        for palabra in [
            "faltante",
            "faltan",
            "faltó",
            "falto"
        ]
    ):
        return "FALTANTE"

    # ROTURA

    if any(
        palabra in texto
        for palabra in [
            "rotura",
            "roturas",
            "rota",
            "roto",
            "rotos",
            "rotas",
            "mercaderia rota",
            "mercadería rota",
            "dañado",
            "dañada",
            "golpeado",
            "golpeada"
        ]
    ):
        return "ROTURA"

    # DEMORA

    if any(
        palabra in texto
        for palabra in [
            "demora",
            "demorado",
            "demorada",
            "retraso",
            "retrasada",
            "retrasado"
        ]
    ):
        return "DEMORA"

    # FACTURACION

    if any(
        palabra in texto
        for palabra in [
            "factura",
            "facturacion",
            "facturación",
            "error de factura",
            "factura incorrecta"
        ]
    ):
        return "FACTURACION"

    # FELICITACION

    if any(
        palabra in texto
        for palabra in [
            "felicit",
            "excelente servicio",
            "gracias por"
        ]
    ):
        return "FELICITACION"

    return "CONSULTA"