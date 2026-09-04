# Churn Intelligence B2B SaaS - Telecom

**Plataforma de soporte para Fidelización, Atención al Cliente y Analítica de Negocios.**

Proyecto del módulo **Analista de Datos 2** de la Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial, Instituto Superior Politécnico de Córdoba (ISPC).

**Docente:** Sol Del Valle Figueroa

**Título del proyecto:** Churn Intelligence SaaS

**Integrantes:**

* Amaya, Brenda
* Amaya, Paula
* Cortez, Valeria
* Manrique Aguad, Agustín
* Martinez, Cristian
* Sudañez, Isaias Emanuel

---

# Introducción del Proyecto

Este repositorio contiene el desarrollo del producto **Churn Intelligence**, concebido como una solución de software **B2B SaaS (Software as a Service) multi-tenant** para la gestión analítica y operativa de la retención de clientes.

Como estrategia académica y técnica de validación del **Producto Mínimo Viable (MVP)**, el primer vertical de negocio considerado corresponde a la industria de **Telecomunicaciones (Telefonía)**, utilizando el dataset `telecom_dirty.csv` para la limpieza, exploración, modelado predictivo y visualización del riesgo de abandono.

El proyecto busca integrar el análisis de datos, la ciencia de datos y el desarrollo de producto para transformar información de clientes en resultados que puedan apoyar la toma de decisiones relacionadas con el churn.

Este documento sintetiza la especificación y planificación inicial del proyecto, abarcando las fases de **Descubrimiento y Comprensión del Negocio, Definición del Producto, Factibilidad y Caso de Negocio, y Requisitos y Alcance**.

---

# 1. Descubrimiento y Comprensión del Negocio

## 1.1 Contexto del Problema y Problem Statement

La gestión y reducción del **churn (abandono)** representa un desafío relevante para las organizaciones de telecomunicaciones.

El Problem Statement de trabajo define:

> La empresa de telecomunicaciones necesita mejorar su capacidad para identificar y gestionar tempranamente a los clientes con riesgo de abandono, debido a la dificultad de transformar de manera sistemática los datos disponibles de clientes, comportamiento, interacción y servicio en información predictiva y accionable para las áreas de Fidelización, Atención al Cliente y Analítica de Negocios.

El problema no se limita al desarrollo de un modelo predictivo aislado, sino que contempla un ciclo de trabajo más amplio:

```text
DATOS
  ↓
ANÁLISIS
  ↓
IDENTIFICACIÓN DE PATRONES
  ↓
PREDICCIÓN DE CHURN
  ↓
SEGMENTACIÓN
  ↓
INTERPRETACIÓN
  ↓
INSIGHT
  ↓
DECISIÓN
  ↓
ACCIÓN DE RETENCIÓN
```

## 1.2 Proceso de Negocio Objeto de Soporte

El producto busca brindar soporte al siguiente proceso conceptual:

```text
GESTIÓN DE CLIENTES
        ↓
CAPTURA DE DATOS
        ↓
ANÁLISIS DEL COMPORTAMIENTO
        ↓
DETECCIÓN DE SEÑALES
        ↓
IDENTIFICACIÓN DE RIESGO
        ↓
PRIORIZACIÓN
        ↓
ACCIÓN DE FIDELIZACIÓN
        ↓
SEGUIMIENTO
        ↓
RESULTADO
```

Durante la etapa de descubrimiento se estableció que el funcionamiento concreto de este proceso dentro de una organización deberá ser relevado y validado posteriormente.

## 1.3 Pain Points Identificados

### Pain Point 01 — Detección tardía del riesgo de abandono

El riesgo de abandono puede manifestarse mediante diferentes señales antes de que ocurra el churn. Si estas señales no se detectan oportunamente, la intervención puede producirse demasiado tarde.

**Necesidad:** Detectar anticipadamente clientes que presenten señales compatibles con riesgo de abandono.

**Oportunidad:** Desarrollar un mecanismo de scoring de riesgo que permita identificar y monitorear tempranamente estos casos.

```text
SEÑALES
   ↓
MODELO
   ↓
CHURN SCORE
   ↓
PRIORIZACIÓN
```

### Pain Point 02 — Falta de priorización de clientes

No todos los clientes presentan el mismo nivel de riesgo ni representan el mismo valor para la organización. Cuando la cartera es amplia, analizar todos los casos con el mismo nivel de atención dificulta concentrar los esfuerzos donde pueden generar mayor impacto.

**Necesidad:** Determinar qué clientes requieren mayor prioridad de atención.

