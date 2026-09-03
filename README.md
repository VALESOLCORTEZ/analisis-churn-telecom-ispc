# Análisis del Churn — Telecom

Proyecto del **Módulo Analista de Datos 2** — Tecnicatura Superior en Ciencia de Datos e Inteligencia Artificial, Instituto Superior Politécnico de Córdoba (ISPC).

**Docentes:** Donata Virginia Delfini · Sol Del Valle Figueroa

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

## 3. Plan de proyecto

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

## 4. Estructura del repositorio

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

## 5. Cómo correr el proyecto
1. Clonar el repositorio
2. Colocar `telecom_dirty.csv` en `data/raw/`
3. Instalar dependencias: `pip install -r requirements.txt`
4. Abrir los notebooks en `notebooks/` (o en Google Colab)

