# 🎙️ AI Voice Translator — Intérprete y Traductor de Voz en Tiempo Real

> Aplicación web interactiva desarrollada en Python y Streamlit para la transcripción, traducción e interpretación de voz en tiempo real, optimizada para despliegue en la nube.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://traductorgratis.streamlit.app/)


---

## 🚀 Descripción del Proyecto

Esta aplicación permite capturar audio nativo desde el navegador en español, procesarlo mediante modelos avanzados de reconocimiento de voz (**Speech-to-Text**), traducirlo de forma precisa al inglés y generar automáticamente la respuesta hablada mediante síntesis de voz (**Text-to-Speech**).

Está diseñada con una arquitectura modular y eficiente, libre de dependencias rígidas de hardware local, lo que permite su ejecución fluida tanto en entornos locales como en **Streamlit Community Cloud**.

---

## 🛠️ Tecnologías Utilizadas

- **Frontend / Interfaz:** [Streamlit](https://streamlit.io/) (captura y reproducción de audio web nativa).
- **Speech-to-Text (STT):** `faster-whisper` (Transcripción de voz de alta precisión basada en OpenAI Whisper).
- **Traducción:** `deep-translator` (Motor multilenguaje con tolerancia a fallos y reintentos automáticos).
- **Text-to-Speech (TTS):** `edge-tts` (Síntesis de voz natural y fluida en tiempo real).
- **Procesamiento de Audio:** `soundfile` y `numpy`.

---

## ✨ Características Principales

1. **Captura Web Nativa:** Grabación directa desde el micrófono del navegador o subida de archivos de audio sin requerir drivers de sonido locales (`PortAudio`).
2. **Transcripción Robusta:** Procesamiento optimizado de voz a texto en español usando Whisper.
3. **Traducción Estable:** Manejo de excepciones y reintentos automáticos para garantizar alta disponibilidad en la traducción hacia el inglés.
4. **Respuesta Auditiva Fluida:** Generación inmediata de audio en inglés con voces naturales para facilitar el entrenamiento auditivo y la comunicación.
5. **Estructura Modular:** Código limpio organizado en módulos independientes (`audio/`, `speech/`, `translator/`, `utils/`).

---

## 📁 Estructura del Repositorio

```text
proyectos/TraductorVoz_dev/
│
├── audio/            # Funciones para captura y manejo de archivos de audio
├── speech/           # Módulos de STT (faster-whisper) y TTS (edge-tts)
├── translator/       # Lógica de traducción e integración con APIs
├── utils/            # Funciones auxiliares y logging
├── app_streamlit.py  # Script principal de la aplicación Streamlit
├── requirements.txt  # Dependencias optimizadas para despliegue en la nube
└── README.md         # Documentación del proyecto

# 1. Clonar el repositorio completo
git clone https://github.com/marhermac/mariomaciel.git

# 2. Entrar a la carpeta específica del traductor
cd mariomaciel/proyectos/TraductorVoz_dev

# 3. Crear y activar el entorno virtual (en Windows)
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# 4. Instalar las dependencias
pip install -r requirements.txt

# 5. Ejecutar la app de Streamlit
streamlit run app_streamlit.py