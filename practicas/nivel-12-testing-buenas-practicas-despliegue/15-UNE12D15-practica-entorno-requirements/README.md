# UNE12D15 — Práctica P2: configuración de un entorno virtual y requirements.txt

Clase 15 del Nivel 12 — Testing, buenas prácticas y despliegue.

- **Práctica:** Práctica P2: configuración de un entorno virtual y requirements.txt
- **Resultado terminado:** Conversor de monedas con dependencias de ejecución y desarrollo separadas.
- **Herramientas:** venv, requirements, Ruff y Black y Visual Studio Code
- **Proyecto del nivel:** Aplicación desplegada

1. Crea el entorno con `python -m venv .venv`.
2. Activa el entorno virtual.
3. Ejecuta `python -m pip install -r requirements-dev.txt`.
4. Ejecuta `python app.py`.
5. Ejecuta `python -m pytest`.

Ejecuta `ruff check .` para validar el análisis estático.

Ejecuta `black --check .` para comprobar el formato.

Comprueba la estructura con `python app.py --check`.

