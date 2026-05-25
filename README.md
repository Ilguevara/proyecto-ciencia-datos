# Proyecto de Análisis de Víctimas por Minas Antipersonal y Municiones sin Explotar en Colombia

## Descripción General

Este proyecto tiene como objetivo analizar el conjunto de datos relacionado con víctimas de accidentes ocasionados por minas antipersonal (MAP), municiones sin explotar (MUSE) y eventos asociados al desminado militar en Colombia.

La información proviene del portal oficial de datos abiertos del gobierno colombiano y contiene registros históricos sobre personas afectadas por este tipo de eventos, incluyendo variables geográficas, demográficas y sociales.

El análisis permitirá identificar patrones territoriales, temporales y poblacionales asociados a una de las problemáticas más sensibles derivadas del conflicto armado colombiano.

---

# ¿Por qué se escogió este proyecto?

Este proyecto fue seleccionado debido a la gran relevancia social, histórica y humanitaria que tienen las minas antipersonal en Colombia.

Durante décadas, el conflicto armado dejó miles de víctimas civiles y militares afectadas por explosivos sembrados en distintas regiones del país. Las minas antipersonal han impactado especialmente zonas rurales, comunidades vulnerables y territorios históricamente afectados por la violencia.

Además del impacto social, este dataset permite desarrollar múltiples análisis relacionados con:

- Distribución territorial del conflicto.
- Identificación de zonas críticas.
- Análisis temporal de eventos.
- Caracterización demográfica de víctimas.
- Estudios geoespaciales.
- Visualización de datos.
- Análisis estadístico.
- Construcción de mapas y dashboards.

El proyecto combina ciencia de datos con una problemática real de alto impacto nacional.

---

# Objetivo General

Realizar un análisis exploratorio y estadístico sobre los registros de víctimas por minas antipersonal y municiones sin explotar en Colombia para identificar patrones geográficos, temporales y demográficos.

---

# Objetivos Específicos

- Identificar los departamentos con mayor cantidad de accidentes.
- Analizar la evolución temporal de los eventos.
- Estudiar diferencias entre víctimas civiles y fuerza pública.
- Evaluar la distribución entre zonas rurales y urbanas.
- Analizar grupos de edad más afectados.
- Identificar posibles patrones territoriales.
- Generar visualizaciones geográficas y estadísticas.
- Comprender el impacto social del conflicto armado.

---

# Fuente de los Datos

Dataset oficial del portal de datos abiertos de Colombia:

- Datos Abiertos Colombia
- Categoría: Gobierno y Seguridad
- Dataset relacionado con víctimas de minas antipersonal y municiones sin explotar

