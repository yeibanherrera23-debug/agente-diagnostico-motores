"""Partición estratificada 70/15/15 del conjunto de datos, con semilla fija.

Uso: python src/particion.py
Genera data/entrenamiento.csv, data/validacion.csv y data/prueba.csv.
"""

import pandas as pd
from sklearn.model_selection import train_test_split

from datos import CARPETA_DATOS, OBJETIVO, SEMILLA, cargar_datos_originales


def particionar(df: pd.DataFrame) -> dict[str, pd.DataFrame]:
    """Divide en entrenamiento (70 %), validación (15 %) y prueba (15 %), conservando la proporción de clases."""
    entrenamiento, resto = train_test_split(
        df, test_size=0.30, stratify=df[OBJETIVO], random_state=SEMILLA
    )
    validacion, prueba = train_test_split(
        resto, test_size=0.50, stratify=resto[OBJETIVO], random_state=SEMILLA
    )
    return {"entrenamiento": entrenamiento, "validacion": validacion, "prueba": prueba}


def verificar_sin_solapamiento(particiones: dict[str, pd.DataFrame]) -> None:
    """Comprueba que ningún registro aparezca en más de una partición."""
    indices = [set(p.index) for p in particiones.values()]
    for i in range(len(indices)):
        for j in range(i + 1, len(indices)):
            assert not indices[i] & indices[j], "Hay registros repetidos entre particiones"


def resumen(particiones: dict[str, pd.DataFrame], total: int) -> pd.DataFrame:
    """Tamaño y proporción de motores defectuosos en cada partición."""
    filas = []
    for nombre, p in particiones.items():
        filas.append({
            "particion": nombre,
            "registros": len(p),
            "porcentaje_del_total": round(len(p) / total * 100, 2),
            "porcentaje_defectuoso": round(p[OBJETIVO].mean() * 100, 2),
        })
    return pd.DataFrame(filas)


def main() -> None:
    df = cargar_datos_originales()
    particiones = particionar(df)
    verificar_sin_solapamiento(particiones)
    for nombre, p in particiones.items():
        p.to_csv(CARPETA_DATOS / f"{nombre}.csv", index=False)
    print(resumen(particiones, len(df)).to_string(index=False))
    print(f"\nParticiones guardadas en {CARPETA_DATOS} (semilla {SEMILLA}).")


if __name__ == "__main__":
    main()
