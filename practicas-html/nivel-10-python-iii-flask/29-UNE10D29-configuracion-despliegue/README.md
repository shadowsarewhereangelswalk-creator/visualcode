# UNE10D29 — Fundamentos de configuración y despliegue de Flask

Clase 29 del Nivel 10 — Python III: Flask.

- **Práctica:** Fundamentos de configuración y despliegue de Flask
- **Resultado terminado:** Aplicación configurable para desarrollo, pruebas y producción con Gunicorn y Docker.
- **Herramientas:** Python, Flask y Visual Studio Code
- **Proyecto del nivel:** Servicio Flask

1. Crea y activa un entorno virtual.
2. Ejecuta `python -m pip install -r requirements.txt`.
3. Ejecuta `python app.py` para desarrollo.
4. Para producción, define las variables de `env.example` y ejecuta `gunicorn -c gunicorn.conf.py wsgi:app`.
5. También puedes construir la imagen con `docker build -t flask-desplegable .`.

Comprueba la estructura y la lógica independiente con `python app.py --check`.

