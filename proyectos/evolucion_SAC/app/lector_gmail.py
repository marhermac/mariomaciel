from google.auth.transport.requests import Request
from google_auth_oauthlib.flow import InstalledAppFlow
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build

import base64

from app.config import (
    TOKEN_FILE,
    CREDENTIALS_FILE
)

from app.extractor_datos import (
    extraer_cliente,
    extraer_pedido
)

from app.clasificador_ia import (
    clasificar_mensaje_con_ia
)

from app.gestor_db import (
    guardar_reclamo,
    correo_ya_procesado,
    guardar_correo_procesado
)

# -----------------------------------
# CONFIGURACION
# -----------------------------------

SCOPES = [
    "https://www.googleapis.com/auth/gmail.readonly"
]

# -----------------------------------
# AUTENTICACION
# -----------------------------------

def conectar_gmail():

    creds = None

    try:

        creds = Credentials.from_authorized_user_file(
            str(TOKEN_FILE),
            SCOPES
        )

    except Exception:
        pass

    if not creds or not creds.valid:

        if creds and creds.expired and creds.refresh_token:

            creds.refresh(Request())

        else:

            flow = InstalledAppFlow.from_client_secrets_file(
                str(CREDENTIALS_FILE),
                SCOPES
            )

            creds = flow.run_local_server(
                port=0
            )

        with open(
            TOKEN_FILE,
            "w"
        ) as token:

            token.write(
                creds.to_json()
            )

    servicio = build(
        "gmail",
        "v1",
        credentials=creds
    )

    return servicio


# -----------------------------------
# LEER CORREOS
# -----------------------------------

def leer_correos():

    servicio = conectar_gmail()

    resultados = (
        servicio.users()
        .messages()
        .list(
            userId="me",
            maxResults=50
        )
        .execute()
    )

    mensajes = resultados.get(
        "messages",
        []
    )

    print(
        f"\nCorreos encontrados: {len(mensajes)}\n"
    )

    for mensaje in mensajes:

        gmail_id = mensaje["id"]

        if correo_ya_procesado(
            gmail_id
        ):

            print(
                f"Correo ya fue procesado: {gmail_id}"
            )

            continue

        datos = (
            servicio.users()
            .messages()
            .get(
                userId="me",
                id=gmail_id
            )
            .execute()
        )

        headers = datos["payload"].get(
            "headers",
            []
        )

        remitente = ""
        asunto = ""

        for h in headers:

            if h["name"] == "From":
                remitente = h["value"]

            elif h["name"] == "Subject":
                asunto = h["value"]

        cuerpo = ""

        try:

            if "parts" in datos["payload"]:

                for parte in datos["payload"]["parts"]:

                    if (
                        parte["mimeType"]
                        == "text/plain"
                    ):

                        data = parte["body"].get(
                            "data"
                        )

                        if data:

                            cuerpo = (
                                base64
                                .urlsafe_b64decode(data)
                                .decode(
                                    "utf-8",
                                    errors="ignore"
                                )
                            )

                            break

        except Exception:
            pass

        texto_completo = (
            asunto + " " + cuerpo
        )

        cliente = extraer_cliente(
            remitente
        )

        pedido = extraer_pedido(
            texto_completo
        )

        categoria = clasificar_mensaje_con_ia(
            texto_completo
        )

        guardar_reclamo(
            email_cliente=remitente,
            cliente_logistica=cliente,
            pedido=pedido,
            categoria=categoria,
            texto_mensaje=cuerpo
        )

        guardar_correo_procesado(
            gmail_id
        )

        print("=" * 60)
        print(f"CLIENTE: {cliente}")
        print(f"PEDIDO: {pedido}")
        print(f"CATEGORIA: {categoria}")
        print(f"ASUNTO: {asunto}")
        print("=" * 60)


# -----------------------------------
# MAIN
# -----------------------------------

if __name__ == "__main__":

    leer_correos()