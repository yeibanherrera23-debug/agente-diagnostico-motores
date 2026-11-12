"""Evaluación de las líneas base: clasificador de clase predominante y regresión logística.

Uso: python src/lineas_base.py   (requiere haber ejecutado antes src/particion.py)
Genera experiments/lineas_base_cv.csv y experiments/lineas_base_validacion.csv.
El conjunto de prueba no se usa en este paso.
"""

import json

import pandas as pd
from sklearn.dummy import DummyClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, recall_score, roc_auc_score
from sklearn.model_selection import StratifiedKFold, cross_validate
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

from datos import CARPETA_EXPERIMENTOS, SEMILLA, cargar_particion

METRICAS = {
    "f1_macro": "f1_macro",
    "auc": "roc_auc",
    "recall_defectuoso": "recall",
    "exactitud": "accuracy",
}


def modelos_base() -> dict:
    """Las dos líneas base declaradas en la propuesta."""
    return {
        "Clase predominante": DummyClassifier(strategy="most_frequent"),
        # El escalador va dentro del Pipeline: en cada pliegue se ajusta solo con los datos de entrenamiento.
        "Regresión logística": Pipeline([
            ("escalador", StandardScaler()),
            ("modelo", LogisticRegression(max_iter=1000, random_state=SEMILLA)),
        ]),
    }


def validacion_cruzada(modelos: dict, X, y) -> pd.DataFrame:
    """Validación cruzada estratificada de 5 pliegues: media y desviación estándar de cada métrica."""
    cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=SEMILLA)
    filas = []
    for nombre, modelo in modelos.items():
        r = cross_validate(modelo, X, y, cv=cv, scoring=METRICAS)
        fila = {"modelo": nombre}
        for metrica in METRICAS:
            valores = r[f"test_{metrica}"]
            fila[f"{metrica}_media"] = round(valores.mean(), 4)
            fila[f"{metrica}_desv"] = round(valores.std(), 4)
        filas.append(fila)
    return pd.DataFrame(filas)


def evaluar_en_validacion(modelos: dict, X_ent, y_ent, X_val, y_val) -> pd.DataFrame:
    """Entrena con todo el conjunto de entrenamiento y mide en el conjunto de validación."""
    filas = []
    for nombre, modelo in modelos.items():
        modelo.fit(X_ent, y_ent)
        prediccion = modelo.predict(X_val)
        probabilidad = modelo.predict_proba(X_val)[:, 1]
        filas.append({
            "modelo": nombre,
            "f1_macro": round(f1_score(y_val, prediccion, average="macro"), 4),
            "auc": round(roc_auc_score(y_val, probabilidad), 4),
            "recall_defectuoso": round(recall_score(y_val, prediccion), 4),
            "exactitud": round(accuracy_score(y_val, prediccion), 4),
        })
    return pd.DataFrame(filas)


def main() -> None:
    X_ent, y_ent = cargar_particion("entrenamiento")
    X_val, y_val = cargar_particion("validacion")

    CARPETA_EXPERIMENTOS.mkdir(exist_ok=True)
    tabla_cv = validacion_cruzada(modelos_base(), X_ent, y_ent)
    tabla_val = evaluar_en_validacion(modelos_base(), X_ent, y_ent, X_val, y_val)

    tabla_cv.to_csv(CARPETA_EXPERIMENTOS / "lineas_base_cv.csv", index=False)
    tabla_val.to_csv(CARPETA_EXPERIMENTOS / "lineas_base_validacion.csv", index=False)
    with open(CARPETA_EXPERIMENTOS / "configuracion.json", "w", encoding="utf-8") as f:
        json.dump({"semilla": SEMILLA, "particion": "70/15/15 estratificada", "pliegues_cv": 5}, f, indent=2)

    print("Validación cruzada (5 pliegues, conjunto de entrenamiento):")
    print(tabla_cv.to_string(index=False))
    print("\nConjunto de validación:")
    print(tabla_val.to_string(index=False))


if __name__ == "__main__":
    main()