[Datos Abiertos Colombia](https://www.datos.gov.co/d/yhxn-eqqw?utm_source=chatgpt.com)

---

# Características del Dataset

## Cantidad de Variables

El dataset contiene un total de:

### 18 variables

Estas variables permiten realizar análisis completos desde dimensiones geográficas, sociales y temporales.

---

# Variables del Dataset


| #   | Variable               | Descripción                                                    |
| --- | ---------------------- | -------------------------------------------------------------- |
| 1   | departamento           | Departamento donde ocurrió el accidente.                       |
| 2   | codigodanedepartamento | Código DANE del departamento.                                  |
| 3   | municipio              | Municipio donde ocurrió el evento.                             |
| 4   | codigodanemunicipio    | Código DANE del municipio.                                     |
| 5   | tipoarea               | Indica si el evento ocurrió en zona rural o urbana.            |
| 6   | sitio                  | Lugar específico donde ocurrió el accidente.                   |
| 7   | ano                    | Año del evento.                                                |
| 8   | mes                    | Mes del evento.                                                |
| 9   | rangoedad              | Clasificación de edad de la víctima.                           |
| 10  | grupoetnico            | Grupo étnico al que pertenece la víctima.                      |
| 11  | condicion              | Define si la víctima pertenece a la fuerza pública o es civil. |
| 12  | estado                 | Estado de la víctima después del evento (herido o muerto).     |
| 13  | genero                 | Género de la víctima.                                          |
| 14  | latitudcabecera        | Latitud del lugar del evento.                                  |
| 15  | longitudcabecera       | Longitud del lugar del evento.                                 |
| 16  | tipoevento             | Tipo de evento relacionado con minas o municiones.             |
| 17  | ubicacion              | Coordenadas geográficas del evento.                            |
| 18  | actividad              | Actividad que realizaba la víctima antes del accidente.        |


---

# Importancia de las Variables

## Dimensión Geográfica

Las variables geográficas permiten:

- Identificar regiones más afectadas.
- Construir mapas de calor.
- Analizar distribución territorial.
- Detectar zonas de alto riesgo.

Variables importantes:

- departamento
- municipio
- latitudcabecera
- longitudcabecera
- ubicacion

---

## Dimensión Temporal

Las variables temporales permiten:

- Analizar tendencias históricas.
- Identificar años críticos.
- Estudiar evolución del conflicto.
- Relacionar eventos con procesos de paz.

Variables importantes:

- ano
- mes

---

## Dimensión Social y Demográfica

Permite analizar:

- Edad de las víctimas.
- Género.
- Condición civil o militar.
- Pertenencia étnica.

Variables importantes:

- rangoedad
- genero
- grupoetnico
- condicion

---

## Dimensión del Evento

Estas variables ayudan a comprender el contexto del accidente:

- tipoevento
- actividad
- estado
- sitio

Gracias a esto es posible estudiar cómo y bajo qué circunstancias ocurren los eventos.

---

# Posibles Preguntas de Investigación

Este proyecto permite responder preguntas como:

- ¿Qué departamentos presentan más accidentes?
- ¿La mayoría de eventos ocurren en zonas rurales o urbanas?
- ¿Qué grupos poblacionales son más afectados?
- ¿Existen años con incrementos significativos?
- ¿Qué tipo de víctimas predominan: civiles o fuerza pública?
- ¿Cuáles son las principales actividades realizadas antes del accidente?
- ¿Qué regiones siguen presentando altos niveles de riesgo?

---

# Posibles Análisis a Realizar

## Análisis Exploratorio de Datos (EDA)

- Limpieza de datos.
- Tratamiento de valores nulos.
- Distribución de variables.
- Estadísticas descriptivas.
- Detección de inconsistencias.

---

## Visualización de Datos

- Histogramas.
- Gráficas de barras.
- Series temporales.
- Mapas geográficos.
- Heatmaps.
- Dashboards interactivos.

---

## Estadística Descriptiva

- Frecuencias.
- Porcentajes.
- Distribuciones.
- Comparaciones regionales.

---

## Análisis Geoespacial

Debido a las coordenadas geográficas, el dataset permite:

- Construcción de mapas interactivos.
- Identificación de zonas críticas.
- Análisis espacial de eventos.
- Georreferenciación de accidentes.

---

# Tecnologías Propuestas

## Lenguajes y Librerías

- Python
- Pandas
- NumPy
- Matplotlib
- Plotly
- Scikit-learn
- GeoPandas

---

## Herramientas de Visualización

- Power BI
- Tableau
- Folium
- Plotly Dash

---

## Entornos de Desarrollo

- Jupyter Notebook
- Google Colab
- Visual Studio Code

---

# Metodología del Proyecto

## 1. Recolección de Datos

Obtención del dataset desde el portal oficial de datos abiertos.

---

## 2. Limpieza y Preparación

- Corrección de inconsistencias.
- Eliminación de duplicados.
- Tratamiento de valores faltantes.
- Conversión de formatos.

---

## 3. Exploración de Datos

- Estadísticas descriptivas.
- Identificación de patrones.
- Visualización preliminar.

---

## 4. Análisis Profundo

- Comparaciones regionales.
- Tendencias históricas.
- Relación entre variables.
- Análisis geográfico.

---

## 5. Presentación de Resultados

- Informes.
- Dashboards.
- Visualizaciones interactivas.
- Conclusiones.

---

# Impacto Esperado

Este proyecto busca aportar:

- Comprensión del impacto territorial de las minas antipersonal.
- Evidencia estadística sobre víctimas del conflicto.
- Información útil para estudios sociales y humanitarios.
- Apoyo a investigaciones académicas.
- Conciencia sobre las consecuencias del conflicto armado.

---

# Conclusiones

El análisis de víctimas por minas antipersonal y municiones sin explotar es especialmente relevante para Colombia debido a la larga historia de conflicto armado interno que ha afectado múltiples regiones del país.

Las minas antipersonal representan una de las consecuencias más graves y persistentes de la violencia, afectando principalmente comunidades rurales, campesinos, población civil y miembros de la fuerza pública. Incluso años después de muchos enfrentamientos armados, estos artefactos continúan generando accidentes y limitando el desarrollo de distintas regiones.

Este proyecto permite comprender cómo se distribuyen territorialmente los eventos, cuáles son los grupos más afectados y cómo ha evolucionado la problemática a lo largo del tiempo.

Además, el uso de ciencia de datos y análisis geoespacial ayuda a generar información valiosa para procesos de desminado, prevención, políticas públicas y estudios relacionados con la construcción de paz y la seguridad en Colombia.