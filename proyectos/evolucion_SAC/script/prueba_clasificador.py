# prueba_clasificador.py

from app.clasificador_ia import clasificar_mensaje_con_ia

casos = [

    "pedido con faltante",

    "mercaderia rota",

    "pedido demorado",

    "problema de facturacion",

    "excelente servicio",

    "estado del pedido"

]

for texto in casos:

    print(
        texto,
        "->",
        clasificar_mensaje_con_ia(texto)
    )