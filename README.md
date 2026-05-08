# Proyecto de Análisis de Personas Desaparecidas en Colombia

## Descripción General

Este proyecto tiene como objetivo analizar el conjunto de datos histórico de personas desaparecidas en Colombia publicado por el portal oficial de datos abiertos del gobierno colombiano. El análisis busca identificar patrones sociales, demográficos, geográficos y temporales relacionados con las desapariciones registradas en el país.

El dataset utilizado corresponde a:

**“Desaparecidos en Colombia – Histórico marzo de 2026”**

La información proviene del portal de datos abiertos del Estado colombiano y contiene registros históricos asociados a personas desaparecidas, incluyendo variables demográficas, sociales, territoriales y judiciales.

---

# ¿Por qué se escogió este proyecto?

Este proyecto fue seleccionado debido a su gran impacto social, humano y analítico. La problemática de las desapariciones en Colombia representa una situación histórica compleja que involucra múltiples factores:

* Violencia y conflicto armado.
* Problemáticas sociales.
* Desplazamiento forzado.
* Trata de personas.
* Violencia intrafamiliar.
* Vulnerabilidad de ciertos grupos poblacionales.
* Falencias institucionales y judiciales.

Además del valor social del tema, el dataset permite realizar múltiples tipos de análisis de datos:

* Análisis estadístico.
* Visualización de datos.
* Minería de datos.
* Predicción de tendencias.
* Segmentación poblacional.
* Análisis temporal.
* Análisis geográfico.
* Detección de patrones.

Por lo tanto, el proyecto no solo tiene relevancia técnica, sino también una fuerte importancia ética y social.

---

# Objetivo General

Desarrollar un análisis exploratorio y estadístico sobre los registros históricos de personas desaparecidas en Colombia para identificar patrones relevantes asociados al comportamiento de las desapariciones.

---

# Objetivos Específicos

* Analizar las características demográficas de las personas desaparecidas.
* Identificar los grupos etarios más afectados.
* Evaluar diferencias por sexo y género.
* Analizar la distribución territorial de las desapariciones.
* Estudiar el comportamiento temporal de los casos.
* Identificar patrones relacionados con etnias, escolaridad y estado civil.
* Generar visualizaciones que faciliten la interpretación de los datos.
* Construir una base sólida para futuros modelos predictivos o análisis avanzados.

---

# Fuente de los Datos

Dataset oficial del portal de datos abiertos de Colombia:

* Datos Abiertos Colombia
* Categoría: Justicia y Derecho
* Nombre del dataset: “Desaparecidos en Colombia - Histórico marzo de 2026”

---

# Características del Dataset

## Cantidad de Variables

El dataset contiene un total de:

### 30 variables

Cada variable aporta información importante para comprender las características de las desapariciones registradas.

---

# Variables del Dataset

A continuación se describen todas las variables presentes en el conjunto de datos:

| #  | Variable                                           | Descripción                                                    |
| -- | -------------------------------------------------- | -------------------------------------------------------------- |
| 1  | ID                                                 | Identificador único del registro.                              |
| 2  | Entidad que realiza el registro de la desaparición | Institución encargada de registrar el caso.                    |
| 3  | Estado de la desaparición                          | Estado actual del caso de desaparición.                        |
| 4  | Clasificación de la desaparición                   | Tipo o categoría de la desaparición registrada.                |
| 5  | Sexo del desaparecido                              | Sexo biológico registrado de la persona desaparecida.          |
| 6  | Grupo mayor y menor de edad del desaparecido       | Clasificación general por mayoría o minoría de edad.           |
| 7  | Grupo de edad quinquenal del desaparecido          | Segmentación por rangos de edad de cinco años.                 |
| 8  | Grupo de edad judicial del desaparecido            | Clasificación judicial de la edad.                             |
| 9  | Ciclo vital del desaparecido                       | Etapa de vida de la persona desaparecida.                      |
| 10 | Estado civil del desaparecido                      | Estado civil registrado de la persona.                         |
| 11 | Escolaridad del desaparecido                       | Nivel educativo alcanzado.                                     |
| 12 | Identidad de género del desaparecido               | Identidad de género registrada.                                |
| 13 | Orientación sexual del desaparecido                | Orientación sexual registrada en el sistema.                   |
| 14 | Transgénero                                        | Indicación sobre condición transgénero.                        |
| 15 | Pueblo indígena del desaparecido                   | Pueblo indígena al que pertenece la persona.                   |
| 16 | Pertenencia étnica del desaparecido                | Grupo étnico registrado.                                       |
| 17 | Pertenencia grupal del desaparecido                | Grupo poblacional al que pertenece.                            |
| 18 | País de nacimiento del desaparecido                | País de origen de la persona desaparecida.                     |
| 19 | Fecha de la desaparición                           | Fecha exacta de ocurrencia de la desaparición.                 |
| 20 | Año de la desaparición                             | Año en el que ocurrió el caso.                                 |
| 21 | Mes de la desaparición                             | Mes en que ocurrió la desaparición.                            |
| 22 | Día de la desaparición                             | Día específico de la desaparición.                             |
| 23 | País de desaparición                               | País donde ocurrió el hecho.                                   |
| 24 | Departamento de desaparición                       | Departamento colombiano donde se registró el caso.             |
| 25 | Municipio de desaparición                          | Municipio donde ocurrió la desaparición.                       |
| 26 | Zona de desaparición                               | Zona urbana o rural asociada al caso.                          |
| 27 | Lugar de desaparición                              | Lugar específico relacionado con la desaparición.              |
| 28 | Presunto responsable de la desaparición            | Actor o posible responsable vinculado al caso.                 |
| 29 | Fecha de registro del caso                         | Fecha en la que el caso fue ingresado oficialmente al sistema. |
| 30 | Año de registro del caso                           | Año en que se realizó el registro oficial.                     |

