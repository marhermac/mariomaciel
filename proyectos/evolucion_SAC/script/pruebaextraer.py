from app.extractor_datos import extraer_pedido

casos = [

    "pedido 12567 con faltante",
    "pedido nro 7560",
    "pedido n° 8954",
    "pedido #12345",
    "codigo AR001"

]

for c in casos:

    print(
        c,
        "->",
        extraer_pedido(c)
    )