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
    # Si es un objeto en memoria de Streamlit (UploadedFile/BytesIO)
    if hasattr(audio_file, "read"):
        with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_file:
            temp_file.write(audio_file.read())
            temp_file_path = temp_file.name
        
        try:
            segments, info = model.transcribe(temp_file_path, language="es")
            texto = "".join(segment.text for segment in segments)
        finally:
            # Limpiamos el archivo temporal del disco
            if os.path.exists(temp_file_path):
                os.remove(temp_file_path)
    else:
        # Si ya es una ruta de archivo en formato string
        segments, info = model.transcribe(audio_file, language="es")
        texto = "".join(segment.text for segment in segments)

    return texto.strip()