import time
from deep_translator import MyMemoryTranslator, GoogleTranslator

def translate_text(texto, source="es", target="en"):
    """Traduce texto utilizando MyMemory como motor principal para evitar bloqueos por IP,

    con fallback a Google.
    """
    if not texto or not texto.strip():
        return ""

    # Intento principal con MyMemory (libre de rate-limits estrictos)
    try:
        traductor = MyMemoryTranslator(source="es-ES", target="en-US")
        return traductor.translate(texto)
    except Exception:
        # Fallback de respaldo con Google e intento progresivo
        for intento in range(2):
            try:
                time.sleep(1)
                traductor_google = GoogleTranslator(
                    source=source, target=target
                )
                return traductor_google.translate(texto)
            except Exception:
                pass

    return (
        "[Error al traducir: No se pudo conectar con el servidor de traducción. Por favor, reintenta en un momento.]"
    )