**Oportunidad:** Combinar el riesgo de churn con variables de valor y segmentación para generar una priorización de la cartera.

```text
RIESGO DE CHURN
        +
VALOR DEL CLIENTE
        +
SEGMENTO
        ↓
MATRIZ DE PRIORIDAD
```

### Pain Point 03 — Información distribuida

La información necesaria para comprender el comportamiento de un cliente puede provenir de diferentes fuentes y sistemas. Esta distribución dificulta construir una visión integrada de la relación del cliente con la organización.

**Necesidad:** Contar con una visión consolidada de la información relevante del cliente.

**Oportunidad:** Construir una capa analítica capaz de integrar las variables disponibles para el análisis.

```text
CLIENTE
  ├── Facturación
  ├── Servicio
  └── Atención
          ↓
       ANÁLISIS
```

Las fuentes concretas de información quedan sujetas a relevamiento y validación.

### Pain Point 04 — Dificultad para explicar el riesgo

Una predicción como:

```text
CHURN = 87%
```

por sí sola puede no ser suficiente para que un usuario de negocio comprenda el resultado y decida cómo actuar.

**Necesidad:** Comprender los principales factores asociados al riesgo identificado.

**Oportunidad:** Incorporar mecanismos de interpretabilidad que permitan mostrar los factores más relevantes para cada predicción.

```text
87% RIESGO

Factores relevantes:
↓ Consumo
↑ Reclamos
↓ Actividad
↑ Incidencias
```

Los factores concretos dependerán de los datos disponibles y del modelo seleccionado.

### Pain Point 05 — Información poco accionable

Un dashboard puede mostrar información general como:

> "8.000 clientes presentan riesgo alto."

Sin embargo, el área de negocio necesita responder preguntas operativas como:

> "¿A cuáles atendemos primero y por qué?"

**Necesidad:** Transformar los resultados analíticos y predictivos en información que facilite la toma de decisiones.

**Oportunidad:** Incorporar:

* segmentos;
* niveles de riesgo;
* priorización;
* alertas;
* indicadores;
* perfiles de clientes;
* insights basados en evidencia.

### Pain Point 06 — Ausencia de seguimiento

La identificación del riesgo no representa el final del proceso. Para evaluar la efectividad de las acciones de fidelización resulta necesario conocer qué ocurrió después de intervenir sobre un cliente.

**Necesidad:** Contar con mecanismos que permitan registrar y analizar los resultados de las acciones realizadas.

**Oportunidad:** Diseñar el producto para permitir posteriormente un ciclo de seguimiento:

```text
PREDICCIÓN
    ↓
ACCIÓN
    ↓
RESULTADO
    ↓
MEDICIÓN
    ↓
APRENDIZAJE
```

Entre los resultados que podrían medirse posteriormente se encuentran:

* clientes intervenidos;
* clientes retenidos;
* churn posterior;
* evolución del riesgo;
* efectividad de las acciones.

Esta capacidad podrá formar parte de una evolución posterior del producto y no necesariamente del MVP inicial.

## 1.4 Mapeo de Stakeholders

### Stakeholders Primarios

| Stakeholder           | Interés | Relación               |
| --------------------- | ------- | ---------------------- |
| Área de Fidelización  | Alto    | Usuario de negocio     |
| Analítica de Negocios | Alto    | Usuario analítico      |
| Dirección / Gerencia  | Alto    | Consumidor estratégico |

### Stakeholders Secundarios

| Stakeholder         | Interés    | Relación            |
| ------------------- | ---------- | ------------------- |
| Atención al Cliente | Alto       | Usuario operativo   |
| IT / Sistemas       | Medio/Alto | Integración         |
| QA / Testing        | Medio      | Calidad             |
| Data Engineering    | Medio/Alto | Datos e integración |

## 1.5 Usuarios del Sistema

### Persona 01 — Analista de Fidelización

**Rol:** Usuario operativo/comercial.

**Objetivo:** Identificar los clientes que requieren acciones de retención.

**Necesita:**

* conocer el riesgo;
* priorizar clientes;
* analizar segmentos;
* comprender factores asociados al riesgo;
* disponer de información actualizada.

**Necesidad principal:**

> Saber dónde concentrar los esfuerzos de fidelización.

### Persona 02 — Analista de Negocios

**Rol:** Usuario analítico.

**Objetivo:** Analizar el comportamiento de la cartera y producir información para la toma de decisiones.

**Necesita:**

* métricas;
* tendencias;
* segmentaciones;
* análisis de churn;
* visualizaciones;
* resultados de modelos.

**Necesidad principal:**

