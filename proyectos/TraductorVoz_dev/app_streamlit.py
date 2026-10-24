import os
import tempfile
import asyncio
import streamlit as st
import inspect

# Importamos la lógica de tus módulos existentes
from speech.stt import speech_to_text
from translator.translator import translate_text
from speech.tts import text_to_speech

# Configuración básica de la interfaz
st.set_page_config(
    page_title="Traductor de Voz (ES -> EN)",
    page_icon="🎙️",
    layout="centered"
)

st.title("🎙️ Traductor de Voz GRATIS")
st.subheader("Español ➡️ Inglés")

st.markdown("""
Graba tu voz en español o sube un archivo de audio para obtener la traducción en texto y voz en inglés.
Practica tu conversacion o Aprende con tus propias palabras """)

# Selector de modo de entrada
modo = st.radio(
    "Selecciona el método de entrada de audio:",
    ["Grabar con Micrófono", "Subir Archivo de Audio"],
    horizontal=True
)

audio_bytes = None

if modo == "Grabar con Micrófono":
    audio_bytes = st.audio_input("Presiona para grabar")
else:
    archivo_subido = st.file_uploader(
        "Sube un archivo de audio (.wav, .mp3, .m4a)", 
        type=["wav", "mp3", "m4a"]
    )
    if archivo_subido is not None:
        audio_bytes = archivo_subido.read()

# Procesamiento cuando se recibe audio
if audio_bytes:
    st.audio(audio_bytes, format="audio/wav")
    
    if st.button("🚀 Traducir ahora", type="primary"):
        with st.spinner("Procesando audio y generando traducción..."):
            
            # Guardamos temporalmente el audio de entrada para enviarlo a STT
            with tempfile.NamedTemporaryFile(delete=False, suffix=".wav") as temp_in:
                temp_in.write(audio_bytes if isinstance(audio_bytes, bytes) else audio_bytes.getvalue())
                ruta_temp_in = temp_in.name

            try:
                # 1. Transcripción (Speech-to-Text)
                texto_reconocido = speech_to_text(ruta_temp_in)
                
                if not texto_reconocido:
                    st.error("No se pudo reconocer texto en el audio ingresado.")
                else:
                    # 2. Traducción (Español a Inglés)
                    traduccion = translate_text(texto_reconocido, source="es", target="en")

                    # Mostrar resultados de texto
                    col1, col2 = st.columns(2)
                    with col1:
                        st.markdown("### 🗣️ Texto original")
                        st.info(texto_reconocido)

                    with col2:
                        st.markdown("### 🇬🇧 Traducción")
                        st.success(traduccion)

                    # 3. Síntesis de voz (Text-to-Speech)
                    st.markdown("### 🔊 Audio Traducido")
                    
                    # Manejo asíncrono o sincrónico para `text_to_speech`
                    # DESPUÉS:

                    if inspect.iscoroutinefunction(text_to_speech):
                        ruta_voz = asyncio.run(text_to_speech(traduccion))
                    else:
                        ruta_voz = text_to_speech(traduccion)

                    if ruta_voz and os.path.exists(ruta_voz):
                        st.audio(ruta_voz, format="audio/mp3")
                    else:
                        st.warning("No se pudo generar la voz traducida.")

            except Exception as e:
                st.error(f"Ocurrió un error durante el procesamiento: {e}")
            
            finally:
                # Limpieza del archivo temporal de entrada
                if os.path.exists(ruta_temp_in):
                    os.remove(ruta_temp_in)


st.markdown("""
Creado por Mario Maciel mas info en: https://marhermac.github.io/mariomaciel/  """)
