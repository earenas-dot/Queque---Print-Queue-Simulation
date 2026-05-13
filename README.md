# Simulación de Cola de Impresión en Python

## Descripción

Este proyecto consiste en una simulación de una cola de impresión desarrollada en Python utilizando Programación Orientada a Objetos (POO) y la estructura de datos Queue.

El sistema simula cómo distintos trabajos de impresión llegan a una impresora, esperan en una cola y son procesados en orden de llegada utilizando el modelo FIFO (First In First Out).

Además, el proyecto incluye una interfaz gráfica desarrollada con Tkinter para facilitar la interacción del usuario.

---

# Objetivo

Simular el comportamiento de una impresora que recibe múltiples trabajos de impresión durante un período de tiempo, almacenándolos en una cola y procesándolos uno por uno.

---

# Características del sistema

El programa permite:

- Generar trabajos de impresión aleatorios
- Almacenar trabajos en una cola FIFO
- Procesar un trabajo a la vez
- Simular el tiempo de impresión
- Calcular métricas de rendimiento
- Mostrar resultados en una interfaz gráfica

---

# Tecnologías utilizadas

- Python 3
- Tkinter
- Programación Orientada a Objetos
- Estructura de datos Queue

---

# Estructura del proyecto

```text
simulacion_cola/
│
├── main.py
├── gui.py
├── simulation.py
├── printer.py
├── print_task.py
├── queue_custom.py
└── tests.py
