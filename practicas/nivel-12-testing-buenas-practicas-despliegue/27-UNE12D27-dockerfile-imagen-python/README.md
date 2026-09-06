# UNE12D27 — Fundamentos de Dockerfile e imagen de una aplicación Python

Clase 27 del Nivel 12 — Testing, buenas prácticas y despliegue.

- **Práctica:** Fundamentos de Dockerfile e imagen de una aplicación Python
- **Resultado terminado:** API de inventario con imagen multietapa, usuario sin privilegios y health check.
- **Herramientas:** Docker, Flask y Gunicorn y Visual Studio Code
- **Proyecto del nivel:** Aplicación desplegada

1. Crea el entorno con `python -m venv .venv`.
2. Activa el entorno virtual.
3. Ejecuta `python -m pip install -r requirements-dev.txt`.
4. Ejecuta `python app.py`.
5. Ejecuta `python -m pytest`.

Ejecuta `docker build -t une12-practica .` y `docker run --rm -p 8000:8000 une12-practica` para probar la imagen.

Comprueba la estructura con `python app.py --check`.

