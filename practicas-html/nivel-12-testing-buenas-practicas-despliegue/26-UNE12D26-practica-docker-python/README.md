# UNE12D26 — Práctica P4: contenerización de una aplicación Python con Docker

Clase 26 del Nivel 12 — Testing, buenas prácticas y despliegue.

- **Práctica:** Práctica P4: contenerización de una aplicación Python con Docker
- **Resultado terminado:** API de tareas contenerizada con build multietapa, Compose y pruebas.
- **Herramientas:** Docker, Compose, Flask y Gunicorn y Visual Studio Code
- **Proyecto del nivel:** Aplicación desplegada

1. Crea el entorno con `python -m venv .venv`.
2. Activa el entorno virtual.
3. Ejecuta `python -m pip install -r requirements-dev.txt`.
4. Ejecuta `python app.py`.
5. Ejecuta `python -m pytest`.

Ejecuta `docker build -t une12-practica .` y `docker run --rm -p 8000:8000 une12-practica` para probar la imagen.

Ejecuta `docker compose up --build` para iniciar la práctica con Compose.

Comprueba la estructura con `python app.py --check`.

