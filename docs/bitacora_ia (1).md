# Bitácora humano-IA

Registro del uso de herramientas de IA generativa durante el proyecto *Agente inteligente para el diagnóstico y evaluación del estado de motores automotrices*.

## Integrantes y reparto de trabajo

| Integrante | Pasos a cargo |
|---|---|
| Yeiban Camilo Herrera Pérez | Repositorio y entorno (paso 1), exploración de datos (paso 2) |
| Valerie Jireth Pájaro Fernández | Propuesta del Hito 1 (paso 0) |
| Salvador Simarra Cassiani | Partición de datos y líneas base (pasos 3 y 4) |

## Herramientas utilizadas

| Herramienta | Uso principal |
|---|---|
| Claude (Anthropic) | Ideas de proyecto, búsqueda de datos, apoyo en código y explicación de conceptos |

## Registro de uso

### Entrada 1 · 2026-10-28

| Campo | Detalle |
|---|---|
| Integrante | Yeiban Herrera |
| Herramienta | Claude |
| Para qué se usó | Lluvia de ideas para el proyecto final y resumen de los temas del material del curso |
| Qué se aceptó, modificó o descartó | Se aceptó la idea de un agente de diagnóstico de motores. Se descartaron las ideas de trading, tickets de soporte e inventario por considerarlas demasiado básicas |
| Cómo se verificó | Discusión en equipo y revisión contra los temas vistos en el curso |

### Entrada 2 · 2026-10-28

| Campo | Detalle |
|---|---|
| Integrante | Yeiban Herrera |
| Herramienta | Claude |
| Para qué se usó | Búsqueda de conjuntos de datos públicos de mantenimiento predictivo |
| Qué se aceptó, modificó o descartó | Se aceptó el dataset de Kaggle *Automotive Vehicles Engine Health* como principal y AI4I 2020 (UCI) como respaldo. Se descartaron EngineFaultDB y NASA C-MAPSS |
| Cómo se verificó | Licencias revisadas manualmente en Kaggle (CC0) y UCI (CC BY 4.0) |

### Entrada 3 · 2026-11-02

| Campo | Detalle |
|---|---|
| Integrante | Yeiban Herrera |
| Herramienta | Claude |
| Para qué se usó | Revisar que la idea cumpliera los lineamientos del proyecto (ruta, línea base, métricas) y redactar el mensaje de consulta al docente |
| Qué se aceptó, modificó o descartó | Se aceptó la ruta C con módulo de reglas complementario. Se modificó el texto del mensaje para explicar mejor el módulo de reglas |
| Cómo se verificó | Comparación con el documento de lineamientos del docente |

### Entrada 4 · 2026-11-10

| Campo | Detalle |
|---|---|
| Integrante | Yeiban Herrera |
| Herramienta | Claude |
| Para qué se usó | Preparar la estructura del repositorio, `requirements.txt`, `README.md` y el notebook de exploración de datos |
| Qué se aceptó, modificó o descartó | Se aceptaron los archivos. Se modificaron las versiones de `requirements.txt` porque pandas 2.2.3 no se instalaba en Python 3.14, y la ruta del CSV en el notebook porque no se encontraba al ejecutarlo desde VS Code |
| Cómo se verificó | Instalación en Windows con Python 3.14 y ejecución completa del notebook |

### Entrada 5 · 2026-11-11

| Campo | Detalle |
|---|---|
| Integrante | Yeiban Herrera |
| Herramienta | Claude |
| Para qué se usó | Completar el notebook de partición iniciado por Salvador Simarra, crear los scripts de partición y líneas base, y actualizar el `README.md` |
| Qué se aceptó, modificó o descartó | Se conservó la celda de carga de datos del notebook original. La lógica se movió a `src/` para cumplir el requisito de ejecución desde scripts |
| Cómo se verificó | Ejecución de `src/particion.py` y `src/lineas_base.py`; la partición se repitió dos veces con resultados idénticos |
