# Análisis del Churn — Telecom

Proyecto del **Módulo Analista de Datos 2** — Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial, Instituto Superior Politécnico de Córdoba (ISPC).

**Docente:**  Sol Del Valle Figueroa

**Título del proyecto:** Churn Intelligence SaaS
**Integrantes:**
- Amaya, Brenda
- Amaya, Paula
- Cortez, Valeria
- Manrique Aguad, Agustín
- Martinez, Cristian
- Sudañez, Isaias Emanuel

---

## 1. Comprensión del negocio

### Contexto del problema
Las empresas de telecomunicaciones deben gestionar grandes cantidades de clientes y buscar estrategias para retenerlos. El abandono de un cliente (**Churn**) representa una pérdida de ingresos y la necesidad de captar nuevos clientes. Este proyecto utiliza técnicas de Ciencia de Datos para analizar el comportamiento de los clientes y desarrollar una solución predictiva orientada a identificar el Churn.

### Problema de negocio
> ¿Es posible identificar anticipadamente a los clientes con mayor probabilidad de abandonar el servicio utilizando la información disponible sobre ellos?

### Stakeholders
| Área | Interés |
|---|---|
| Gerencia | Información para mejorar la toma de decisiones |
| Marketing / Retención | Orientar acciones de retención con las predicciones |
| Atención al Cliente | Priorizar clientes según riesgo |
| Ciencia de Datos | Desarrollar el análisis y el modelo predictivo |

### Recursos disponibles
- Dataset `telecom_dirty.csv` (con problemas de calidad introducidos deliberadamente)
- Variable objetivo: `Churn`
- Variables numéricas de comportamiento y consumo
- Variables categóricas, incluyendo binarias
- Variable temporal: `RegistrationDate`

**Stack técnico:** Google Colab · Python · Pandas · Matplotlib · Seaborn · Scikit-Learn

### Restricciones
- Análisis limitado a las variables disponibles en el dataset
- Problemas de calidad a identificar en el EDA y tratar en la preparación de datos
- Información temporal limitada a `RegistrationDate`
- Uso de las herramientas/técnicas vistas en la materia
- Cronograma sujeto al calendario académico

### Riesgos iniciales
- Datos no suficientemente representativos
- Problemas de calidad no detectados/tratados correctamente
- Outliers que afecten el modelado
- Desbalance de clases (Churn vs. no Churn)
- Selección inadecuada de variables
- Data Leakage durante preparación/modelado
- Overfitting
- Bajo desempeño predictivo

## 2. Objetivos analíticos

**Objetivo de negocio:** Identificar anticipadamente a los clientes con mayor riesgo de abandono para apoyar la toma de decisiones y las estrategias de retención.

**Objetivo analítico:** Desarrollar un modelo de clasificación binaria que prediga si un cliente abandonará o permanecerá en el servicio, a partir de las características del dataset.

**Pregunta analítica:**
> ¿Es posible predecir si un cliente abandonará el servicio a partir de sus características y comportamiento registrado?

Preguntas complementarias para el EDA:
- ¿Qué características presentan los clientes que abandonan?
- ¿Qué variables tienen mayor relación con el Churn?
- ¿Qué características podrían ser relevantes para predecir el abandono?

## 3. Relevamiento de Requerimientos (Funcionales y No Funcionales)

