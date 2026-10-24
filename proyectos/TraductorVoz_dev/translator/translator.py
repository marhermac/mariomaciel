import time
from deep_translator import GoogleTranslator, MyMemoryTranslator, LibreTranslateTranslator

def translate_text(text, source="auto", target="en", target_language=None, **kwargs):
    """
    Función flexible que acepta cualquier parámetro (target o target_language)
    y prueba múltiples motores de traducción para evitar bloqueos en la nube.
    """
    # Si la app pasa 'target_language' en lugar de 'target', lo adaptamos
    if target_language:
        target = target_language

    if not text or not str(text).strip():
        return ""

    texto_limpio = str(text).strip()

    # 1. Intento con GoogleTranslator
    try:
        traductor = GoogleTranslator(source=source, target=target)
        res = traductor.translate(texto_limpio)
        if res:
            return res
    except Exception:
        pass

    # 2. Intento con LibreTranslate (alternativa libre sin clave)
    try:
        traductor_lib = LibreTranslateTranslator(source=source if source != "auto" else "es", target=target)
        res = traductor_lib.translate(texto_limpio)
        if res:
            return res
    except Exception:
        pass

    # 3. Intento con MyMemoryTranslator como último recurso
    try:
        traductor_mm = MyMemoryTranslator(source="es", target=target)
        res = traductor_mm.translate(texto_limpio)
        if res:
            return res
    except Exception:
        pass

    return "[Error al traducir: No se pudo conectar con el servidor de traducción. Por favor, reintenta en un momento.]"