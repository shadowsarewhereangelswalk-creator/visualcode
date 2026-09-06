# UNE12D29 — Fundamentos de despliegue de Flask o Django en la nube

Clase 29 del Nivel 12 — Testing, buenas prácticas y despliegue.

- **Práctica:** Fundamentos de despliegue de Flask o Django en la nube
- **Resultado terminado:** Aplicación web de producción con health check y configuración para Render.
- **Herramientas:** Flask, Gunicorn, Docker y Render y Visual Studio Code
- **Proyecto del nivel:** Aplicación desplegada

1. Crea el entorno con `python -m venv .venv`.
2. Activa el entorno virtual.
3. Ejecuta `python -m pip install -r requirements-dev.txt`.
4. Ejecuta `python app.py`.
5. Ejecuta `python -m pytest`.

Ejecuta `docker build -t une12-practica .` y `docker run --rm -p 10000:10000 une12-practica` para probar la imagen.

Comprueba la estructura con `python app.py --check`.