> Transformar datos de clientes en información confiable para la toma de decisiones.

### Persona 03 — Responsable de Atención al Cliente

**Rol:** Usuario operativo.

**Objetivo:** Comprender los problemas e interacciones de los clientes.

**Necesita:**

* historial;
* incidencias;
* motivos de contacto;
* señales de insatisfacción;
* clientes prioritarios.

**Necesidad principal:**

> Detectar señales provenientes de la interacción con el cliente que puedan relacionarse con riesgo de abandono.

### Persona 04 — Gerencia / Dirección

**Rol:** Usuario estratégico.

**Objetivo:** Conocer el estado de la cartera y tomar decisiones.

**Necesita:**

* KPIs;
* evolución del churn;
* impacto económico;
* segmentos;
* tendencias;
* información ejecutiva.

**Necesidad principal:**

> Entender el impacto del churn y dónde actuar.

---

# 2. Definición del Producto

## 2.1 Visión del Producto

**Churn Intelligence** es una plataforma SaaS B2B que ayuda a empresas con grandes carteras de clientes a detectar, comprender y priorizar el riesgo de abandono mediante analítica, segmentación y modelos predictivos de churn.

El producto busca transformar los resultados analíticos en información accionable para que los equipos de negocio puedan tomar decisiones de fidelización basadas en datos.

## 2.2 Product Goals

* **PG-01 — Detectar:** Identificar de forma proactiva clientes con riesgo de abandono.
* **PG-02 — Comprender:** Explicar los factores asociados al score predictivo calculado.
* **PG-03 — Priorizar:** Clasificar clientes y segmentos según criterios de riesgo y valor.
* **PG-04 — Analizar:** Monitorear la evolución de las tasas de churn mediante KPIs.
* **PG-05 — Segmentar:** Agrupar clientes con características relevantes para el análisis.
* **PG-06 — Accionar:** Proporcionar información que facilite la selección de clientes para acciones de retención.

## 2.3 Fronteras del Alcance del MVP

### In Scope

* Ingesta y procesamiento de datasets estructurados.
* Carga de archivos CSV.
* Validación de calidad de datos.
* Dashboard analítico de churn.
* KPIs e indicadores.
* Modelo predictivo de clasificación.
* Churn Score.
* Interpretabilidad individual.
* Consulta individual de clientes.
* Filtrado de cartera.
* Segmentación de clientes.

### Out of Scope

* Gestión automática de campañas de marketing.
* CRM completo.
* Integraciones CRM complejas en tiempo real.
* Facturación.
* Automatización de retención mediante WhatsApp o Call Center.
* Procesamiento de datos por streaming.
* Infraestructura multi-cloud.

## 2.4 Priorización de Características — MoSCoW

### Must Have

* Gestión de organizaciones.
* Autenticación segura.
* Carga de datasets estructurados.
* Validaciones de calidad de datos.
* Dashboard analítico.
* KPIs de churn.
* Predicción mediante Machine Learning.
* Churn Score.
* Interpretabilidad.
* Vista detallada del cliente.

### Should Have

* Exportación de resultados a CSV.
* Filtros avanzados multi-variable.
* Insights descriptivos automatizados.
* Historial de ejecuciones analíticas.

### Could Have

* Alertas tempranas parametrizables.
* Análisis de sentimiento de comentarios o quejas de soporte.

### Won't Have — MVP

* CRM nativo completo.
* Motor de facturación SaaS.
* Envío automatizado de WhatsApp.
* Integraciones de marcado telefónico automatizado.

---

# 3. Factibilidad y Caso de Negocio

## 3.1 Análisis de Viabilidad

### Factibilidad Técnica — Viable

La solución puede desarrollarse utilizando tecnologías y herramientas conocidas por el equipo:

* Python;
* APIs;
* frontend interactivo;
* bases de datos relacionales;
* Scikit-Learn;
* herramientas de interpretabilidad.

### Factibilidad Operativa — Viable

El sistema busca proporcionar inteligencia analítica para apoyar el trabajo de las áreas de negocio, sin reemplazar necesariamente las herramientas de gestión o contacto utilizadas por la organización.

### Factibilidad Temporal — Viable

El MVP se considera viable dentro de un marco estimado de **10 a 20 semanas**, manteniendo controlado el alcance inicial de ingesta mediante CSV y procesamiento batch.

### Factibilidad de Datos — Crítica

La disponibilidad y calidad de los datos representan una dependencia fundamental.

No se construirá el modelo de Machine Learning hasta contar con:

