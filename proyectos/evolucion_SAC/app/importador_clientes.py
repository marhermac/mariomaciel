import pandas as pd
from app.gestor_db import agregar_cliente

from app.config import CLIENTES_CSV

df = pd.read_csv("CLIENTES_CVS")

for _, fila in df.iterrows():

    agregar_cliente(
        fila["cliente_logistica"],
        fila["email"]
    )

print("Importación finalizada")