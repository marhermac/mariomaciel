import os
import tempfile
from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.responses import FileResponse, JSONResponse, HTMLResponse
from fastapi.middleware.cors import CORSMiddleware
from faster_whisper import WhisperModel
from deep_translator import MyMemoryTranslator
import edge_tts

app = FastAPI(
    title="Voice-to-Voice Translator API",
    version="1.3"
)

# Configuración de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

MODEL_SIZE = "base"
print(f"Cargando modelo Whisper ({MODEL_SIZE})...")
model = WhisperModel(MODEL_SIZE, device="cpu", compute_type="int8")
print("¡Modelo cargado correctamente!")

# Carpeta temporal para guardar los audios generados y poder servirlos
TEMP_DIR = tempfile.gettempdir()

@app.post("/api/translate")
async def translate_voice(file: UploadFile = File(...)):
    with tempfile.NamedTemporaryFile(delete=False, suffix=".wav", dir=TEMP_DIR) as temp_in:
        content = await file.read()
        temp_in.write(content)
        temp_in_path = temp_in.name

    output_filename = f"translated_{os.path.basename(temp_in_path)}.mp3"
    output_audio_path = os.path.join(TEMP_DIR, output_filename)

    try:
        # Transcribir audio en español con faster-whisper
        segments, info = model.transcribe(temp_in_path, language="es")
        spanish_text = "".join([segment.text for segment in segments]).strip()

        if not spanish_text:
            raise HTTPException(status_code=400, detail="No se detectó voz clara en el audio.")

        if len(spanish_text) > 450:
            spanish_text = spanish_text[:450]

        # Traducir al inglés usando MyMemoryTranslator
        english_text = MyMemoryTranslator(source='spanish', target='english').translate(spanish_text)

        if len(english_text) > 450:
            english_text = english_text[:450]

        # Generar audio en inglés con edge-tts
        communicate = edge_tts.Communicate(english_text, "en-US-AriaNeural")
        await communicate.save(output_audio_path)
        
    except Exception as e:
        if os.path.exists(temp_in_path):
            os.remove(temp_in_path)
        raise HTTPException(status_code=500, detail=f"Error en el pipeline de IA: {str(e)}")

    finally:
        if os.path.exists(temp_in_path):
            os.remove(temp_in_path)

    return JSONResponse(content={
        "spanish_text": spanish_text,
        "english_text": english_text,
        "audio_url": f"/api/audio/{output_filename}"
    })

@app.get("/api/audio/{filename}")
async def get_audio(filename: str):
    file_path = os.path.join(TEMP_DIR, filename)
    if os.path.exists(file_path):
        return FileResponse(file_path, media_type="audio/mpeg")
    raise HTTPException(status_code=404, detail="Audio no encontrado")

# Ruta para servir tu index.html principal en Hugging Face
@app.get("/", response_class=HTMLResponse)
async def read_index():
    if os.path.exists("index.html"):
        with open("index.html", "r", encoding="utf-8") as f:
            return f.read()
    return "<h1>Bienvenido a la API del Traductor de Voz a Voz</h1><p>El archivo index.html no se encontró en la raíz.</p>"