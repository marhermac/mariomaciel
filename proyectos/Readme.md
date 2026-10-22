# 📂 Directorio de Proyectos | Mario Maciel

¡Bienvenido al catálogo de proyectos de mi portafolio! En este directorio centralizo desarrollos aplicados que combinan más de 15 años de experiencia en **Supply Chain, Gestión de Inventarios y Master Data**, con herramientas modernas de **Inteligencia Artificial Generativa, Data Engineering y Analítica de Datos**.

---

## 🚀 Proyectos Destacados

### 🎙️ 1. [AI Voice Translator (Traductor de Voz con IA)](./TraductorVoz_dev)
* **Categoría:** Inteligencia Artificial Generativa / Speech Processing
* **Descripción:** Aplicación web interactiva en tiempo real que captura voz en español, transcribe con modelos de IA, traduce de forma contextual al inglés y sintetiza la salida en audio nativo. Diseñada con arquitectura liviana y optimizada para la nube.
* **Tech Stack:** Python, Streamlit, `faster-whisper` (STT), `deep-translator`, `edge-tts` (TTS), NumPy, SoundFile.
* **Links:** [Ver Código y Documentación](./TraductorVoz_dev) | [Probar App en Streamlit Cloud](https://share.streamlit.io)

---

### 🛒 2. [Retail Pulse — Platform & Competitive Price Intelligence](../retail_pulse)
* **Categoría:** Price Intelligence / Supply Chain & Retail Analytics
* **Descripción:** Plataforma analítica para el monitoreo automatizado de precios, consolidación de matrices competitivas y generación de reportes ejecutivos entre las principales cadenas de retail de consumo masivo en Argentina (Carrefour, Coto y Jumbo).
* **Características Clave:** Ingesta vía APIs VTEX, matcheo por EAN-13 (comparaciones 1:1), motor analítico de brechas ($ y %) y generación de reportes ejecutivos en Excel con formato condicional corporativo.
* **Tech Stack:** Python 3.12, Pandas, OpenPyxl (Excel Automation), Requests / VTEX Rest APIs.
* **Outputs:** Informes ejecutivos descargables en la carpeta `outputs/` (`Informe_Ejecutivo_Carrefour_Overprice.xlsx`, `Coto`, `Jumbo`).
* **Links:** [Ver Directorio](../retail_pulse)
---

### 🧹 3. [Master Data Quality Assessment](../Proyecto_Master_Data_Quality)
* **Categoría:** Data Governance & Master Data Analytics
* **Descripción:** Evaluación de la calidad y exhaustividad de un archivo maestro de datos logísticos (34 registros, 75 atributos y 2,550 celdas analizadas) utilizado para la gestión de inventarios, almacenamiento y distribución.
* **Metodología & Hallazgos:** Perfilado de datos y evaluación por relevancia operativa. A pesar de una cobertura general del 37.33%, los atributos críticos para la operación (Logística y dimensiones) alcanzaron un 100% de completitud, demostrando que la calidad del dato se mide por su impacto directo en el negocio.
* **Tech Stack:** Excel / WPS Spreadsheets, Tablas Dinámicas, Métricas de Gobernanza y Data Profiling.
* **Links:** [Ver Directorio](../Proyecto_Master_Data_Quality)
---

### 📬 4. [Análisis Operacional & Logistics Delivery](../analisis-quejas-mail-delivery)
* **Categoría:** Exp### 📬 4. [Análisis de Quejas por Email — Empresa de Entregas a Domicilio](../analisis-quejas-mail-delivery)
* **Categoría:** Data Cleaning & Operational Text Analytics / Logística
* **Descripción:** Transformación de un dataset no estructurado de correos electrónicos (6 meses de reclamos en AMBA Norte) en datos estructurados y métricas operativas accionables para la toma de decisiones en logística y servicio al cliente.
* **Procesamiento & Clasificación:** Limpieza y estandarización de texto libre con Expresiones Regulares (Regex), parsing de fechas multiformato y clasificación *rule-based* (sin ML) en 5 categorías de reclamo (Retraso, Pedido incompleto, Mal estado, Repartidor y Facturación).
* **Tech Stack:** Python 3.x, Pandas, Regex, CSV Handling, Rule-Based Text Classification.
* **Outputs:** Datasets analíticos para dashboards (`ranking_quejas.csv`, `quejas_por_fecha.csv` y `quejas_por_zona.csv`).
* **Links:** [Ver Directorio](../analisis-quejas-mail-delivery)
---

### 🧹 5. [Data Cleaning Challenge: E-commerce Inventory](../limpieza-ecommerce)
* **Categoría:** Data Engineering / Data Cleaning & Transformation
* **Descripción:** Pipeline de limpieza, normalización y transformación de un dataset simulado de 5.000 registros y más de 100 columnas sobre inventario e-commerce proveniente de sucursales en Argentina y EE.UU., preparándolo para análisis en Power BI o Tableau.
* **Problemas Resueltos:** Estandarización geográfica (unificación de variantes con diccionarios de mapeo), conversión de precios en formato texto a `float`, normalización de fechas heterogéneas al estándar ISO y tratamiento de nulos y duplicados.
* **Tech Stack:** Python 3.x, Pandas, NumPy, Regular Expressions (Regex).
* **Outputs:** Dataset final depurado (`clean_data_final.csv`) generado mediante el script reproducible `limpieza.py`.
* **Links:** [Ver Directorio](../limpieza-ecommerce)
---

## 🛠️ Stack Tecnológico Utilizado en este Directorio

| Área | Tecnologías / Herramientas |
| :--- | :--- |
| **Lenguajes & Entornos** | Python 3, SQL, Jupyter Notebooks |
| **IA & Speech** | OpenAI Whisper (`faster-whisper`), `edge-tts`, `deep-translator` |
| **Análisis & Datos** | Pandas, NumPy, Data Profiling, Excel Avanzado |
| **Visualización & Web** | Streamlit, Plotly, Matplotlib, Seaborn |
| **Entorno & Despliegue** | Git, GitHub, Streamlit Community Cloud, PowerShell |

---

## 📌 Navegación del Repositorio

- ⬅️ **[Volver al Perfil Principal (Perfil / README General)](../README.md)**
- 💼 **[Ver Curriculum Vitae (CV)](../CV)**

---