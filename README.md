# Agente inteligente para el diagnóstico y evaluación del estado de motores automotrices

Proyecto final del curso de Inteligencia Artificial, Universidad Tecnológica de Bolívar.

**Integrantes:** Yeiban Camilo Herrera Pérez, Valerie Jireth Pájaro Fernández, Salvador Simarra Cassiani.

## Descripción

Agente de apoyo al diagnóstico de motores con dos módulos:

- **Módulo 1 — Diagnóstico basado en reglas:** a partir de los síntomas que reporta el usuario, identifica el sistema probablemente afectado (combustible, lubricación o enfriamiento), sugiere causas y recomienda revisiones.
- **Módulo 2 — Evaluación con aprendizaje automático:** a partir de seis lecturas de sensores, clasifica el motor como normal o defectuoso y explica su decisión.

Ruta principal: C (aprendizaje automático). Complemento: razonamiento con reglas (ruta B).

## Datos

- **Fuente:** [Automotive Vehicles Engine Health Dataset](https://www.kaggle.com/datasets/parvmodi/automotive-vehicles-engine-health-dataset) (Kaggle, parvmodi).
- **Licencia:** CC0: Public Domain.
- **Tamaño:** 19.535 registros, 6 variables numéricas y la etiqueta `Engine Condition` (0 = normal, 1 = defectuoso).
- **Archivo:** `data/engine_data.csv`. No contiene datos personales.

## Estructura del repositorio

```
data/          Conjunto de datos
notebooks/     Exploración de datos
src/           Código de la solución
experiments/   Resultados de los experimentos y semilla utilizada
docs/          Bitácora de uso de IA generativa
```

## Instalación y ejecución

Requiere Python 3.11 a 3.14.

```bash
python -m venv .venv
.venv\Scripts\activate          # Windows  (Linux/macOS: source .venv/bin/activate)
pip install -r requirements.txt
python src/particion.py
python src/lineas_base.py
```

- `src/particion.py` divide los datos en entrenamiento, validación y prueba (70/15/15, estratificada, semilla 42) y los guarda en `data/`.
- `src/lineas_base.py` evalúa el clasificador de clase predominante y la regresión logística con validación cruzada de 5 pliegues y en el conjunto de validación. Los resultados quedan en `experiments/`.

## Resultados actuales

Líneas base, validación cruzada de 5 pliegues sobre el conjunto de entrenamiento:

| Modelo | F1-macro | AUC | Recall defectuoso | Exactitud |
|---|---|---|---|---|
| Clase predominante | 0,387 | 0,500 | 1,000 | 0,631 |
| Regresión logística | 0,576 ± 0,007 | 0,688 | 0,875 | 0,660 |

## Notebooks

- `notebooks/01_exploracion_datos.ipynb`: exploración de datos.
- `notebooks/02_particion_y_lineas_base.ipynb`: partición sin fuga y líneas base.