* una definición operacional de churn;
* datos suficientes;
* volumen adecuado;
* granularidad adecuada;
* historial suficiente;
* información correctamente etiquetada.

### Factibilidad Económica — Go Condicionado

Se plantea inicialmente un modelo SaaS basado en suscripción mensual:

$$
MRR = Clientes\ Activos \times Precio\ Mensual\ Promedio
$$

La decisión económica queda condicionada a la validación de la viabilidad analítica y técnica del producto.

## 3.2 Análisis FODA

### Fortalezas

* Problema de negocio cuantificable.
* Orientación SaaS B2B.
* Arquitectura multi-tenant como visión de producto.
* Integración entre Analytics, Machine Learning e información accionable.

### Oportunidades

* Crecimiento de la cultura data-driven.
* Mayor utilización de analítica predictiva.
* Automatización de análisis que actualmente puede realizarse mediante hojas de cálculo.

### Debilidades

* Dependencia de la calidad de los datos de origen.
* Dependencia de la disponibilidad de información histórica.
* Complejidad potencial de integración de múltiples fuentes.

### Amenazas

* Herramientas tradicionales de BI ya adoptadas.
* Resistencia organizacional a incorporar nuevas herramientas.
* Competencia de soluciones analíticas existentes.

---

# 4. Requisitos y Alcance

## 4.1 Requisitos Funcionales

* **RF-005:** El sistema deberá permitir la carga manual de datasets estructurados en formato CSV.
* **RF-006:** El sistema deberá validar automáticamente la estructura lógica y las columnas del dataset cargado.
* **RF-007:** El sistema deberá identificar problemas críticos de calidad, como valores faltantes, duplicados e inconsistencias, antes del procesamiento.
* **RF-015:** El sistema deberá ejecutar el pipeline predictivo para estimar la probabilidad de abandono.
* **RF-016:** El sistema deberá calcular un score de riesgo continuo entre 0 y 1 para cada cliente.
* **RF-017:** El sistema deberá clasificar a los clientes en niveles de riesgo: Alto, Medio y Bajo.
* **RF-018:** El sistema deberá proporcionar información de interpretabilidad individual sobre las variables relevantes para cada predicción.
* **RF-020:** El sistema deberá permitir filtros interactivos basados en niveles de riesgo, segmentos y variables de clientes.
* **RF-022:** El sistema deberá mostrar un dashboard de analítica consolidada con indicadores como tasa de churn, total de clientes y volumen por nivel de riesgo.

## 4.2 Requisitos No Funcionales

* **RNF-002 — Seguridad:** Un usuario no podrá visualizar, procesar o acceder a información perteneciente a otra organización.
* **RNF-004 — Rendimiento:** Las consultas interactivas del dashboard y los filtros deberán ejecutarse en menos de 2 segundos.
* **RNF-005 — Rendimiento:** Los procesos prolongados deberán mostrar indicadores de progreso.
* **RNF-010 — Usabilidad:** La interfaz deberá permitir a usuarios no técnicos comprender y priorizar clientes sin requerir conocimientos especializados en ciencia de datos.
* **RNF-013 — Mantenibilidad:** El sistema deberá mantener una separación modular entre Frontend, Backend, persistencia y servicio predictivo.
* **RNF-014 — Calidad:** Las funciones críticas y los flujos analíticos deberán contar con pruebas de calidad e integración antes del despliegue.

## 4.3 Reglas de Negocio

* **RN-002 — Aislamiento:** Los datos pertenecientes a una organización no podrán estar disponibles para otra organización.
* **RN-004 — Churn:** La definición operacional de churn deberá establecerse antes del modelado analítico final.
* **RN-005 — Score:** El score predictivo representa una estimación probabilística y no deberá presentarse como una certeza determinista de abandono.
* **RN-007 — Interpretabilidad:** Los factores asociados a una predicción no deberán interpretarse directamente como relaciones causales.

---

# 5. Objetivos Analíticos

Los objetivos analíticos corresponden al componente de **Ciencia de Datos y Machine Learning** del producto y utilizan inicialmente el dataset de telecomunicaciones como caso de validación.

## 5.1 Objetivo de Negocio

Identificar anticipadamente a los clientes con mayor riesgo de abandono para apoyar la toma de decisiones y las estrategias de retención.

## 5.2 Objetivo Analítico

Desarrollar un modelo de clasificación binaria capaz de estimar la probabilidad de abandono de un cliente a partir de las características y comportamiento registrados en el dataset.

El resultado del modelo deberá permitir generar un **Churn Score** que pueda utilizarse posteriormente como insumo para la segmentación y priorización.

## 5.3 Pregunta Analítica