| Pain Point | Código | Requerimiento |
|---|---|---|
| **01: Detección tardía del riesgo de abandono** | RF-015 | El sistema deberá ejecutar un modelo predictivo de churn utilizando los datos de los clientes. |
| | RF-016 | El sistema deberá calcular un score de riesgo (probabilidad de 0 a 1) por cliente de forma sistemática. |
| | RF-022 | El sistema deberá generar alertas cuando el score de riesgo de un cliente supere el umbral establecido o cuando se detecten señales relevantes de comportamiento. (Aporte del grupo) |
| | NF-004 | Las operaciones de visualización de scores en tiempo real deberán responder en menos de 2 segundos para el volumen de datos del MVP. |
| | RNF-005 | Los procesos de entrenamiento de modelos prolongados deberán disponer de indicadores de estado de procesamiento visibles. |
| | RNF-014 | El procesamiento e inferencia sobre un lote de hasta 10.000 registros de clientes deberá completarse en un tiempo máximo de 5 segundos tras la ingesta del archivo. (Aporte del grupo) |
| **02: Falta de priorización de la cartera y saturación** | RF-017 | El sistema deberá clasificar automáticamente a los clientes en tres niveles de riesgo (Alto, Medio, Bajo) según umbrales definidos. |
| | RF-020 | El sistema deberá permitir filtrar y ordenar la lista de clientes según nivel de riesgo, segmento y valor. |
| | RF-023 | El sistema deberá permitir segmentar clientes críticos para facilitar la ejecución de campañas de retención personalizadas. (Aporte del grupo) |
| | RNF-010 | La interfaz gráfica deberá ser intuitiva, permitiendo que un usuario de negocio (fidelización) comprenda y priorice los casos de riesgo sin necesidad de tener conocimientos técnicos avanzados de Machine Learning. |
| | RNF-011 | Los usuarios deberán poder acceder al perfil y nivel de riesgo de cualquier cliente en un máximo de 3 clics. (Aporte del grupo) |
| **03: Información distribuida, fragmentada y en silos** | RF-005 | El sistema deberá permitir la carga centralizada de datasets estructurados (archivos CSV/Excel) con variables de facturación, comportamiento y servicio. (Aporte del grupo) |
| | RF-007 | El sistema deberá identificar de forma automática errores, valores nulos, duplicados e inconsistencias de datos. |
| | RF-024 | El sistema deberá integrar variables de plan, consumo, historial de soporte y estado de cuenta para disponer de una visión consolidada del cliente. (Aporte del grupo) |
| | RNF-002 | El sistema deberá garantizar el aislamiento absoluto de los datos entre diferentes organizaciones (arquitectura multi-tenant), impidiendo estrictamente que cualquier usuario acceda a datos de otra compañía. |
| | RNF-012 | El sistema deberá implementar autenticación basada en credenciales y control de acceso para restringir el acceso a datos sensibles y de facturación exclusivamente al personal autorizado. (Aporte del grupo) |
| **04: Dificultad para explicar e interpretar el riesgo** | RF-018 | El sistema deberá proporcionar y visualizar los principales factores de comportamiento que más influyen en el score de riesgo de cada cliente (interpretabilidad individual). |
| | RF-021 | El sistema deberá mostrar una vista detallada del perfil del cliente con sus variables explicativas. |
| | RNF-013 | La arquitectura de software deberá mantener una estricta separación de capas (Presentación, Lógica de Negocio, Procesamiento de Datos y Componente Analítico de ML) para asegurar la mantenibilidad del sistema. |
| **05: Información analítica poco accionable** | RF-019 | El sistema deberá proporcionar un dashboard analítico con métricas de abandono segmentadas por tipo de plan, servicios adicionales y volumen de reclamos. (Aporte del grupo) |
| | RF-025 | El sistema deberá permitir visualizar indicadores relacionados con consumo, facturación, contratación e interacciones de soporte para facilitar el análisis de los segmentos de riesgo. (Aporte del grupo) |
| | RNF-010 | La interfaz deberá facilitar la interpretación de los indicadores y la identificación de clientes prioritarios por parte de usuarios de negocio. |
| **06: Ausencia de seguimiento y trazabilidad del proceso** | RF-026 | El sistema deberá registrar las acciones de retención realizadas sobre clientes identificados como de riesgo y permitir consultar su resultado. |
| | RF-027 | El sistema deberá permitir realizar seguimiento de los clientes intervenidos para evaluar posteriormente su comportamiento frente al churn. (Aporte del grupo) |
| | RNF-015 | La arquitectura deberá ser modular para facilitar la ejecución de pruebas por parte del equipo de QA y permitir el despliegue de nuevos modelos de análisis sin afectar el frontend principal. (Aporte del grupo) |

## 4. Plan de proyecto

### Criterios de éxito
- Analizar correctamente calidad y características del dataset
- Identificar patrones relevantes relacionados con el Churn
- Desarrollar y validar un modelo de clasificación adecuado
- Obtener métricas de evaluación satisfactorias
- Interpretar los resultados en relación al problema planteado

**Métricas de evaluación:** Accuracy · Precision · Recall · F1-score · ROC-AUC

### Metodología (CRISP-DM)
1. **Comprensión del negocio** — problema, objetivos, criterios de éxito ✅
2. **Comprensión de los datos** — EDA, clasificación de variables, estadísticas descriptivas y visualizaciones ⏳ *(etapa actual)*
3. **Preparación de los datos** — tratamiento de nulos, duplicados, inconsistencias, outliers, transformación de la variable temporal, selección de características
4. **Modelado** — modelos de clasificación (Regresión Logística, entre otros)
5. **Evaluación** — validación y análisis de métricas
6. **Interpretación** — resultados y relación con el problema inicial

## 5. Estructura del repositorio

```
├── data/
│   ├── raw/            # Dataset original (telecom_dirty.csv)
│   └── processed/      # Datasets limpios/transformados
├── notebooks/          # Notebooks de EDA, preparación y modelado
├── src/                # Funciones y utilidades reutilizables
├── reports/            # Gráficos, resultados y hallazgos
├── docs/               # Documentación del proyecto (CRISP-DM, entregas)
└── README.md
```

## 6. Cómo correr el proyecto
1. Clonar el repositorio
2. Colocar `telecom_dirty.csv` en `data/raw/`
3. Instalar dependencias: `pip install -r requirements.txt`
4. Abrir los notebooks en `notebooks/` (o en Google Colab)
