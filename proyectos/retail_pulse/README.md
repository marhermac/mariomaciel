# 🛒 Retail Pulse — Platform & Competitive Price Intelligence

**Retail Pulse** es una plataforma analítica desarrollada en Python diseñada para automatizar el monitoreo de precios, la consolidación de matrices competitivas y la generación de reportes ejecutivos entre las principales cadenas de retail de consumo masivo en Argentina (**Carrefour, Coto y Jumbo**).

## 🚀 Características Clave
- **Ingesta vía APIs VTEX:** Extracción automatizada de catálogo de eCommerce.
- **EAN-13 Matching:** Matcheo estricto por código universal de producto para garantizar comparaciones 1:1 limpias.
- **Motor Analítico de Brechas:** Cálculo automatizado de diferencias absolutas (`$`) y relativas (`%`) por marca y competidor.
- **Reporting Ejecutivo Automático:** Generación de informes en Excel con OpenPyxl formateados con semáforos condicionales y diseño corporativo por retail.

## 🛠️ Tech Stack
- **Lenguaje:** Python 3.12
- **Procesamiento de Datos:** Pandas
- **Reporting & Formatting:** OpenPyxl (Excel Automation)
- **Ingesta:** Requests / VTEX Rest APIs

## 📊 Estructura de Salida
El proyecto genera reportes ejecutivos listos para la toma de decisiones comerciales, Pricing y CRM:
- `Informe_Ejecutivo_Carrefour_Overprice.xlsx`
- `Informe_Ejecutivo_Coto_Overprice.xlsx`
- `Informe_Ejecutivo_Jumbo_Overprice.xlsx`