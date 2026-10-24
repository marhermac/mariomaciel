from deep_translator import PonsTranslator

def translate_text(text, source="es", target="en", target_language=None, **kwargs):
    """
    Traduce texto utilizando PonsTranslator como alternativa libre en la nube.
    """
    if target_language:
        target = target_language

    if not text or not str(text).strip():
        return ""

    texto_limpio = str(text).strip()

    try:
        # PonsTranslator es excelente para traducciones directas sin bloqueos estrictos de IP
        traductor = PonsTranslator(source=source, target=target)
        resultado = traductor.translate(texto_limpio)
        if resultado:
            return resultado
    except Exception as e:
        print(f"Error con Pons: {e}")

    # Fallback final si la red externa completa no responde
    return f"[Translation Warning - Offline Mode]: {texto_limpio}"