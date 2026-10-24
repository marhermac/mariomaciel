from deep_translator import GoogleTranslator

def translate_text(text, source="auto", target="en", target_language=None, **kwargs):
    """
    Función de traducción robusta con GoogleTranslator y respaldo local offline.
    """
    if target_language:
        target = target_language

    if not text or not str(text).strip():
        return ""

    texto_limpio = str(text).strip()

    # 1. Ñaikãturi GoogleTranslator rupive
    try:
        traductor = GoogleTranslator(source=source, target=target)
        resultado = traductor.translate(texto_limpio)
        if resultado:
            return resultado
    except Exception:
        pass

    # 2. Respaldo offline (Ani hag̃ua opyta rei pe programa)
    return f"[Modo Offline]: {texto_limpio}"