> ¿Es posible predecir el abandono de un cliente a partir de sus características y comportamiento registrado?

## 5.4 Preguntas Complementarias para el EDA

* ¿Qué características presentan los clientes que abandonan?
* ¿Qué variables presentan mayor relación con el Churn?
* ¿Existen diferencias relevantes entre clientes que abandonan y permanecen?
* ¿Qué variables podrían resultar relevantes para la predicción?
* ¿Existen patrones o segmentos de clientes asociados con diferentes niveles de abandono?

## 5.5 Métricas de Evaluación

El desempeño de los modelos podrá evaluarse mediante:

* Accuracy
* Precision
* Recall
* F1-Score
* ROC-AUC

La selección e interpretación de las métricas deberá considerar el impacto que tienen los falsos positivos y falsos negativos sobre el problema de negocio.

## 5.6 Metodología — CRISP-DM

El desarrollo analítico seguirá las etapas de **CRISP-DM**:

1. **Comprensión del negocio**
   Definición del problema, objetivos y criterios de éxito.

2. **Comprensión de los datos**
   Exploración del dataset, clasificación de variables, estadísticas descriptivas y visualizaciones.

3. **Preparación de los datos**
   Tratamiento de valores nulos, duplicados, inconsistencias y outliers; transformación de variables; selección de características y preparación para el modelado.

4. **Modelado**
   Desarrollo y comparación de modelos de clasificación, comenzando por algoritmos apropiados para el problema, como Regresión Logística.

5. **Evaluación**
   Validación del desempeño de los modelos mediante las métricas seleccionadas y análisis de sus resultados.

6. **Interpretación**
   Relación de los resultados obtenidos con el problema de negocio y análisis de los factores asociados a las predicciones.

---

# 6. Datos y Recursos

## 6.1 Dataset

El proyecto utiliza inicialmente:

```text
telecom_dirty.csv
```

El dataset contiene problemas de calidad introducidos deliberadamente para trabajar las etapas de exploración y preparación de datos.

## 6.2 Variables Disponibles

Entre las características disponibles se encuentran:

* Variable objetivo: `Churn`
* Variables numéricas de comportamiento y consumo.
* Variables categóricas, incluyendo variables binarias.
* Variable temporal: `RegistrationDate`.

## 6.3 Restricciones

* El análisis estará limitado inicialmente a las variables disponibles en el dataset.
* Los problemas de calidad deberán ser identificados durante el EDA.
* La información temporal disponible está limitada inicialmente a `RegistrationDate`.
* Se utilizarán las herramientas y técnicas abordadas en la materia.
* El desarrollo estará condicionado por el cronograma académico.

## 6.4 Riesgos Analíticos Iniciales

* Datos no suficientemente representativos.
* Problemas de calidad no detectados o tratados incorrectamente.
* Presencia de outliers que afecten el modelado.
* Desbalance entre las clases de Churn.
* Selección inadecuada de variables.
* Data Leakage durante la preparación o modelado.
* Overfitting.
* Bajo desempeño predictivo.

---

# 7. Stack Tecnológico

El desarrollo analítico inicial utiliza:

* **Google Colab**
* **Python**
* **Pandas**
* **Matplotlib**
* **Seaborn**
* **Scikit-Learn**

La arquitectura completa del producto SaaS podrá incorporar posteriormente componentes adicionales para backend, frontend, persistencia, autenticación e infraestructura.

---

# 8. Estructura del Repositorio

```text
├── data/
│   ├── raw/            # Dataset original
│   └── processed/      # Datasets limpios/transformados
│
├── notebooks/          # Notebooks de EDA, preparación y modelado
│
├── src/                # Funciones y utilidades reutilizables
│
├── reports/            # Gráficos, resultados y hallazgos
│
├── docs/               # Documentación del proyecto
│
└── README.md
```

---

# 9. Cómo ejecutar el proyecto

## 9.1 Clonar el repositorio

```bash
git clone <URL_DEL_REPOSITORIO>
cd <NOMBRE_DEL_REPOSITORIO>
```

## 9.2 Agregar el dataset

Colocar el archivo:

```text
telecom_dirty.csv
```

dentro de:

```text
data/raw/
```

## 9.3 Instalar dependencias

```bash
pip install -r requirements.txt
```

## 9.4 Ejecutar los notebooks

Los notebooks pueden ejecutarse localmente o mediante **Google Colab**.

La secuencia recomendada es:

```text
EDA
 ↓
Preparación de datos
 ↓
Modelado
 ↓
Evaluación
 ↓
Interpretación
```

---
