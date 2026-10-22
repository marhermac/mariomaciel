import asyncio
import edge_tts
import os

VOICE = "en-US-AndrewNeural"

def text_to_speech(texto):

    archivo = os.path.abspath("audio/temp/output.mp3")

    async def generar():
        communicate = edge_tts.Communicate(texto, VOICE)
        await communicate.save(archivo)

    asyncio.run(generar())

    print("Archivo generado:", archivo)
    print("Existe:", os.path.exists(archivo))

    return archivo