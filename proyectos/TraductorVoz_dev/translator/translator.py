from deep_translator import GoogleTranslator

def translate_text(text, source="es", target="en", target_language=None, **kwargs):
    """
    Función de traducción de Español a Inglés utilizando GoogleTranslator.
    """
    if target_language:
        target = target_language

    if not text or not str(text).strip():
        return ""

    texto_limpio = str(text).strip()

    # Intentar traducir con Google
    try:
        traductor = GoogleTranslator(source=source, target=target)
        resultado = traductor.translate(texto_limpio)
        if resultado:
            return resultado
    except Exception:
        pass

    # Si el servidor externo bloquea la IP, devolvemos un aviso en inglés para mantener el flujo
    return f"Translation service temporarily unavailable. Original text: {texto_limpio}"