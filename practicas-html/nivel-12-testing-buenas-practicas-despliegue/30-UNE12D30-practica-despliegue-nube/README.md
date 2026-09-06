# UNE12D30 — Práctica P5: proyecto de despliegue de una aplicación Flask o Django en la nube

Clase 30 del Nivel 12 — Testing, buenas prácticas y despliegue.

- **Práctica:** Práctica P5: proyecto de despliegue de una aplicación Flask o Django en la nube
- **Resultado terminado:** Panel de despliegue con APIs operativas, seguridad, CI, cobertura total y configuración de nube.
- **Herramientas:** Flask, pytest, GitHub Actions, Docker, Compose y Render y Visual Studio Code
- **Proyecto del nivel:** Aplicación desplegada

1. Crea el entorno con `python -m venv .venv`.
2. Activa el entorno virtual.
3. Ejecuta `python -m pip install -r requirements-dev.txt`.
4. Ejecuta `python app.py`.
5. Ejecuta `python -m pytest`.

Ejecuta `ruff check .` para validar el análisis estático.

Ejecuta `black --check .` para comprobar el formato.

Ejecuta `coverage run -m pytest` y `coverage report` para comprobar la cobertura.

Ejecuta `docker build -t une12-practica .` y `docker run --rm -p 10000:10000 une12-practica` para probar la imagen.

Ejecuta `docker compose up --build` para iniciar la práctica con Compose.

Comprueba la estructura con `python app.py --check`.
