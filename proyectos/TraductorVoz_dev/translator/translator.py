import time
from deep_translator import GoogleTranslator, MyMemoryTranslator

def translate_text(texto, source="auto", target="en"):
    """
    Traduce texto utilizando GoogleTranslator como motor principal,
    con fallback a MyMemoryTranslator.
    """
    if not texto or not texto.strip():
        return ""

    # 1. Intento principal con GoogleTranslator (más rápido y estable)
    for intento in range(2):
        try:
            if intento > 0:
                time.sleep(1)
            traductor_google = GoogleTranslator(source=source, target=target)
            resultado = traductor_google.translate(texto)
            if resultado:
                return resultado
        except Exception:
            pass

    # 2. Fallback de respaldo con MyMemoryTranslator si Google falla
    try:
        traductor_mymemory = MyMemoryTranslator(source="es", target="en")
        resultado_mm = traductor_mymemory.translate(texto)
        if resultado_mm:
            return resultado_mm
    except Exception:
        pass

    return (
        "[Error al traducir: No se pudo conectar con el servidor de traducción. Por favor, reintenta en un momento.]"
    )