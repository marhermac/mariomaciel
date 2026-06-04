# 📊 Evaluación de la Calidad de Datos - Archivo Maestro de Logística


Este proyecto analiza la **calidad y exhaustividad** de un archivo maestro de datos logísticos utilizado para la gestión de inventarios, almacenamiento y distribución. El objetivo es identificar datos faltantes y medir el impacto de los atributos críticos en la toma de decisiones operativas.

---

## 📈 Resumen Ejecutivo

A pesar de una cobertura general baja (**37.33%**), los datos críticos para la operación presentan niveles óptimos de completitud. Esto demuestra que la calidad del dato debe medirse por su **relevancia para el negocio** y no solo por volumen general.

---

## 📑 Índice
1. [Descripción del Conjunto de Datos](#-descripción-del-conjunto-de-datos)
2. [Metodología](#-metodología)
3. [Principales Hallazgos](#-principales-hallazgos)
4. [Impacto en el Negocio](#-impacto-en-el-negocio)
5. [Herramientas Utilizadas](#-herramientas-utilizadas)
6. [Visualizaciones](#-visualizaciones)

---

## 🗃️ Descripción del Conjunto de Datos

El dataset contiene información maestra de productos anonimizada procedente de operaciones logísticas reales.


| Dimensión | Métrica |
| :--- | :--- |
| **Registros analizados** | 34 |
| **Atributos analizados** | 75 |
| **Total de celdas evaluadas** | 2,550 |

### 🔍 Información Disponible:
*   Códigos y descripciones de producto.
*   Familias, categorías y códigos de barras.
*   Dimensiones, peso y volumen.
*   Ubicaciones de almacén y parámetros de inventario.
*   Datos de paletización, clientes y atributos financieros.

---

## ⚙️ Metodología

El análisis se desarrolló en **cuatro etapas operativas**:

### 1. Perfilado de Datos
Evaluación inicial para determinar volumen de registros, atributos, celdas totales y detección de valores faltantes.

### 2. Evaluación de Cobertura
Cálculo del índice de cobertura general mediante la fórmula:
$$\text{Índice de Cobertura} = \frac{\text{Celdas con Información}}{\text{Total de Celdas}}$$

*   **Celdas con información:** 952
*   **Celdas vacías:** 1,598
*   **Índice general:** `37.33%`

### 3. Clasificación de Atributos
Se clasificaron los 75 atributos según su nivel de relevancia operativa:


| Nivel de Relevancia | Número de Atributos | Impacto Operativo |
| :---: | :---: | :--- |
| **Crítico** | 16 | Alta prioridad / Bloqueante |
| **Alto** | 31 | Impacto directo en procesos |
| **Medio** | 8 | Informativo / Secundario |
| **Bajo** | 20 | Despreciable a corto plazo |
| **Total** | **75** | **47 Atributos Clave (Crítico + Alto)** |

### 4. Cobertura por Categoría de Negocio
Agrupación de atributos en categorías funcionales para identificar cuellos de botella de calidad de datos.

---

## 📊 Principales Hallazgos

### Cobertura por Categoría Funcional


| Categoría | Cobertura Promedio | Estado |
| :--- | :---: | :---: |
| 📦 Logística y dimensiones | **100.00%** | 🟢 Excelente |
| 🆔 Identificación de materiales | **71.43%** | 🟡 Aceptable |
| 🏢 Organización y clientes | **71.43%** | 🟡 Aceptable |
| 🔄 Inventario y reabastecimiento | **40.00%** | 🟠 Crítico |
| 🗂️ Clasificación de materiales | **33.33%** | 🟠 Crítico |
| 🪵 Paletización | **0.00%** | 🔴 Sin Datos |

### 💡 Observaciones Clave:
*   Los atributos estrictamente **logísticos** muestran una completitud perfecta.
*   La información de **inventario** representa la mayor oportunidad de mejora inmediata.
*   Los campos de **paletización** se encuentran totalmente vacíos y requieren intervención de TI.

---

## ⚠️ Impacto en el Negocio

La falta de consistencia en el archivo maestro afecta directamente los siguientes pilares:

*   **Precisión del inventario** y planificación de reabastecimiento.
*   **Eficiencia en operaciones** de almacén (picking/slotting).
*   **Trazabilidad** del producto y visibilidad de la cadena de suministro.
*   **Optimización del espacio** de almacenamiento por falta de datos de paletización.

---

## 🛠️ Herramientas Utilizadas

*   **Microsoft Excel / Hoja de cálculo WPS** (Procesamiento base).
*   **Tablas dinámicas** para la segmentación de atributos.
*   **Métricas de calidad de datos** aplicadas a operaciones logísticas.

---

## 🖼️ Visualizaciones


<p align="center">
  <img src="proyectos/Proyecto_Master_Data_Quality/imagenes/grafico indice cobertura.png" alt="Gráfico de Cobertura por Categoría" width="45%"/>
  <img src="proyectos/Proyecto_Master_Data_Quality/imagenes/grafico promedio de cobertura de informacion.png" alt="Gráfico de Clasificación de Atributos" width="45%"/>
</p>

---

💻 Diseñado  para la optimización de procesos logísticos.
