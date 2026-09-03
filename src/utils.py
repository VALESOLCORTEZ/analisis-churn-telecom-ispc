"""
utils.py
Funciones reutilizables para el proyecto "Análisis del Churn - Telecom".
Cubren carga de datos, exploración/calidad de datos y visualizaciones
que se repiten a lo largo de los distintos notebooks (EDA, limpieza,
modelado).

Uso típico en un notebook:
    from src.utils import cargar_dataset, resumen_calidad, reporte_nulos
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# ---------------------------------------------------------------------------
# Carga de datos
# ---------------------------------------------------------------------------

def cargar_dataset(path: str, encoding: str = "utf-8-sig") -> pd.DataFrame:
    """
    Carga el dataset desde un archivo CSV.

    Intenta primero con la codificación indicada (por defecto utf-8-sig,
    que evita el problema del BOM en archivos exportados desde Excel) y,
    si falla, reintenta con latin-1, que suele resolver casos con
    caracteres especiales mal codificados.

    Parameters
    ----------
    path : str
        Ruta al archivo CSV (por ejemplo "data/raw/telecom_dirty.csv").
    encoding : str
        Codificación a intentar primero.

    Returns
    -------
    pd.DataFrame
    """
    try:
        df = pd.read_csv(path, encoding=encoding)
    except UnicodeDecodeError:
        df = pd.read_csv(path, encoding="latin-1")

    assert not df.empty, f"El archivo {path} se cargó vacío, revisar la fuente."
    print(f"Dataset cargado: {df.shape[0]} filas x {df.shape[1]} columnas")
    return df


# ---------------------------------------------------------------------------
# Exploración y calidad de datos
# ---------------------------------------------------------------------------

def resumen_estructura(df: pd.DataFrame) -> pd.DataFrame:
    """
    Devuelve un resumen por columna: tipo de dato, cantidad de valores
    únicos y un ejemplo de valor. Sirve como primer vistazo para
    clasificar variables en numéricas, categóricas, binarias o de fecha.
    """
    resumen = pd.DataFrame({
        "tipo_dato": df.dtypes,
        "valores_unicos": df.nunique(),
        "ejemplo": df.iloc[0] if len(df) > 0 else np.nan,
    })
    return resumen


def reporte_nulos(df: pd.DataFrame) -> pd.DataFrame:
    """
    Reporta la cantidad y el porcentaje de valores nulos por columna,
    ordenado de mayor a menor. Solo incluye columnas con al menos un nulo.
    """
    nulos = df.isnull().sum()
    porcentaje = (nulos / len(df) * 100).round(2)
    reporte = pd.DataFrame({"nulos": nulos, "% nulos": porcentaje})
    reporte = reporte[reporte["nulos"] > 0].sort_values("% nulos", ascending=False)
    return reporte


def reporte_duplicados(df: pd.DataFrame, subset: list = None) -> pd.DataFrame:
    """
    Devuelve las filas duplicadas del dataset.

    Parameters
    ----------
    subset : list, opcional
        Columnas a considerar para definir un duplicado (por ejemplo,
        un identificador de cliente). Si no se especifica, se comparan
        todas las columnas (duplicado exacto de fila completa).
    """
    duplicados = df[df.duplicated(subset=subset, keep=False)]
    print(f"Filas duplicadas encontradas: {len(duplicados)}")
    return duplicados.sort_values(subset if subset else df.columns.tolist())


def reporte_atipicos(df: pd.DataFrame, columna: str, factor: float = 1.5) -> pd.DataFrame:
    """
    Detecta outliers en una columna numérica usando el método IQR
    (rango intercuartílico) y devuelve las filas fuera de ese rango.

    Parameters
    ----------
    columna : str
        Nombre de la columna numérica a analizar.
    factor : float
        Multiplicador del IQR para definir los límites (1.5 es el
        estándar; usar un valor mayor, ej. 3, para detectar solo
        outliers extremos).
    """
    q1 = df[columna].quantile(0.25)
    q3 = df[columna].quantile(0.75)
    iqr = q3 - q1
    limite_inferior = q1 - factor * iqr
    limite_superior = q3 + factor * iqr

    atipicos = df[(df[columna] < limite_inferior) | (df[columna] > limite_superior)]
    print(f"'{columna}': {len(atipicos)} valores atípicos "
          f"(límites: {limite_inferior:.2f} a {limite_superior:.2f})")
    return atipicos


def resumen_calidad(df: pd.DataFrame) -> None:
    """
    Imprime un resumen rápido de calidad de datos: dimensiones, nulos
    totales, duplicados totales y tipos de datos. Pensado como primer
    chequeo al abrir un dataset nuevo o una versión intermedia.
    """
    print(f"Dimensiones: {df.shape[0]} filas x {df.shape[1]} columnas")
    print(f"Valores nulos totales: {df.isnull().sum().sum()}")
    print(f"Filas duplicadas (exactas): {df.duplicated().sum()}")
    print("\nTipos de datos:")
    print(df.dtypes.value_counts())


# ---------------------------------------------------------------------------
# Visualizaciones reutilizables
# ---------------------------------------------------------------------------

def graficar_distribucion(df: pd.DataFrame, columna: str, hue: str = None) -> None:
    """
    Grafica un histograma con curva de densidad (KDE) para una columna
    numérica. Si se pasa `hue` (por ejemplo la variable Churn), separa
    la distribución por esa categoría.
    """
    plt.figure(figsize=(8, 5))
    sns.histplot(data=df, x=columna, hue=hue, kde=True, multiple="stack")
    plt.title(f"Distribución de {columna}")
    plt.xlabel(columna)
    plt.ylabel("Frecuencia")
    plt.tight_layout()
    plt.show()


def graficar_boxplot(df: pd.DataFrame, columna: str, hue: str = None) -> None:
    """
    Grafica un boxplot de una columna numérica, útil para visualizar
    outliers detectados con reporte_atipicos(). Si se pasa `hue`,
    compara la distribución entre categorías (por ejemplo Churn=Sí/No).
    """
    plt.figure(figsize=(6, 5))
    if hue:
        sns.boxplot(data=df, x=hue, y=columna)
    else:
        sns.boxplot(data=df, y=columna)
    plt.title(f"Boxplot de {columna}")
    plt.tight_layout()
    plt.show()


def graficar_correlaciones(df: pd.DataFrame, columnas_numericas: list = None) -> None:
    """
    Grafica un heatmap de correlaciones entre variables numéricas.
    Si no se especifican columnas, usa todas las numéricas del dataset.
    """
    columnas = columnas_numericas or df.select_dtypes(include=np.number).columns.tolist()
    corr = df[columnas].corr()

    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, fmt=".2f", cmap="coolwarm", center=0)
    plt.title("Matriz de correlación")
    plt.tight_layout()
    plt.show()


def graficar_churn_por_categoria(df: pd.DataFrame, columna_categorica: str, columna_churn: str = "Churn") -> None:
    """
    Grafica la proporción de Churn dentro de cada categoría de una
    variable categórica (por ejemplo tipo de contrato, forma de pago).
    Útil para responder "¿qué características presentan los clientes
    que abandonan?" durante el EDA.
    """
    plt.figure(figsize=(8, 5))
    sns.countplot(data=df, x=columna_categorica, hue=columna_churn)
    plt.title(f"{columna_churn} según {columna_categorica}")
    plt.xticks(rotation=45, ha="right")
    plt.tight_layout()
    plt.show()
