# UNE10D30 — Práctica P5: proyecto de servicio web Flask con base de datos y despliegue

Clase 30 del Nivel 10 — Python III: Flask.

- **Práctica:** Práctica P5: proyecto de servicio web Flask con base de datos y despliegue
- **Resultado terminado:** Servicio completo con interfaz, API, base de datos, migración, pruebas y despliegue.
- **Herramientas:** Python, Flask, SQLAlchemy, Alembic y Visual Studio Code
- **Proyecto del nivel:** Servicio Flask

1. Crea y activa un entorno virtual.
2. Ejecuta `python -m pip install -r requirements.txt`.
3. Ejecuta `flask --app app db upgrade`.
4. Ejecuta `flask --app app run --debug`.
5. Ejecuta `python -m pytest` para comprobar el servicio.
6. Para producción, define las variables de `env.example` y ejecuta `gunicorn -c gunicorn.conf.py wsgi:app`.

Comprueba la estructura y la lógica independiente con `python app.py --check`.

