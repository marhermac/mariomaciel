from faster_whisper import WhisperModel

# Se carga una sola vez al iniciar el programa
model = WhisperModel(
    "base",
    device="cpu",
    compute_type="int8"
)

def speech_to_text(audio_file):

    segments, info = model.transcribe(
        audio_file,
        language="es"
    )

    texto = ""

    for segment in segments:
        texto += segment.text

    return texto.strip()