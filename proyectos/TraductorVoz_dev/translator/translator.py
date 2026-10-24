import time
from deep_translator import GoogleTranslator, MyMemoryTranslator

def translate_text(text, source="auto", target="en", target_language=None, **kwargs):
    """
    Función de traducción flexible y robusta con Google y MyMemory.
    """
    if target_language:
        target = target_language

    if not text or not str(text).strip():
        return ""

    texto_limpio = str(text).strip()

    # 1. Intento principal con GoogleTranslator
    for intento in range(2):
        try:
            if intento > 0:
                time.sleep(1)
            traductor = GoogleTranslator(source=source, target=target)
            res = traductor.translate(texto_limpio)
            if res:
                return res
        except Exception:
            pass

    # 2. Fallback de respaldo con MyMemoryTranslator
    try:
        src_mm = "es" if source == "auto" else source[:2]
        tgt_mm = target[:2]
        traductor_mm = MyMemoryTranslator(source=src_mm, target=tgt_mm)
        res = traductor_mm.translate(texto_limpio)
        if res:
            return res
    except Exception:
        pass

    return "[Error al traducir: No se pudo conectar con el servidor de traducción. Por favor, reintenta en un momento.]"