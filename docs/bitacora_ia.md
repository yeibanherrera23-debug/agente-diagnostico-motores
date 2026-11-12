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
| Claude (Anthropic) | Apoyo en código y explicación de conceptos |

## Registro de uso

### Entrada 1 · 2026-11-9

| Campo | Detalle |
|---|---|
| Integrante | Yeiban Herrera |
| Herramienta | Claude |
| Para qué se usó | Preparar el notebook de exploración de datos |
| Qué se aceptó, modificó o descartó | Se aceptaron los archivos. |
| Cómo se verificó | Instalación en Windows con Python 3.14 y ejecución completa del notebook |
### Entrada 2 · 2026-11-11

| Campo | Detalle |
|---|---|
| Integrante | Yeiban Herrera |
| Herramienta | Claude |
| Para qué se usó | Completar el notebook de partición iniciado por Salvador Simarra, crear los scripts de partición y líneas base |
| Qué se aceptó, modificó o descartó | Se conservó la celda de carga de datos del notebook original. La lógica se movió a `src/` para cumplir el requisito de ejecución desde scripts |
| Cómo se verificó | Ejecución de `src/particion.py` y `src/lineas_base.py` |
