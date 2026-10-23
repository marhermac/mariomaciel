import tempfile
import os
from faster_whisper import WhisperModel

# Se carga una sola vez al iniciar el programa
model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)

def speech_to_text(audio_file):
    """
    Convierte un archivo de audio o un objeto binario de Streamlit a texto 
    utilizando faster-whisper, evitando errores de metadatos o flujos en memoria.
    """
    temp_file_path = None
    try:
        # Si el objeto viene desde la interfaz de Streamlit (BytesIO / UploadedFile)
        if hasattr(audio_file, "read"):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
                temp_file.write(audio_file.read())
                temp_file_path = temp_file.name
            target_path = temp_file_path
        else:
            # Si ya es una ruta de archivo local en texto
            target_path = audio_file

        # Transcripción estándar con faster-whisper
        segments, info = model.transcribe(target_path, language="es")
        texto = "".join(segment.text for segment in segments)
        
        return texto.strip()

    finally:
        # Asegurarse de eliminar el archivo temporal si fue creado
        if temp_file_path and os.path.exists(temp_file_path):
            try:
                os.remove(temp_file_path)
            except Exception:
                pass