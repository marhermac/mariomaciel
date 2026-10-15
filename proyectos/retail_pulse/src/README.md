# 📂 Retail Pulse - Source Code (`src/`)

Esta carpeta contiene el núcleo lógico de **Retail Pulse**, encargado del procesamiento de datos, análisis de diferencias de precios (*price intelligence*) y generación de reportes ejecutivos automatizados para la inteligencia comercial.

---

## 📜 Descripción de Scripts y Archivos

### 🔍 Análisis de Diferencias y Variaciones
* **`analyze_coto_diff.py`**: Script enfocado en procesar y analizar las variaciones, fluctuaciones y diferencias de precios detectadas en el catálogo de productos de Coto frente a periodos anteriores o referencias de mercado.
* **`analyze_jumbo_diff.py`**: Script homólogo orientado al análisis de diferencias de precios para la cadena Jumbo, permitiendo identificar brechas, aumentos o caídas de precios específicos.

### 📊 Generación de Reportes Ejecutivos (Excel)
* **`generate_excel_report.py`**: Módulo principal para la consolidación y formateo de los reportes ejecutivos en formato Excel (`.xlsx`), estructurando los datos para una lectura gerencial clara.
* **`generate_excel_report_coto.py`**: Script especializado en compilar los datos específicos de Coto y darles formato en un reporte de Excel orientado a la toma de decisiones.
* **`generate_excel_report_jumbo.py`**: Script especializado en estructurar, estilizar y generar el reporte ejecutivo en Excel con la información procesada de Jumbo.

### 🛠️ Procesamiento y Matching de Datos
* **`vtex_matcher_by_coto.py`**: Script de lógica de negocio que utiliza tecnologías de parsing/matching para emparejar y unificar los códigos de productos y SKUs basados en la estructura de VTEX utilizando los datos de Coto.

### 📋 Archivos de Datos Base
* **`retail_pulse_comparison_matrix_20261013.csv`**: Matriz histórica de comparación de precios en formato CSV (generada el 13/10/2026) que sirve como insumo o base de datos estructurada para los análisis y reportes de la herramienta.

---

## 🚀 Flujo de Trabajo Sugerido
1. Se ejecutan los scrapers o matchers (como `vtex_matcher_by_coto.py`) para consolidar las matrices base como la de octubre.
2. Se procesan las variaciones utilizando los scripts de análisis (`analyze_coto_diff.py` / `analyze_jumbo_diff.py`).
3. Se compilan y exportan los resultados ejecutivos mediante los generadores de reportes (`generate_excel_report_*.py`).