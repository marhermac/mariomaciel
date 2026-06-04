Evaluación de la calidad de los datos de un archivo maestro de logística

Resumen del proyecto



Este proyecto analiza la calidad y la exhaustividad de un archivo maestro de datos logísticos utilizado para la gestión de inventarios, el almacenamiento y la distribución.



El objetivo es evaluar la calidad de la información disponible, identificar los datos faltantes y determinar si los atributos más relevantes para la toma de decisiones operativas se mantienen correctamente.



Descripción del conjunto de datos



El conjunto de datos contiene información maestra de productos anonimizada procedente de las operaciones logísticas.



Tamaño del conjunto de datos

Registros analizados: 34

Atributos analizados: 75

Total de celdas evaluadas: 2550

Información disponible

Códigos de producto

Descripciones de producto

Familias y categorías de productos

Códigos de barras

Dimensiones

Información de peso

Información de volumen

Datos de ubicación del almacén

Parámetros de inventario

Información del cliente

Atributos financieros

Datos de paletización

Metodología



El análisis se desarrolló en cuatro etapas:



1\. Perfilado de datos



Se realizó una evaluación inicial para determinar:



Número de registros

Número de atributos

Total de celdas analizadas

Valores faltantes

Información disponible

2\. Evaluación de la cobertura de datos



El índice de cobertura general se calculó mediante:



Índice de cobertura = Celdas con información / Total de celdas



Resultados:

Celdas con información: 952

Celdas vacías: 1598

Índice de cobertura general: 37,33 %

3\. Clasificación de atributos



Los 75 atributos se clasificaron según su relevancia operativa.



Resultados de la clasificación

Nivel de relevancia Número de atributos

Crítico 16

Alto 31

Medio 8

Bajo 20

Total 75



Se identificaron un total de 47 atributos (Críticos + Altos) que impactan directamente en las operaciones de logística e inventario.



4\. Análisis de cobertura por categoría de negocio



Los atributos se agruparon en categorías funcionales:



Identificación de materiales

Clasificación de materiales

Logística y dimensiones

Inventario y reabastecimiento

Organización y clientes

Paletización



La cobertura se evaluó a nivel de categoría para determinar dónde se concentran los problemas de calidad de los datos.



Principales hallazgos

Cobertura general de datos



Aunque el conjunto de datos presenta una tasa de cobertura general relativamente baja (37,33 %), el análisis mostró que la calidad de los datos varía significativamente según el área de negocio.



Cobertura por categoría

Categoría Cobertura promedio

Logística y dimensiones 100,00 %

Identificación de materiales 71,43 %

Organización y clientes 71,43 %

Inventario y reabastecimiento 40,00 %

Clasificación de materiales 33,33 %

Paletización 0,00 %



Observaciones principales



Los atributos de logística muestran el mayor nivel de completitud.

Los datos de identificación de materiales presentan niveles de cobertura aceptables.

La información relacionada con el inventario muestra oportunidades de mejora.

Los atributos de paletización no están completos.

La calidad de los datos es desigual entre las categorías y debe gestionarse según su relevancia para el negocio. Impacto en el negocio



La calidad de los datos maestros afecta directamente a:



Precisión del inventario

Operaciones de almacén

Trazabilidad del producto

Utilización del espacio

Planificación de reabastecimiento

Visibilidad de la cadena de suministro



Los datos maestros incompletos o inconsistentes pueden generar ineficiencias operativas y reducir la fiabilidad en la toma de decisiones.



Herramientas utilizadas

Microsoft Excel / Hoja de cálculo WPS

Tablas dinámicas

Técnicas de perfilado de datos

Métricas de calidad de datos



Conclusión



El análisis reveló que, si bien la cobertura general de datos es limitada, la información más relevante para las operaciones presenta una calidad significativamente superior a la media del conjunto de datos.



Esto subraya la importancia de evaluar la calidad de los datos no solo en función de la exhaustividad general, sino también de la relevancia para el negocio de cada atributo.



La metodología aplicada proporciona un marco práctico para evaluar la calidad de los datos maestros en entornos de logística y cadena de suministro.

