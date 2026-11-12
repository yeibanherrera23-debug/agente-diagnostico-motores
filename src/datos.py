"""Carga del conjunto de datos y constantes compartidas por todo el proyecto."""

from pathlib import Path

import pandas as pd

SEMILLA = 42

VARIABLES = [
    "rpm",
    "presion_aceite",
    "presion_combustible",
    "presion_refrigerante",
    "temp_aceite",
    "temp_refrigerante",
]
OBJETIVO = "condicion"

NOMBRES_COLUMNAS = {
    "Engine rpm": "rpm",
    "Lub oil pressure": "presion_aceite",
    "Fuel pressure": "presion_combustible",
    "Coolant pressure": "presion_refrigerante",
    "lub oil temp": "temp_aceite",
    "Coolant temp": "temp_refrigerante",
    "Engine Condition": "condicion",
}


def raiz_proyecto() -> Path:
    """Ubica la carpeta raíz del proyecto (la que contiene data/ y src/)."""
    candidatas = [Path.cwd(), *Path.cwd().parents, Path(__file__).resolve().parent.parent]
    for carpeta in candidatas:
        if (carpeta / "data").is_dir() and (carpeta / "src").is_dir():
            return carpeta
    raise FileNotFoundError("No se encontró la carpeta raíz del proyecto (con data/ y src/).")


RAIZ = raiz_proyecto()
CARPETA_DATOS = RAIZ / "data"
CARPETA_EXPERIMENTOS = RAIZ / "experiments"


def cargar_datos_originales() -> pd.DataFrame:
    """Lee el CSV original y renombra las columnas a nombres cortos en español."""
    return pd.read_csv(CARPETA_DATOS / "engine_data.csv").rename(columns=NOMBRES_COLUMNAS)


def cargar_particion(nombre: str) -> tuple[pd.DataFrame, pd.Series]:
    """Lee una partición guardada ('entrenamiento', 'validacion' o 'prueba') y la separa en X e y."""
    df = pd.read_csv(CARPETA_DATOS / f"{nombre}.csv")
    return df[VARIABLES], df[OBJETIVO]
