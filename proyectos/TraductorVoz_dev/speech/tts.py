import tempfile
import asyncio
import edge_tts

def text_to_speech(text, voice="en-US-AndrewNeural"):
    """
    Genera audio a partir de texto y lo guarda en un archivo temporal seguro.
    """
    # Crear un archivo temporal seguro con extensión .mp3
    with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
        temp_path = temp_audio.name

    # Función asíncrona para guardar el audio con edge-tts
    async def _generate():
        communicate = edge_tts.Communicate(text, voice)
        await communicate.save(temp_path)

    asyncio.run(_generate())
    
    return temp_path  # Retorna la ruta al archivo temporal