---

# Importancia de las Variables

Las variables seleccionadas permiten abordar el fenómeno desde diferentes dimensiones:

## Dimensión Demográfica

Permite estudiar:

* Edad.
* Sexo.
* Estado civil.
* Escolaridad.
* Género.
* Orientación sexual.

Esto ayuda a identificar qué grupos poblacionales presentan mayor vulnerabilidad.

---

## Dimensión Territorial

Incluye:

* País.
* Departamento.
* Municipio.
* Zona.
* Lugar de desaparición.

Gracias a estas variables es posible construir mapas de calor, identificar regiones críticas y analizar comportamientos geográficos.

---

## Dimensión Temporal

Las variables relacionadas con fechas permiten:

* Analizar tendencias históricas.
* Detectar aumentos o disminuciones por años.
* Estudiar comportamientos mensuales.
* Identificar temporadas críticas.

---

## Dimensión Social

Variables como:

* Pertenencia étnica.
* Pueblo indígena.
* Pertenencia grupal.
* Identidad de género.

permiten estudiar desigualdades sociales y vulnerabilidad diferencial.

---

## Dimensión Judicial

Variables como:

* Estado de la desaparición.
* Clasificación.
* Presunto responsable.
* Entidad registradora.

permiten analizar el comportamiento institucional y judicial de los casos.

---

# Posibles Preguntas de Investigación

Este proyecto permite responder preguntas como:

* ¿Qué grupos de edad presentan mayor número de desapariciones?
* ¿Qué departamentos registran más casos?
* ¿Existen diferencias significativas entre hombres y mujeres desaparecidos?
* ¿Qué tendencias históricas presentan los casos?
* ¿Qué grupos sociales son más vulnerables?
* ¿Existen patrones temporales específicos?
* ¿Cómo varía la desaparición entre zonas urbanas y rurales?
* ¿Qué relación existe entre escolaridad y desaparición?

---

# Posibles Análisis a Realizar

## Análisis Exploratorio de Datos (EDA)

* Limpieza de datos.
* Detección de valores nulos.
* Distribución de variables.
* Identificación de outliers.
* Análisis descriptivo.

---

## Visualización de Datos

* Histogramas.
* Gráficas de barras.
* Gráficas temporales.
* Mapas geográficos.
* Diagramas circulares.
* Heatmaps.

---

## Estadística Descriptiva

* Frecuencias.
* Porcentajes.
* Medidas de tendencia central.
* Medidas de dispersión.

---

## Machine Learning (Posible Expansión)

A futuro, el proyecto podría ampliarse hacia:

* Modelos predictivos.
* Clasificación de riesgo.
* Clustering de regiones.
* Predicción temporal.
* Detección automática de patrones.

---

# Tecnologías Propuestas

Dependiendo del desarrollo final del proyecto, podrían utilizarse herramientas como:

## Lenguajes y Librerías

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn

---

## Herramientas de Visualización

* Power BI
* Tableau
* Plotly
* Dash

---

## Entornos de Desarrollo

* Jupyter Notebook
* Visual Studio Code
* Google Colab

---

# Metodología del Proyecto

El proyecto puede desarrollarse siguiendo las siguientes etapas:

## 1. Recolección de Datos

Obtención del dataset oficial desde el portal de datos abiertos.

---

## 2. Limpieza y Preparación

* Eliminación de inconsistencias.
* Tratamiento de datos nulos.
* Normalización.
* Conversión de formatos.

---

## 3. Exploración de Datos

* Estadísticas descriptivas.
* Visualización inicial.
* Identificación de patrones.

---

## 4. Análisis Profundo

* Correlaciones.
* Tendencias.
* Comparaciones regionales.
* Segmentaciones.

---

## 5. Presentación de Resultados

* Dashboards.
* Informes.
* Visualizaciones.
* Conclusiones.

---

# Impacto Esperado

El proyecto busca generar:

* Mayor comprensión sobre las desapariciones en Colombia.
* Información útil para análisis sociales.
* Evidencia estadística para investigaciones.
* Herramientas de apoyo para toma de decisiones.
* Conciencia sobre una problemática nacional.

---

# Conclusión

Este proyecto representa una oportunidad para aplicar técnicas de análisis de datos a una problemática real de alto impacto social. Gracias a la riqueza y amplitud del dataset, es posible realizar múltiples enfoques analíticos que permitan comprender mejor el fenómeno de las desapariciones en Colombia.

Además de fortalecer habilidades técnicas en ciencia de datos, visualización y análisis estadístico, el proyecto también aporta una perspectiva humana y social al uso de la tecnología y los datos.
